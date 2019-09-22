//[[mw:Snippets/Autoedit]]
function getParamValue(e){var t=RegExp("[&?]"+e+"=([^&]*)");var n=document.location;var r;if(r=t.exec(n)){try{return decodeURI(r[1])}catch(i){}}return null}function substitute(e,t){var n=RegExp(t.from,t.flags);return e.replace(n,t.to)}function execCmds(e,t){for(var n=0;n<t.length;++n){e=t[n].action(e,t[n])}return e}function parseCmd(e){if(!e.length)return[];var t=false;switch(e.charAt(0)){case"s":t=parseSubstitute(e);break;case"j":t=parseJavascript(e);break;default:return false}if(t)return[t].concat(parseCmd(t.remainder));return false}function unEscape(e,t){return e.split("\\\\").join("\\").split("\\"+t).join(t).split("\\n").join("\n")}function runJavascript(data,argWrapper){return eval(argWrapper.code)}function parseJavascript(e){var t,n,r;if(e.length<3)return false;var i=e.charAt(1);e=e.substring(2);t=skipOver(e,i);if(t){n=t.segment.split("\n").join("\\n");e=t.remainder}else return false;r="";if(e.length){t=skipOver(e,";")||skipToEnd(e,";");if(t){r=t.segment;e=t.remainder}}return{action:runJavascript,code:n,flags:r,remainder:e}}function parseSubstitute(e){var t,n,r,i;if(e.length<4)return false;var s=e.charAt(1);e=e.substring(2);i=skipOver(e,s);if(i){t=i.segment;e=i.remainder}else return false;i=skipOver(e,s);if(i){n=i.segment;e=i.remainder}else return false;r="";if(e.length){i=skipOver(e,";")||skipToEnd(e,";");if(i){r=i.segment;e=i.remainder}}return{action:substitute,from:t,to:n,flags:r,remainder:e}}function skipOver(e,t){var n=findNext(e,t);if(n<0)return false;var r=unEscape(e.substring(0,n),t);return{segment:r,remainder:e.substring(n+1)}}function skipToEnd(e,t){return{segment:e,remainder:""}}function findNext(e,t){for(var n=0;n<e.length;++n){if(e.charAt(n)=="\\")n+=2;if(e.charAt(n)==t)return n}return-1}function runOnLoad(e){if(window.addEventListener){window.addEventListener("load",e,false)}else if(window.attachEvent){window.attachEvent("onload",e)}else{window._old_popup_autoedit_onload=window.onload;window.onload=function(){window._old_popup_autoedit_onload();e()}}}window.autoEdit=function(){if(window.autoEdit.alreadyRan)return false;window.autoEdit.alreadyRan=true;var e=getParamValue("autoedit");if(e){try{var t=document.editform.wpTextbox1}catch(n){return}var r=parseCmd(e);var i=t.value;var s=execCmds(i,r);t.value=s;if(typeof wikEdUseWikEd!="undefined"){if(wikEdUseWikEd==true){WikEdUpdateFrame()}}}var o=getParamValue("autosummary");if(o)document.editform.wpSummary.value=o;var u=getParamValue("autominor");if(u){switch(u){case"1":case"yes":case"true":document.editform.wpMinoredit.checked=true;break;case"0":case"no":case"false":document.editform.wpMinoredit.checked=false}}var a=getParamValue("autowatch");if(a){switch(a){case"1":case"yes":case"true":document.editform.wpWatchthis.checked=true;break;case"0":case"no":case"false":document.editform.wpWatchthis.checked=false}}var f=getParamValue("autoclick");if(f){if(document.editform&&document.editform[f]){var l=document.getElementsByTagName("h1");if(l){var c=document.createElement("div");var h=document.editform[f];c.innerHTML='<font size=small><b>"'+h.value+'" تلقائيا.</b></font>';document.title="("+document.title+")";l[0].parentNode.insertBefore(c,l[0]);h.click()}}else{alert('autoedit.js\n\nautoclick: could not find button "'+f+'".')}}};runOnLoad(autoEdit)