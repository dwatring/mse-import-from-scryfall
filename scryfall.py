import requests
import time
import json
from types import SimpleNamespace


input = """underrealm lich
trackers instincts
doomed artisan
changeling outcast
ingenious infiltrator
cabal therapist
ishkanah grafwidow
bygone bishop
glare of subdual
soul shatter
vorinclex monstrous raider
casualties of war
punishing fire
ethereal forager
Reidane, God of the Worthy
clarion spirit
tombstalker
mire triton
icehide golem
defile
elspeth conquers death
eliminate
ice fang coatl
avalanche riders
mazemind tome
desolate lighthouse
nephalia drownyard
anguished unmaking
irencrag pyromancer
skyknight vanguard
grim flayer
Stoneforge Mystic
Thalia Guardian of Thraben
Councils Judgment
Glen Elendra Archmage
Daze
Ponder
marsh flats
Goblin Guide
misty rainforest
overgrown tomb
polluted delta
scalding tarn
sacred foundry
stomping ground
steam vents
temple garden
verdant catacombs
windswept heath
watery grave
wooded foothills
godless shrine
hallowed fountain
karakas
gaeas cradle
flooded strand
creeping tar pit
blood crypt
bloodstained mire
breeding pool
arid mesa
batterskull
sword of fire and ice
sword of feast and famine
crucible of worlds
Uro Titan of Natures Wrath
thief of sanity
Dragonlord Atarka
needleverge pathway
Blightstep Pathway
Sprite Dragon
pack rat
Aurelia Exemplar of Justice
Meren of Clan Nel Toth
Dream Trawler
Fallen Shinobi
Dig Through Time
Birthing Pod
Hydroid Krasis
Falkenrath Aristocrat
The Scarab God
Boros Charm
Judith the Scourge Diva
Spell Queller
Edric Spymaster of Trest
Maelstrom Pulse
Baleful Strix
Assassins Trophy
Vindicate
Bloodbraid Elf
Kolaghans Command
Trostani Discordant
Teferi, Hero of Dominaria
Ashiok, Nightmare Weaver
Daretti, Ingenious Iconoclast
Wrenn and Six
Sorin, Lord of Innistrad
Oko, Thief of Crowns
Dack Fayden
Gideon, Ally of Zendikar
Elspeth, Sun's Champion
Tezzeret, Artifice Master
Jace, the Mind Sculptor
Jace, Wielder of Mysteries
Liliana of the Veil
Liliana, the Last Hope
Chandra, Flamecaller
Daretti, Scrap Savant
Chandra, Torch of Defiance
Nissa, Voice of Zendikar
Garruk Relentless
Garruk Wildspeaker
Nissa, Who Shakes the World"""

def getColors(inputs, colorList): 
  if inputs.find("W") != -1:
    colorList.append('white')
  if inputs.find("G") != -1:
    colorList.append('green')
  if inputs.find("B") != -1:
    colorList.append('black')
  if inputs.find("R") != -1:
    colorList.append('red')
  if inputs.find("U") != -1:
    colorList.append('blue')

def printToSet(formatted):
  name = formatted.name
  print(name)
  oracleText = formatted.oracle_text.replace("\n", "\n\t\t").replace('{', "").replace('}', "")
  _castingCost = formatted.mana_cost.replace('{', "").replace('}', "")
  castingCost = '\n\tcasting cost: {_castingCost}'.format(_castingCost=_castingCost) if _castingCost != '' else ''

  _flavorText = formatted.flavor_text.replace("\n", "\n\t\t") if hasattr(formatted, 'flavor_text') else ''
  flavorText = "\n\tflavor text:\n\t\t<i-flavor>{_flavorText}</i-flavor>".format(_flavorText=_flavorText) if _flavorText != '' else ''
  splitType = formatted.type_line.split("  ")

  land = ''
  isLand = False
  artifact = ''
  superType = splitType[0]
  if superType.find('Land') != -1:
    land = 'land'
    isLand = True
  if superType.find('Artifact') != -1:
    artifact = 'artifact'
  
  _subType = splitType[1] if len(splitType) == 2 else ''
  subType = "\n\tsub type: <word-list-race>{_subType}</word-list-race>".format(_subType=_subType) if _subType != '' else ''

  _toughness = formatted.toughness if hasattr(formatted, 'toughness') else ''
  toughness = "\n\ttoughness: {_toughness}".format(_toughness=_toughness) if _toughness != '' else ''

  _power = formatted.power if hasattr(formatted, 'power') else ''
  power = "\n\tpower: {_power}".format(_power=_power) if _power != '' else ''

  artist = formatted.artist.encode('ASCII', "ignore").decode() if hasattr(formatted, 'artist') else ''

  producedMana = ''.join([str(elem) for elem in formatted.produced_mana])  if hasattr(formatted, 'produced_mana') else ''
  hybrid = ''
  colorsList = []
  producedColorsList = []
  getColors(castingCost, colorsList)
  if isLand:
    getColors(producedMana, producedColorsList)
    if len(producedColorsList) > 0:
      hybrid = ', horizontal'
      land = 'land, '
  if len(colorsList) > 1: 
    hybrid = ', hybrid, horizontal'
  colors = ', '.join(map(str, producedColorsList if isLand else colorsList))
  endCode = '\n' if name != cards[len(cards)-1] else ''
  f.write(
"""card:
\thas styling: false
	notes: 
	time created: 2021-03-21 11:55:34
	time modified: 2021-03-21 13:03:52
	border color: rgb(255,255,255)
	card color: {land}{artifact}{colors}{hybrid}
	name: {name}{castingCost}
	image:
	super type: <word-list-type>{superType}</word-list-type>{subType}
	rule text:
\t\t{oracleText}{flavorText}{power}{toughness}
	illustrator: Illus. {artist}
	copyright: PROXY: Not for sale or use in organized play
	image 2: 
	copyright 2: 
	copyright 3: 
	mainframe image: 
	mainframe image 2:{endCode}""".format(land=land,artifact=artifact,hybrid=hybrid,castingCost=castingCost,artist=artist,toughness=toughness,power=power,flavorText=flavorText,oracleText=oracleText,subType=subType,superType=superType,name=name,colors=colors,endCode=endCode))

cards = input.split("\n")
f= open("set","w+")
initialWrite = """mse version: 0.3.8
game: magic
stylesheet: oldBig
set info:
	symbol: symbol1.mse-symbol
	masterpiece symbol: 
	border color: rgb(255,255,255)
	automatic card numbers: no
	automatic copyright: no
styling:
	magic-oldBig:
		text box mana symbols: magic-mana-small.mse-symbol-font
		alpha style blending: no
		type of gradient multicolor: full card
		type of gradient artifact: full card
		center text: short text only
		colored rarities: yes
		overlay: 
		pt font: MPlantin-Bold
		inverted common symbol: no\n"""
f.write(initialWrite)

for card in cards:
  url = "https://api.scryfall.com/cards/named?exact={card}".format(card=card)
  response = requests.get(url)
  text = response.text.replace('\u2014', "").replace('\u2022', "").replace('\u2212', "-")
  formatted = json.loads(text, object_hook=lambda d: SimpleNamespace(**d))
  if  hasattr(formatted, 'card_faces'):
    printToSet(formatted.card_faces[0])
    printToSet(formatted.card_faces[1])
  else:
    printToSet(formatted)
  time.sleep(0.01) # Be nice to scryfall

finalWrite = """
version control:
	type: none
apprentice code:"""

f.write(finalWrite)
