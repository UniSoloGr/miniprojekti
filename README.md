# miniprojekti

OKD-kluster:
https://route-ohjelmistotuotanto-lahiopetus-2026-19.ext.okd-cs-test-0.k8s.cs.helsinki.fi/

## Backlogit

Product Backlog:
https://github.com/users/UniSoloGr/projects/2/views/8

Sprint Backlog:
https://github.com/users/UniSoloGr/projects/2/views/9

# DoD

## Lähtökohta

- User storyille tulee määritellä hyväksymiskriteerit, jotka dokumentoidaan sprintistä 2 alkaen Robot Frameworkin syntaksilla
    - hyvänä käytäntönä on laittaa README:stä linkki hyväksymiskriteerit määritteleviin tiedostoihin
- Toteutetun koodin testikattavuuden tulee olla kohtuullinen
- Asiakas pääsee näkemään koko ajan koodin ja testien tilanteen CI-palvelusta
- Koodin ylläpidettävyyden tulee olla mahdollisimman hyvä
    - järkevä nimeäminen
    - järkevä/selkeä ja perusteltu arkkitehtuuri
    - yhtenäinen koodityyli (valvotaan Pylintin avulla)
- Story on valmis vasta, kun se toimii OKD-klusterilla olevassa sovelluksen versiossa

## Tekninen toteutus

- Tietokanta
  - Selkeä tiedonjako

## Käyttäjäliittymä

- Käyttäjällä on pääsy lomakkeeseen, josta löytyvät kaikki relevantit syöttöparametrit riippuen lisättävästä lähdetyypistä.
- Käyttäjä näkee lisäämänsä lähteitä listana
- Käyttäjä voi hakea lisäämiensä lähteitä eri parametrien perusteella
- Lähteiden lisäys, muokkaus ja poistaminen onnistuvat vaivattomasti