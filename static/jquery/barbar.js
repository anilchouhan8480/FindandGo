
            // $(function () {
            //     GetRatings();
            //     $('.filled-stars').click(function () {
            //         var value = parseInt($(this)[0].style.width.replace('%')) / 20;
            //         $.ajax({
            //             type: "POST",
            //             url: "Default.aspx/Rate",
            //             data: "{rating: " + value + "}",
            //             contentType: "application/json; charset=utf-8",
            //             dataType: "json",
            //             success: function (response) {
            //                 alert("Your rating has been saved.");
            //                 GetRatings();
            //             },
            //             failure: function (response) {
            //                 alert('There was an error.');
            //             }
            //         });
            //     });
            // });
            // function GetRatings() {
            //     $.ajax({
            //         type: "POST",
            //         url: "Default.aspx/GetRating",
            //         data: "{}",
            //         contentType: "application/json; charset=utf-8",
            //         dataType: "json",
            //         success: function (response) {
            //             var result = eval(response.d)[0];
            //             if (result.Average > 0) {
            //                 $('.filled-stars')[0].style.width = result.Average * 20 + "%";
            //                 $("#rating").html("Average Rating: " + result.Average + " Total Rating: " + result.Total);
            //             }
            //             else {
            //                 $('.filled-stars')[0].style.width = "0%";
            //                 $("#rating").html("Average Rating: 0 Total Rating: 0");
            //             }
            //         },
            //         failure: function (response) {
            //             alert('There was an error.');
            //         }
            //     });
            // }

//     function onButtonClick(){
//     document.getElementById('form1').className="show";
// }

