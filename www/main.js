
$(document).ready(function () {
    
    $('.text').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "bounceIn",
        },
        out: {
            effect: "bounceOut",
        },

    });

    //siriwave
    var siriWave = new SiriWave({
        container: document.getElementById("siri-container"),
        width: 800,
        height: 200,
        style: "ios9",
        amplitude: "1",
        speed: "0.3",
        autostart: true
    });

    //siri message
    $('.siri-message').textillate({
        loop: true,
        sync: true,
        in: {
            effect: "fadeInUp",
            sync: true,
        },
        out: {
            effect: "fadeOutUp",
            sync: true,
        },

    });

    //mic
    $("#MicBtn").click(function () { 

        eel.playAssistantSound()

       $("#Oval").attr("hidden", true);
       $("#Siriwave").attr("hidden", false);
       eel.takecommand()();
        
    });


});
 

