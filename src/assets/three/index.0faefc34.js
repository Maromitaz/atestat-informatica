import{S as L,G as x,P,W as v,a as o,O,A,b as G}from"./vendor.076b62ae.js";const R=function(){const l=document.createElement("link").relList;if(l&&l.supports&&l.supports("modulepreload"))return;for(const e of document.querySelectorAll('link[rel="modulepreload"]'))d(e);new MutationObserver(e=>{for(const t of e)if(t.type==="childList")for(const c of t.addedNodes)c.tagName==="LINK"&&c.rel==="modulepreload"&&d(c)}).observe(document,{childList:!0,subtree:!0});function b(e){const t={};return e.integrity&&(t.integrity=e.integrity),e.referrerpolicy&&(t.referrerPolicy=e.referrerpolicy),e.crossorigin==="use-credentials"?t.credentials="include":e.crossorigin==="anonymous"?t.credentials="omit":t.credentials="same-origin",t}function d(e){if(e.ep)return;e.ep=!0;const t=b(e);fetch(e.href,t)}};R();const s=new L,S=new x,r=new P(75,5/3,.1,1e3),a=new v({canvas:document.querySelector("#bg")}),u=new o(16755370,2,1e5),p=new o(16755370,.5,1e5),m=new o(16755370,.5,1e5),w=new o(16755370,.5,1e5),g=new o(16755370,.5,1e5),h=new o(16755370,.5,1e5),i=new O(r,a.domElement),H=new A(16777215,2);a.setPixelRatio(window.devicePixelRatio);a.setSize(bg.scrollWidth,bg.scrollHeight);u.position.set(0,10,0);p.position.set(10,0,0);m.position.set(0,0,10);w.position.set(10,0,10);g.position.set(-10,0,0);h.position.set(0,0,-10);const W=new G(40,20);s.add(u,p,m,w,g,h,H,W);a.render(s,r);i.enableZoom=!1;i.enableRotate=!1;i.enablePan=!1;r.position.set(0,4,7);r.rotateX=35;let f;S.load(model,function(n){f=n.scene,s.add(n.scene),n.asset,f.rotation.y=.7},function(n){console.log(n.loaded/n.total*100+"% loaded")},function(n){console.log(`An error happened
`+n)});function y(){requestAnimationFrame(y),i.autoRotate=!0,i.update(),a.render(s,r)}y();