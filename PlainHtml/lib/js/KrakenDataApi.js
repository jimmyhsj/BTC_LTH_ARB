var apigClient = apigClientFactory.newClient({
    apiKey: 'VeECFhYrz2QO8xUBjiyn4svT8aLc32b5vK4N2lWc'
});

function KrakenLoadData() {
    var index_data = {};
    var params = {};
    var body = {};
    var additionalParams = {
    };

    apigClient.krakenApiGet(params, body, additionalParams)
        .then(function (result) {
            console.log(result.data);
            index_data = result.data;

            $("#btc_spot_kraken").text(index_data.spot.XXBTZUSD_spot).toggle("highlight").toggle("highlight");
            $("#lth_spot_kraken").text(index_data.spot.XLTCZUSD_spot).toggle("highlight").toggle("highlight");
            $("#usdt_spot_kraken").text(index_data.spot.USDTZUSD_spot).toggle("highlight").toggle("highlight");

            $("#kraken_USDT_postion").text(index_data.return_position.balance.USDT).toggle("highlight").toggle("highlight");
            $("#kraken_XXBT_position").text(index_data.return_position.balance.XXBT).toggle("highlight").toggle("highlight");
            $("#kraken_XLTC_position").text(index_data.return_position.balance.XLTC).toggle("highlight").toggle("highlight");
            $("#kraken_ZUSD_position").text(index_data.return_position.balance.ZUSD).toggle("highlight").toggle("highlight");

            return result;
        }).catch(function (result) {
        console.log(result);
    });
}



function precisionRound(number, precision) {
    var factor = Math.pow(10, precision);
    return Math.round(number * factor) / factor;
}