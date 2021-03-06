import fdb
import diabloapi as da

Tables = {
    "Profile": "Profile ("
                             "battleTag VARCHAR(50) NOT NULL PRIMARY KEY, "
                             "guildName VARCHAR(50), "
                             "paragonLevel INT, "
                             "paragonLevelHardcore INT, "
                             "paragonLevelSeason INT, "
                             "paragonLevelSeasonHardcore INT)",
    "Artisans": "Artisans ("
                              "battleTag VARCHAR(50) NOT NULL PRIMARY KEY, "
                              "blacksmith INT, "
                              "jeweler INT, "
                              "mystic INT, "
                              "blacksmithSeason INT, "
                              "jewelerSeason INT, "
                              "mysticSeason INT, "
                              "blacksmithHardcore INT, "
                              "jewelerHardcore INT, "
                              "mystiCHARdcore INT, "
                              "blacksmithSeasonHardcore INT, "
                              "jewelerSeasonHardcore INT, "
                              "mysticSeasonHardcore INT, "
                              "FOREIGN KEY(battleTag) REFERENCES Profile(battleTag))",
    "Hero": "Hero ("
                              "idHero INT NOT NULL PRIMARY KEY, "
                              "battleTag VARCHAR(50), "
                              "heroName VARCHAR(50), "
                              "heroClass VARCHAR(50), "
                              "gender char(1), "
                              "level INT, "
                              "kills_of_elite INT, "
                              "hardcore BOOLEAN, "
                              "Seasonal BOOLEAN, "
                              "dead BOOLEAN, "
                              "last_update INT, "
                              "FOREIGN KEY(battleTag) REFERENCES Profile(battleTag))",
    "Item": "Item ("
                              "idItem VARCHAR(50) NOT NULL PRIMARY KEY, "
                              "nameItem VARCHAR(50), "
                              "requiredLevel INT, "
                              "accountBound BOOLEAN, "
                              "flavorText VARCHAR(256), "
                              "typeName VARCHAR(50), "
                              "isSeasonRequiredToDrop BOOLEAN, "
                              "SeasonRequiredToDrop BOOLEAN)",
    "HeroItems": "HeroItems ("
                               "idHero INT NOT NULL PRIMARY KEY, "
                               "nameItem VARCHAR(50), "
                               "idItem VARCHAR(50), "
                               "Slot VARCHAR(50), "
                               "FOREIGN KEY(idHero) REFERENCES Hero(idHero), "
                               "FOREIGN KEY (IDITEM) REFERENCES ITEM (IDITEM))",
    "ItemStats": "ItemStats ("
                               "idItem VARCHAR(50) NOT NULL PRIMARY KEY, "
                               "armor INT, "
                               "attacksPerSecond INT, "
                               "minDamage INT, "
                               "maxDamage INT, "
                               "FOREIGN KEY(idItem) REFERENCES Item(idItem))",
    "Skill": "Skill ("
                               "slugSkill VARCHAR(50) NOT NULL PRIMARY KEY, "
                               "nameSkill VARCHAR(50), "
                               "level INT, "
                               "description VARCHAR(50), "
                               "active BOOLEAN, "
                               "pasive BOOLEAN, "
                               "classHero VARCHAR(50))",
    "HeroSkills": "HeroSkills ("
                               "idHero INT NOT NULL PRIMARY KEY, "
                               "nameSkill VARCHAR(50), "
                               "slugSkill VARCHAR(50), "
                               "FOREIGN KEY(idHero) REFERENCES Hero(idHero), "
                               "FOREIGN KEY(slugSkill) REFERENCES Skill(slugSkill))",
    "Runes": "Runes ("
                               "slug VARCHAR(50) NOT NULL PRIMARY KEY, "
                               "slugSkill VARCHAR(50), "
                               "name VARCHAR(50), "
                               "level INT, "
                               "description VARCHAR(50), "
                               "active BOOLEAN, "
                               "FOREIGN KEY(slugSkill) REFERENCES Skill(slugSkill))",
    "Era": "Era ("
                               "idEra INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY, "
                               "era_start_date INT, "
                               "isCurrent BOOLEAN)",
    "EraLeaderboardClass": "EraLeaderboardClass ("
                               "class VARCHAR(50) NOT NULL PRIMARY KEY, "
                               "idEra INT, "
                               "FOREIGN KEY(idEra) REFERENCES Era(idEra))",
    "EraLeaderboard": "EraLeaderboard ("
                              "rank INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY, "
                              "battleTag VARCHAR(50), "
                              "guildName VARCHAR(50), "
                              "heroClass VARCHAR(50), "
                              "idHero INT, "
                              "paragonLevel INT, "
                              "riftLevel INT, "
                              "riftTime INT, "
                              "completedTime INT, "
                              "FOREIGN KEY(heroClass) REFERENCES EraLeaderboardClass(class))",
    "Season": "Season ("
                              "idSeason INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY, "
                              "isCurrent BOOLEAN)",
    "SeasonLeaderboardClass": "SeasonLeaderboardClass ("
                              "class VARCHAR(50) NOT NULL PRIMARY KEY, "
                              "idSeason INT, "
                              "FOREIGN KEY(idSeason) REFERENCES Season(idSeason))",
    "SeasonLeaderboard": "SeasonLeaderboard ("
                              "rank INT GENERATED BY DEFAULT AS IDENTITY PRIMARY KEY, "
                              "battleTag VARCHAR(50), "
                              "guildName VARCHAR(50), "
                              "heroClass VARCHAR(50), "
                              "idHero INT, "
                              "paragonLevel INT, "
                              "riftLevel INT, "
                              "riftTime INT, "
                              "completedTime INT, "
                              "FOREIGN KEY(heroClass) REFERENCES SeasonLeaderboardClass(class))"
}


def main():
    con = fdb.create_database(dsn='U:/DiabloDataBase/diablodb.fdb', user='SYSDBA')
    cur = con.cursor()
    for key in Tables:
        cur.execute("CREATE TABLE {}".format(Tables[key]))
    con.commit()


if __name__ == "__main__":
    main()