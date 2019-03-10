var academic_status = document.getElementById("status1");
var hostel_status = document.getElementById("status2");
var regis_done = document.getElementById("status3");

var academic_db;
var hostel_db;
var regis_db;

if(academic_db){
  academic_status.className = "progtrckr-done"
}
if(hostel_db){
  hostel_status.className = "progtrckr-done"
}
if(regis_db){
  regis_done.className = "progtrckr-done"
}




const realFileBtn1 = document.getElementById("real-file1");
const customBtn1 = document.getElementById("custom-button1");
const customTxt1 = document.getElementById("custom-text1");

customBtn1.addEventListener("click", function() {
  realFileBtn1.click();
});


realFileBtn1.addEventListener("change", function() {
  if (realFileBtn1.value) {
    customTxt1.innerHTML = realFileBtn1.value.match(
      /[\/\\]([\w\d\s\.\-\(\)]+)$/
    )[1];
  } else {
    customTxt1.innerHTML = "No file chosen, yet.";
  }
});

const realFileBtn2 = document.getElementById("real-file2");
const customBtn2 = document.getElementById("custom-button2");
const customTxt2 = document.getElementById("custom-text2");

customBtn2.addEventListener("click", function() {
  realFileBtn2.click();
});


realFileBtn2.addEventListener("change", function() {
  if (realFileBtn2.value) {
    customTxt2.innerHTML = realFileBtn2.value.match(
      /[\/\\]([\w\d\s\.\-\(\)]+)$/
    )[2];
  } else {
    customTxt2.innerHTML = "No file chosen, yet.";
  }
});

const realFileBtn3 = document.getElementById("real-file3");
const customBtn3 = document.getElementById("custom-button3");
const customTxt3 = document.getElementById("custom-text3");

customBtn3.addEventListener("click", function() {
  realFileBtn3.click();
});


realFileBtn3.addEventListener("change", function() {
  if (realFileBtn3.value) {
    customTxt3.innerHTML = realFileBtn3.value.match(
      /[\/\\]([\w\d\s\.\-\(\)]+)$/
    )[3];
  } else {
    customTxt3.innerHTML = "No file chosen, yet.";
  }
});






