function openModal(id) {
  $(`#${id}-editModal`).css({
    display: "block",
  });
}

function closeModal(id) {
  $(`#${id}-editModal`).css({
    display: "none",
  });
}
