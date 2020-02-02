window.addEventListener('DOMContentLoaded', function(){

    document.getElementById("btn").addEventListener('click',onclick,false)
    function onclick(){
        socket = new WebSocket('ws://localhost:9001');
    }
    document.getElementById("bot").addEventListener('click',botclick,false)
    function botclick(){
        socket.send($('.current-word').innerText);
    }
}, false);
/*
chrome.runtime.sendMessage({greeting: "hello"}, function(response) {
  console.log(response.farewell);
});*/
