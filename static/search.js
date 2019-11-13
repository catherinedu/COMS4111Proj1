var submitSearch = function(){
	var dept = $("#enter_dept").val()
	//console.log(dept)
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
           	display_list(all_data)
            
        },
        error: function(request, status, error){
            console.log("Error");
            console.log(request)
            console.log(status)
            console.log(error)
        }

	})
}

var submitSearchProf = function(){
	var prof_name = $("#enter_prof").val()
	var arr = prof_name.split(", ")
	var first_name = arr[1]
	var last_name = arr[0]
	var input = [last_name, first_name]

	$.ajax({
		type: "POST",
		url: "search_item_prof",
		datatype: "json",
		contentType: "application/json; charset=utf-8",
		data : JSON.stringify(input),
        success: function(result){
            var all_data = result["data"]
            console.log(all_data)
           	display_list(all_data)
            
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
	console.log("hi")
	$(".experiences").empty()
	$.each(item_to_display, function(i, item){
		var li = $("<li class='click'>")
		var last_name = item["last_name"]
		var first_name = item["first_name"]
		var name = last_name+ ", " + first_name
		var dept_name = item['department']
		var course_name = item["course_name"]
		var p_review = item["p_review"]
		var r_review = item["r_review"]

		var link = "<h3 class='where'>"+name+"</h3>"
		$(li).append(link)

		$(li).append("<h3 class='what pink'> "+dept_name+" </h3> ")
	
		$(li).append("<h3 class='what pink'> "+course_name+" </h3> ")

		$(li).append("<h3 class='description'> "+p_review+" </h3> ")
		$(li).append("<h3 class='description'> "+r_review+" </h3> ")
		$(".experiences").append(li)	

	})
}


$(document).ready(function(){
      $("#submit_search").click(function(){
           submitSearch()
      })
      $("#submit_search_prof").click(function(){
           submitSearchProf()
      })
});
