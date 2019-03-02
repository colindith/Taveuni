function save() {
    let toSave = {};
    toSave.dungeons = dungeons;
    toSave.maxTown = maxTown;
    toSave.actionTownNum = actionTownNum;

    let town = towns[0];
    toSave.stats = stats;
    toSave.skills = skills;
    toSave.expWander = town.expWander;
    toSave.expMet = town.expMet;
    toSave.expSecrets = town.expSecrets;
    toSave.totalHeal = town.totalHeal;
    toSave.totalFight = town.totalFight;
    toSave.totalSDungeon = town.totalSDungeon;

    town = towns[1];
    toSave.expForest = town.expForest;
    toSave.expShortcut = town.expShortcut;
    toSave.expHermit = town.expHermit;

    town = towns[2];
    toSave.expCity = town.expCity;
    toSave.expDrunk = town.expDrunk;
    toSave.totalAdvGuild = town.totalAdvGuild;
    toSave.totalCraftGuild = town.totalCraftGuild;
    toSave.totalLDungeon = town.totalLDungeon;
    toSave.version75 = true;
    toSave.expApprentice = town.expApprentice;
    toSave.expMason = town.expMason;
    toSave.expArchitect = town.expArchitect;
    toSave.totalTournament = town.totalTournament;

    for(let i = 0; i < towns.length; i++) {
        town = towns[i];
        for(let j = 0; j < town.totalActionList.length; j++) {
            let action = town.totalActionList[j];
            if (town.varNames.indexOf(action.varName) !== -1) {
                const varName = action.varName;
                toSave["total" + varName] = town["total" + varName];
                toSave["checked" + varName] = town["checked" + varName];
                toSave["good" + varName] = town["good" + varName];
                toSave["goodTemp" + varName] = town["good" + varName];
                if(document.getElementById("searchToggler" + varName)) {
                    toSave["searchToggler"+varName] = document.getElementById("searchToggler" + varName).checked;
                }
            }
        }
    }
    toSave.nextList = actions.next;
    toSave.loadouts = loadouts;
    toSave.repeatLast = document.getElementById("repeatLastAction").checked;
    toSave.pingOnPause = document.getElementById("audioCueToggle").checked;
    toSave.storyShowing = storyShowing;
    toSave.storyMax = storyMax;
    toSave.date = new Date();
    toSave.totalOfflineMs = totalOfflineMs;

    window.localStorage[saveName] = JSON.stringify(toSave);
}