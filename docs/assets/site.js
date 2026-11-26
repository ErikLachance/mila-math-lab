
document.documentElement.classList.add("js");
const lang=new URLSearchParams(location.search).get("lang")==="fr"?"fr":"en";
document.documentElement.lang=lang;
if(lang==="fr"){
 document.querySelectorAll("[data-fr]").forEach(e=>{e.textContent=e.dataset.fr});
 document.querySelectorAll("[data-fr-placeholder]").forEach(e=>e.placeholder=e.dataset.frPlaceholder);
 document.querySelectorAll("a[data-local]").forEach(a=>{const h=a.getAttribute("href");if(h.startsWith("#"))return;const u=new URL(h,location.href);if(u.origin===location.origin){u.searchParams.set("lang","fr");a.href=u.href}});
}
const sw=document.getElementById("language");
if(sw){sw.textContent=lang==="fr"?"English":"Français";sw.addEventListener("click",()=>{const u=new URL(location.href);if(lang==="fr")u.searchParams.delete("lang");else u.searchParams.set("lang","fr");location.href=u.href})}
const search=document.getElementById("search"),field=document.getElementById("field"),type=document.getElementById("type"),count=document.getElementById("count");
if(search&&field&&type&&count){const rows=Array.from(document.querySelectorAll("[data-paper]"));const norm=s=>s.normalize("NFD").replace(/[\u0300-\u036f]/g,"").toLowerCase();
function filter(){let n=0;for(const row of rows){const ok=(!field.value||field.value===row.dataset.field)&&(!type.value||type.value===row.dataset.type)&&norm(row.dataset.search).includes(norm(search.value.trim()));row.hidden=!ok;if(ok)n++}count.textContent=n+(n===1?" note":" notes");document.getElementById("empty").hidden=n!==0}
search.addEventListener("input",filter);field.addEventListener("change",filter);type.addEventListener("change",filter);filter()}
