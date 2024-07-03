// ==UserScript==
// @name        Stozu block
// @description A stozu block script
// @version     2
// @author      Noob
// @namespace   Violentmonkey Scripts
// @match       https://dash.stozu.net/earn/adpage
// @grant       none
// @icon        https://raw.githubusercontent.com/Noob-Lol/a/main/idk.png
// ==/UserScript==

(function() {
  'use strict';

  const elementsToBlock = [
    ".alert-primary.mt-4.alert",
    ".elevation-4.sidebar-dark-primary.sidebar-open.main-sidebar",
    ".navbar-light.navbar-dark.navbar-expand.navbar.sticky-top.main-header",
    ".main-footer",
    ".card-body > .row",
    ".swal2-backdrop-show.swal2-top-end.swal2-container",
  ];

  // Loop through all elements on the page
  const allElements = document.querySelectorAll("*");

  // Loop through elements to block and hide them
  elementsToBlock.forEach(selector => {
    const elements = document.querySelectorAll(selector);
    elements.forEach(element => element.style.display = "none");
  });
})();