import dataclasses
import json
import os
from dataclasses import dataclass
from dataclasses_json import dataclass_json
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@dataclass_json
@dataclass
class Spell:
    spell_name: str
    spell_school: str
    rulebook: str
    effect: str
    duration: str
    spell_range: str
    components: str
    casting_time: str
    spell_level: int


class EnhancedJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if dataclasses.is_dataclass(o):
            return dataclasses.asdict(o)
        return super().default(o)


options = Options()
options.headless = True
load_dotenv()
webdriver_path = os.getenv('WEBDRIVER_PATH')
driver = webdriver.Chrome(options=options, executable_path=webdriver_path)

try:
    base_url = f'https://dndtools.net/spells/'
    sleep(0.1)
    driver.get(base_url)
    dnd_classes = []
    dnd_classes_select = driver.find_element(By.ID, 'id_class_levels__slug')
    dnd_classes_options = dnd_classes_select.find_elements(By.TAG_NAME, "option")
    for dnd_class in dnd_classes_options[-1]:
        dnd_classes.append(dnd_class.text)

    for dnd_class in dnd_classes:
        class_spells = []
        for spell_level in range(1, 10):
            max_page = 1
            page = 1
            while page <= max_page:
                try:
                    base_url = f'https://dndtools.net/spells/?page={page}&class_levels__slug={dnd_class}&spellclasslevel__level={spell_level}'
                    sleep(0.1)
                    driver.get(base_url)
                    max_page = int(driver.find_elements(By.CLASS_NAME, 'page')[-1].text)
                    spells = driver.find_elements(By.TAG_NAME, 'tr')
                    print(f'Scrapping page {base_url}')
                    for spell in spells[1:]:
                        print(spell.text)
                        try:
                            spell_name = spell.find_elements(By.TAG_NAME, "td")[0].text
                            spell_school = spell.find_elements(By.TAG_NAME, "td")[1].text
                            rulebook = spell.find_elements(By.TAG_NAME, "td")[2].text
                            effect = spell.find_elements(By.TAG_NAME, "td")[3].text
                            duration = spell.find_elements(By.TAG_NAME, "td")[4].text
                            spell_range = spell.find_elements(By.TAG_NAME, "td")[5].text
                            components = spell.find_elements(By.TAG_NAME, "td")[6].text
                            casting_time = spell.find_elements(By.TAG_NAME, "td")[7].text
                            class_spell = Spell(spell_name=spell_name, spell_school=spell_school, rulebook=rulebook, effect=effect,
                                                duration=duration, spell_range=spell_range, casting_time=casting_time,
                                                components=components, spell_level=spell_level)
                            class_spells.append(class_spell)
                        except:
                            continue
                except:
                    continue
                page = page + 1
        str_spells = Spell.schema().dumps(class_spells, many=True)
        with open(f'{dnd_class}.json', 'w') as f:
            f.write(str_spells)
            print(f'{dnd_class}.json was created')
finally:
    driver.quit()
