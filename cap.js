window.onload=function(){
    choosePic();
    drawingBoard();
    }

var imagesArray = ["1.png","2.png","3.png","4.png","5.png"];
var imageBoard;

function randomNum()
{
    var rando = Math.floor(Math.random() * 5);

    return rando;
}

function drawingBoard(){
   imageBoard = new DrawingBoard.Board('board', {
        color: '#000',
        size: 10,
        controls: [
            { Navigation: { back: true, forward: true } },
        ],
        webStorage: 'local'
    });
}



function choosePic() {
    document.getElementById("refimg").src = imagesArray[randomNum()];
}


function checkPic(){
    $("#check").click(function(){
        domtoimage.toBlob(document.getElementById('board'))
        .then(function (blob) {
            const reader= new FileReader();
            //window.saveAs(blob, 'picture.png');
            reader.addEventListener("load",() => {
                localStorage.setItem("recent-image", reader.result);
            })
           
        });
    })
}
