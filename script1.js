var post= 
    document.getElementById("submit");

post.addEventListener("submit",
function(){
    var commentBoxValue=
        document.getElementById("comment").value;
    
    var li= 
        document.createElement("li");
    
    var text = 
        document.createTextNode(commentBoxValue);
    
    li.appendChild(text);
    
    document.getElementById("unordered").appendChild(li)
});



// let add = () => {
//     let name = document.querySelector('.container1 #name'); 
//     let comment = document.querySelector('.container1 #comment'); 
     
//     if (name.value !== "" && comment.value != "") { 
     
//     let list = document.querySelector('.list'); 
//     let time = new Date();
//     let h = time.getHours(); 
//     let m = time.getMinutes(); 
//     let s = time.getSeconds(); 
//     let now = h + " : " + m + " : " + s;
//     let list_item = document.createElement ("l1"); 
     
//     list_item.innerHTML = `
//     <span>
//     <p>${name.value} ${now}</p> 
//     </span>
//     <p>${comment.value}</p>
//     `;
//     list.append(list_item); 
//     }
     
//     if (name.value == "" || comment.value == "") {
//     let list = document.querySelector('.list'); 
//     let list_item = document.createElement ("l2"); 
//     var warn = 'Please enter name & comment!';  
//     list_item.innerHTML = `
//     <span>
//     <p>${warn}</p> 
//     </span>
//     `;
//     list.append(list_item); 
//      }
//     name.value=comment.value = "";
//     }
    