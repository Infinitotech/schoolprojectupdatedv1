/**
 * Created by Arslan on 2/24/2017.
 */


function addQuestion(){
    alert('load')
    $.ajax({
        url : 'test/addQuestion',
        type : 'GET'
    });
}