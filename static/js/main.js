document.addEventListener("DOMContentLoaded", function() {
    checkNotesEmpty();
});


function checkNotesEmpty(){
  const yourNotesBtn = document.getElementById("your-notes-btn");
  yourNotes = yourNotesBtn.dataset.notes;
  if (yourNotes.length < 3) {
    yourNotesBtn.disabled = true;
  } else {
    yourNotesBtn.disabled = false;
  }
}
