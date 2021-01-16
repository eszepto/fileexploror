document.addEventListener("keydown", function(event) {
  if (event.keyCode == 113) {
    //   F2 btn
    Rename();
    alert("F2 was pressed");
  }
});

$(document).ready(function() {
  

  

  $(".ItemTr").click(function() {
      var checkbox = $(this).find("td:first").find("input");
      if (checkbox.is(":checked")) {
        checkbox.attr("checked", false);
        checkbox.closest("tr").css("background-color", "#FFF");
      } else {
        checkbox.attr("checked", true);
        checkbox.closest("tr").css("background-color", "#FC9A01");
      }
      EditButtonBehavior();
    }
    
  );

  $("#SelectAllBox").click(function() {
      var AllselectBox = $(this)
      if (AllselectBox.is(":checked")) {
        $("tr")
          .find("td:first")
          .find("input")
          .attr("checked", true);
        $("#tblDisplay")
          .find("tr:not(#HeaderRow)")
          .each(function() {
            $(this).css("background-color", "#FC9A01");
          });
      } else {
        
        $("tr")
          .find("td:first")
          .find("input")
          .attr("checked", false);
        $("#tblDisplay")
          .find("tr:not(#HeaderRow)")
          .each(function() {
            $(this).css("background-color", "#FFF");
            });
        }
    });
});

function RenameFunc() {
 
}

var hidden = false;
function action() {
  hidden = !hidden;
  if (hidden) {
    document.getElementById("togglee").style.visibility = "hidden";
  } else {
    document.getElementById("togglee").style.visibility = "visible";
  }
}

function EditButtonBehavior()
{
    ItemCheckBoxes = document.getElementsByClassName("checky");
    
    count = 0;
    for (var i = 0; i < ItemCheckBoxes.length; i++) {
      if (ItemCheckBoxes[i].checked) {
        count += 1;
        if (count == 0) {
            $(".rename").hide();
            $(".delete").hide();
          } else if (count == 1) {
            $(".rename").show();
            $(".delete").show();
          } else {
            $(".rename").hide();
            $(".delete").show();
            break;
          }
      }
    }
}

$("#SystemFileCheckBox").click(function(){
    //Hide system file
    if($(this).is(":checked")){
        console.log("aaaa")
        $(".SystemItem").hide();
    }
    else{
        $(".SystemItem").show();
    }
})


function SortByName(){

}
function SortByDate() {  

}
function SortBySize() {  

}