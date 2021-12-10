
$(function()
{
    
$("#delete").click(function(){
    $.ajax({
        type: "POST",
        url:'http://127.0.0.1:3000/delete_paciente/4',
        success: function(){
            alert("Hello! I am an alert box!!");
        }
    })
})
}
)