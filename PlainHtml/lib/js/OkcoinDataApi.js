var apigClient = apigClientFactory.newClient({
    apiKey: 'VeECFhYrz2QO8xUBjiyn4svT8aLc32b5vK4N2lWc'
});
function OkCoinLoadData() {
    var index_data = {};

    var params = {};

    var body = {};
    var additionalParams = {
        // headers: {
        //     "Access-Control-Allow-Origin": "*",
        //     "Access-Control-Allow-Credentials": true
        // }
    };
    apigClient.btcLthIndexGet(params, body, additionalParams)
        .then(function (result) {

            index_data = result;

            index_data.data.Last_Basis_ThisWeek_BTC = precisionRound((index_data.data.Fut_Data_This_Week_BTC / index_data.data.BTC_Spot_OKCoin - 1) * 100, 2) + '%';
            index_data.data.Last_Basis_ThisWeek_LTC = precisionRound((index_data.data.Fut_Data_This_Week_LTC / index_data.data.LTC_Spot_OKCoin - 1) * 100, 2) + '%';
            index_data.data.Last_Basis_ThisWeek_BCH = precisionRound((index_data.data.Fut_Data_This_Week_BCH / index_data.data.BCH_Spot_OKCoin - 1) * 100, 2) + '%';

            index_data.data.Last_Basis_1Week_BTC = precisionRound((index_data.data.Fut_Data_Next_Week_BTC / index_data.data.BTC_Spot_OKCoin - 1) * 100, 2) + '%';
            index_data.data.Last_Basis_1Week_LTC = precisionRound((index_data.data.Fut_Data_Next_Week_LTC / index_data.data.LTC_Spot_OKCoin - 1) * 100, 2) + '%';
            index_data.data.Last_Basis_1Week_BCH = precisionRound((index_data.data.Fut_Data_Next_Week_BCH / index_data.data.BCH_Spot_OKCoin - 1) * 100, 2) + '%';
            
            index_data.data.Last_Basis_Quarter_BTC = precisionRound((index_data.data.Fut_Data_Next_Quarter_BTC / index_data.data.BTC_Spot_OKCoin - 1) * 100, 2) + '%';
            index_data.data.Last_Basis_Quarter_LTC = precisionRound((index_data.data.Fut_Data_Next_Quarter_LTC / index_data.data.LTC_Spot_OKCoin - 1) * 100, 2) + '%';
            index_data.data.Last_Basis_Quarter_BCH = precisionRound((index_data.data.Fut_Data_Next_Quarter_BCH / index_data.data.BCH_Spot_OKCoin - 1) * 100, 2) + '%';


            
            // $("#btc_index").text(index_data.data.BTC_Index).toggle("highlight").toggle("highlight");
            // $("#lth_index").text(index_data.data.LTC_Index).toggle("highlight").toggle("highlight");
            // // $("#btc_spot_okcoin").text(index_data.data.BTC_Spot_OKCoin).toggle("highlight").toggle("highlight");
            // $("#lth_spot_okcoin").text(index_data.data.LTC_Spot_OKCoin).toggle("highlight").toggle("highlight");

            // $("#btc_basic_quater").text(index_data.data.Last_Basis_Quarter_BTC).toggle("highlight").toggle("highlight");
            // $("#ltc_basic_quater").text(index_data.data.Last_Basis_Quarter_LTC).toggle("highlight").toggle("highlight");

            // $("#btc_basic_thisWeek").text(index_data.data.Last_Basis_ThisWeek_BTC).toggle("highlight").toggle("highlight");
            // $("#ltc_basic_thisWeek").text(index_data.data.Last_Basis_ThisWeek_LTC).toggle("highlight").toggle("highlight");

            // $("#btc_basic_1Week").text(index_data.data.Last_Basis_1Week_BTC).toggle("highlight").toggle("highlight");
            // $("#ltc_basic_1Week").text(index_data.data.Last_Basis_1Week_LTC).toggle("highlight").toggle("highlight");

            // $("#btc_fut_thisweek").text(index_data.data.Fut_Data_This_Week_BTC).toggle("highlight").toggle("highlight");
            // $("#btc_fut_1w").text(index_data.data.Fut_Data_Next_Week_BTC).toggle("highlight").toggle("highlight");
            // $("#btc_fut_1q").text(index_data.data.Fut_Next_Quarter_BTC).toggle("highlight").toggle("highlight");

            // $("#lth_fut_thisweek").text(index_data.data.Fut_Data_This_Week_LTC).toggle("highlight").toggle("highlight");
            // $("#lth_fut_1w").text(index_data.data.Fut_Data_Next_Week_LTC).toggle("highlight").toggle("highlight");
            // $("#lth_fut_1q").text(index_data.data.Fut_Next_Quarter_LTC).toggle("highlight").toggle("highlight");

            $("#btc_index").text(index_data.data.BTC_Index);
            $("#lth_index").text(index_data.data.LTC_Index);
            $("#bch_index").text(index_data.data.BCH_Index);

            $("#btc_spot_okcoin").text(index_data.data.BTC_Spot_OKCoin);
            $("#lth_spot_okcoin").text(index_data.data.LTC_Spot_OKCoin);
            $("#bch_spot_okcoin").text(index_data.data.BCH_Spot_OKCoin);

            $("#btc_basic_quater").text(index_data.data.Last_Basis_Quarter_BTC);
            $("#ltc_basic_quater").text(index_data.data.Last_Basis_Quarter_LTC);
            $("#bch_basic_quater").text(index_data.data.Last_Basis_Quarter_BCH);

            $("#btc_basic_thisWeek").text(index_data.data.Last_Basis_ThisWeek_BTC);
            $("#ltc_basic_thisWeek").text(index_data.data.Last_Basis_ThisWeek_LTC);
            $("#bch_basic_thisWeek").text(index_data.data.Last_Basis_ThisWeek_BCH);

            $("#btc_basic_1Week").text(index_data.data.Last_Basis_1Week_BTC);
            $("#ltc_basic_1Week").text(index_data.data.Last_Basis_1Week_LTC);
            $("#bch_basic_1Week").text(index_data.data.Last_Basis_1Week_BCH);

            $("#btc_fut_thisweek").text(index_data.data.Fut_Data_This_Week_BTC);
            $("#btc_fut_1w").text(index_data.data.Fut_Data_Next_Week_BTC);
            $("#btc_fut_1q").text(index_data.data.Fut_Data_Next_Quarter_BTC);

            $("#lth_fut_thisweek").text(index_data.data.Fut_Data_This_Week_LTC);
            $("#lth_fut_1w").text(index_data.data.Fut_Data_Next_Week_LTC);
            $("#lth_fut_1q").text(index_data.data.Fut_Data_Next_Quarter_LTC);

            $("#bch_fut_thisweek").text(index_data.data.Fut_Data_This_Week_BCH);
            $("#bch_fut_1w").text(index_data.data.Fut_Data_Next_Week_BCH);
            $("#bch_fut_1q").text(index_data.data.Fut_Data_Next_Quarter_BCH);

            $("[id^=btc]").toggle("highlight").toggle("highlight");
            $("[id^=lth]").toggle("highlight").toggle("highlight");
            $("[id^=bch]").toggle("highlight").toggle("highlight");

            // return result;
            console.log(result);

        }).catch(function (result) {
        console.log(result);
    });
}

function precisionRound(number, precision) {
    var factor = Math.pow(10, precision);
    return Math.round(number * factor) / factor;
}