var submitSearch = function(){
	var dept = $("#enter_dept").val()
	console.log(dept)
	var nugget = $("#enter_nugget").val()
	var input = [dept, nugget]

	$.ajax({
		type: "POST",
		url: "search_item",
		datatype: "json",
		contentType: "application/json; charset=utf-8",
		data : JSON.stringify(input),
        success: function(result){
            var all_data = result["data"]
            console.log(all_data)
           	//display_list(all_data)
            
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }

	})
}



var display_list = function(item_to_display){ 
	console.log(item_to_display.length)
	$(".experiences").empty()
	$.each(item_to_display, function(i, item){
		var li = $("<li class='click'>")
		var id = item["Id"]
		var name = item["Name"]
		var photo = item["Photo"]

		var link = "<h3 class='where'>"+name+"</h3>"
		$(li).append(link)

		var year = item["SchoolYear"]
		$(li).append("<h3 class='what pink'> "+year+" </h3> ")
		var major = item["Major"]
		$(li).append("<h3 class='what pink'> "+major+" </h3> ")
		
		var photolink = "<img class='description' src= "+photo+" width='100'>"
		$(li).append(photolink)

		var comp = item["Company"]
		$(li).append("<p class='description'> "+comp+" </p> ")

		var email = item["Email"]
		$(li).append("<p class='description'> "+email+" </p> ")


		$(".experiences").append(li)
		

	})
}


$(document).ready(function(){
      $("#submit_search").click(function(){
      	   console.log("hi")
           submitSearch()
      })
      $("#enter_search").keypress(function(e){
            if(e.which == 13){
                  submitSearch()
            }
      })
});
