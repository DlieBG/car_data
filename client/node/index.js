var OBDReader = require('obd2-over-serial');
var options = {};
options.baudRate = 115200;
var serialOBDReader = new OBDReader("/dev/ttyUSB0", options);
var dataReceivedMarker = {};

serialOBDReader.on('dataReceived', function (data) {
    console.log(data);
    dataReceivedMarker = data;
});

serialOBDReader.on('connected', function (data) {
    this.addPoller("vss");
    this.addPoller("rpm");
    this.addPoller("temp");
    this.addPoller("load_pct");
    this.addPoller("map");
    this.addPoller("frp");

    this.startPolling(2000); //Polls all added pollers each 2000 ms.
});

serialOBDReader.connect();