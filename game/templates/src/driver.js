function tick() {
    let newTime = new Date();
    gameTicksLeft += newTime - curTime;
    // console.log('gameTicksLeft'+gameTicksLeft);
    radarUpdateTime += newTime - curTime;
    curTime = newTime;
    if(stop) {
        addOffline(gameTicksLeft * offlineRatio);
        gameTicksLeft = 0;
        return;
    }
    prevState.stats = JSON.parse(JSON.stringify(stats));

    while (gameTicksLeft > (1000 / 50)) {
        if(gameTicksLeft > 2000) {
            window.fps /= 2;
            console.warn('too fast! (${gameTicksLeft})');
            statGraph.graphObject.options.animation.duration = 0;
            gameTicksLeft = 0;
        }
        if(stop) {
            return;
        }
        timer++;

        // actions.tick();
        // for(let i = 0; i < dungeons.length; i++) {
        //     for(let j = 0; j < dungeons[i].length; j++) {
        //         let level = dungeons[i][j];
        //         if(level.ssChance < 1) {
        //             level.ssChance += .0000001;
        //             if(level.ssChance > 1) {
        //                 level.ssChance = 1;
        //             }
        //         }
        //     }
        // }

        if(shouldRestart || timer >= timeNeeded) {
            prepareRestart();
        }

        if(timer % (300*gameSpeed) === 0) {
            save();
        }
        gameTicksLeft -= (1000 / 50) / gameSpeed / bonusSpeed;
        if(bonusSpeed > 1) {
            addOffline(-1 * gameTicksLeft * ((bonusSpeed - 1)/bonusSpeed));
        }
    }

    if(radarUpdateTime > 1000) {
        view.updateStatGraphNeeded = true;
        radarUpdateTime -= 1000;
    }

    view.update();

}