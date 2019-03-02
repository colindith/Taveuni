var intervalId = null;
onmessage = function(event) {
    if ( event.data.start ) {
        intervalId = setInterval(function(){
            postMessage('interval.start');
            console.log('in interval.....')
        },event.data.ms||0);
    }
    if ( event.data.stop && intervalId !== null ) {
        clearInterval(intervalId);
    }
};