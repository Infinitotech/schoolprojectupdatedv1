(function(){var l,n=this;function p(a){return void 0!==a}
function q(a,b,c){a=a.split(".");c=c||n;a[0]in c||!c.execScript||c.execScript("var "+a[0]);for(var d;a.length&&(d=a.shift());)!a.length&&p(b)?c[d]=b:c[d]?c=c[d]:c=c[d]={}}
function r(a,b){for(var c=a.split("."),d=b||n,e;e=c.shift();)if(null!=d[e])d=d[e];else return null;return d}
function aa(){}
function ba(a){a.va=void 0;a.getInstance=function(){return a.va?a.va:a.va=new a}}
function ca(a){var b=typeof a;if("object"==b)if(a){if(a instanceof Array)return"array";if(a instanceof Object)return b;var c=Object.prototype.toString.call(a);if("[object Window]"==c)return"object";if("[object Array]"==c||"number"==typeof a.length&&"undefined"!=typeof a.splice&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("splice"))return"array";if("[object Function]"==c||"undefined"!=typeof a.call&&"undefined"!=typeof a.propertyIsEnumerable&&!a.propertyIsEnumerable("call"))return"function"}else return"null";
else if("function"==b&&"undefined"==typeof a.call)return"object";return b}
function da(a){return"array"==ca(a)}
function ea(a){var b=ca(a);return"array"==b||"object"==b&&"number"==typeof a.length}
function t(a){return"string"==typeof a}
function fa(a){return"function"==ca(a)}
function ga(a){var b=typeof a;return"object"==b&&null!=a||"function"==b}
function ia(a){return a[ja]||(a[ja]=++ka)}
var ja="closure_uid_"+(1E9*Math.random()>>>0),ka=0;function la(a,b,c){return a.call.apply(a.bind,arguments)}
function ma(a,b,c){if(!a)throw Error();if(2<arguments.length){var d=Array.prototype.slice.call(arguments,2);return function(){var c=Array.prototype.slice.call(arguments);Array.prototype.unshift.apply(c,d);return a.apply(b,c)}}return function(){return a.apply(b,arguments)}}
function v(a,b,c){v=Function.prototype.bind&&-1!=Function.prototype.bind.toString().indexOf("native code")?la:ma;return v.apply(null,arguments)}
function na(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var b=c.slice();b.push.apply(b,arguments);return a.apply(this,b)}}
function oa(a,b){for(var c in b)a[c]=b[c]}
var w=Date.now||function(){return+new Date};
function x(a,b){function c(){}
c.prototype=b.prototype;a.B=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.ec=function(a,c,f){for(var d=Array(arguments.length-2),e=2;e<arguments.length;e++)d[e-2]=arguments[e];return b.prototype[c].apply(a,d)}}
;function pa(a,b,c){this.i=c;this.f=a;this.j=b;this.g=0;this.b=null}
pa.prototype.get=function(){var a;0<this.g?(this.g--,a=this.b,this.b=a.next,a.next=null):a=this.f();return a};
function qa(a,b){a.j(b);a.g<a.i&&(a.g++,b.next=a.b,a.b=b)}
;function ra(a){if(Error.captureStackTrace)Error.captureStackTrace(this,ra);else{var b=Error().stack;b&&(this.stack=b)}a&&(this.message=String(a))}
x(ra,Error);ra.prototype.name="CustomError";var sa;function ta(a,b){for(var c in a)b.call(void 0,a[c],c,a)}
function ua(a){var b=va,c;for(c in b)if(a.call(void 0,b[c],c,b))return c}
function wa(){var a=xa,b;for(b in a)return!1;return!0}
function ya(a,b){if(null!==a&&b in a)throw Error('The object already contains the key "'+b+'"');a[b]=!0}
function za(a){var b={},c;for(c in a)b[c]=a[c];return b}
var Ca="constructor hasOwnProperty isPrototypeOf propertyIsEnumerable toLocaleString toString valueOf".split(" ");function Da(a,b){for(var c,d,e=1;e<arguments.length;e++){d=arguments[e];for(c in d)a[c]=d[c];for(var f=0;f<Ca.length;f++)c=Ca[f],Object.prototype.hasOwnProperty.call(d,c)&&(a[c]=d[c])}}
;var Ea=String.prototype.trim?function(a){return a.trim()}:function(a){return a.replace(/^[\s\xa0]+|[\s\xa0]+$/g,"")};
function Fa(a,b){return a<b?-1:a>b?1:0}
function Ga(a){for(var b=0,c=0;c<a.length;++c)b=31*b+a.charCodeAt(c)>>>0;return b}
;var Ha=window.yt&&window.yt.config_||window.ytcfg&&window.ytcfg.data_||{};q("yt.config_",Ha,void 0);var Ia=window.yt&&window.yt.msgs_||window.ytcfg&&window.ytcfg.msgs||{};q("yt.msgs_",Ia,void 0);function y(a){Ja(Ha,arguments)}
function z(a,b){return a in Ha?Ha[a]:b}
function A(a,b){fa(a)&&(a=Ka(a));return window.setTimeout(a,b)}
function La(a){window.clearTimeout(a)}
function Ka(a){return a&&window.yterr?function(){try{return a.apply(this,arguments)}catch(b){Ma(b)}}:a}
function Ma(a,b){var c=r("yt.logging.errors.log");c?c(a,b,void 0,void 0,void 0):(c=z("ERRORS",[]),c.push([a,b,void 0,void 0,void 0]),y("ERRORS",c))}
function Ja(a,b){if(1<b.length){var c=b[0];a[c]=b[1]}else{var d=b[0];for(c in d)a[c]=d[c]}}
var Na=window.performance&&window.performance.timing&&window.performance.now?function(){return window.performance.timing.navigationStart+window.performance.now()}:function(){return(new Date).getTime()},Oa="Microsoft Internet Explorer"==navigator.appName;function Pa(a,b,c){a&&(a.dataset?a.dataset[Qa(b)]=c:a.setAttribute("data-"+b,c))}
function B(a,b){return a?a.dataset?a.dataset[Qa(b)]:a.getAttribute("data-"+b):null}
function Ra(a,b){a&&(a.dataset?delete a.dataset[Qa(b)]:a.removeAttribute("data-"+b))}
var Sa={};function Qa(a){return Sa[a]||(Sa[a]=String(a).replace(/\-([a-z])/g,function(a,c){return c.toUpperCase()}))}
;function C(){this.g=this.g;this.J=this.J}
C.prototype.g=!1;C.prototype.dispose=function(){this.g||(this.g=!0,this.A())};
function Ta(a,b){a.g?p(void 0)?b.call(void 0):b():(a.J||(a.J=[]),a.J.push(p(void 0)?v(b,void 0):b))}
C.prototype.A=function(){if(this.J)for(;this.J.length;)this.J.shift()()};
function Ua(a){a&&"function"==typeof a.dispose&&a.dispose()}
function Va(a){for(var b=0,c=arguments.length;b<c;++b){var d=arguments[b];ea(d)?Va.apply(null,d):Ua(d)}}
;var D;a:{var Wa=n.navigator;if(Wa){var Xa=Wa.userAgent;if(Xa){D=Xa;break a}}D=""}function E(a){return-1!=D.indexOf(a)}
;var Ya=Array.prototype.indexOf?function(a,b,c){return Array.prototype.indexOf.call(a,b,c)}:function(a,b,c){c=null==c?0:0>c?Math.max(0,a.length+c):c;
if(t(a))return t(b)&&1==b.length?a.indexOf(b,c):-1;for(;c<a.length;c++)if(c in a&&a[c]===b)return c;return-1},F=Array.prototype.forEach?function(a,b,c){Array.prototype.forEach.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=t(a)?a.split(""):a,f=0;f<d;f++)f in e&&b.call(c,e[f],f,a)},Za=Array.prototype.filter?function(a,b,c){return Array.prototype.filter.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=[],f=0,g=t(a)?a.split(""):a,k=0;k<d;k++)if(k in g){var h=g[k];
b.call(c,h,k,a)&&(e[f++]=h)}return e},$a=Array.prototype.map?function(a,b,c){return Array.prototype.map.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=Array(d),f=t(a)?a.split(""):a,g=0;g<d;g++)g in f&&(e[g]=b.call(c,f[g],g,a));
return e},ab=Array.prototype.some?function(a,b,c){return Array.prototype.some.call(a,b,c)}:function(a,b,c){for(var d=a.length,e=t(a)?a.split(""):a,f=0;f<d;f++)if(f in e&&b.call(c,e[f],f,a))return!0;
return!1};
function bb(a,b){var c;a:{c=a.length;for(var d=t(a)?a.split(""):a,e=0;e<c;e++)if(e in d&&b.call(void 0,d[e],e,a)){c=e;break a}c=-1}return 0>c?null:t(a)?a.charAt(c):a[c]}
function cb(a,b){return 0<=Ya(a,b)}
function db(a,b){var c=Ya(a,b);0<=c&&Array.prototype.splice.call(a,c,1)}
function eb(a){return Array.prototype.concat.apply(Array.prototype,arguments)}
function fb(a){var b=a.length;if(0<b){for(var c=Array(b),d=0;d<b;d++)c[d]=a[d];return c}return[]}
function gb(a,b){for(var c=1;c<arguments.length;c++){var d=arguments[c];if(ea(d)){var e=a.length||0,f=d.length||0;a.length=e+f;for(var g=0;g<f;g++)a[e+g]=d[g]}else a.push(d)}}
function hb(a,b,c,d){return Array.prototype.splice.apply(a,jb(arguments,1))}
function jb(a,b,c){return 2>=arguments.length?Array.prototype.slice.call(a,b):Array.prototype.slice.call(a,b,c)}
;function kb(){this.g=this.b=null}
var mb=new pa(function(){return new lb},function(a){a.reset()},100);
kb.prototype.remove=function(){var a=null;this.b&&(a=this.b,this.b=this.b.next,this.b||(this.g=null),a.next=null);return a};
function lb(){this.next=this.scope=this.b=null}
lb.prototype.set=function(a,b){this.b=a;this.scope=b;this.next=null};
lb.prototype.reset=function(){this.next=this.scope=this.b=null};function nb(a,b){isNaN(b)&&(b=void 0);var c=r("yt.scheduler.instance.addJob");return c?c(a,1,b):void 0===b?(a(),NaN):A(a,b||0)}
;function ob(){this.b="";this.g=pb}
ob.prototype.ua=!0;ob.prototype.ta=function(){return this.b};
function qb(a){return a instanceof ob&&a.constructor===ob&&a.g===pb?a.b:"type_error:SafeUrl"}
var rb=/^(?:(?:https?|mailto|ftp):|[^&:/?#]*(?:[/?#]|$))/i;function sb(a){if(a instanceof ob)return a;a=a.ua?a.ta():String(a);rb.test(a)||(a="about:invalid#zClosurez");return tb(a)}
var pb={};function tb(a){var b=new ob;b.b=a;return b}
tb("about:blank");function ub(){this.b="";this.g=vb}
ub.prototype.ua=!0;ub.prototype.ta=function(){return this.b};
var vb={};function wb(){return(E("Chrome")||E("CriOS"))&&!E("Edge")}
;function xb(a){n.setTimeout(function(){throw a;},0)}
var yb;
function zb(){var a=n.MessageChannel;"undefined"===typeof a&&"undefined"!==typeof window&&window.postMessage&&window.addEventListener&&!E("Presto")&&(a=function(){var a=document.createElement("IFRAME");a.style.display="none";a.src="";document.documentElement.appendChild(a);var b=a.contentWindow,a=b.document;a.open();a.write("");a.close();var c="callImmediate"+Math.random(),d="file:"==b.location.protocol?"*":b.location.protocol+"//"+b.location.host,a=v(function(a){if(("*"==d||a.origin==d)&&a.data==
c)this.port1.onmessage()},this);
b.addEventListener("message",a,!1);this.port1={};this.port2={postMessage:function(){b.postMessage(c,d)}}});
if("undefined"!==typeof a&&!E("Trident")&&!E("MSIE")){var b=new a,c={},d=c;b.port1.onmessage=function(){if(p(c.next)){c=c.next;var a=c.Ga;c.Ga=null;a()}};
return function(a){d.next={Ga:a};d=d.next;b.port2.postMessage(0)}}return"undefined"!==typeof document&&"onreadystatechange"in document.createElement("SCRIPT")?function(a){var b=document.createElement("SCRIPT");
b.onreadystatechange=function(){b.onreadystatechange=null;b.parentNode.removeChild(b);b=null;a();a=null};
document.documentElement.appendChild(b)}:function(a){n.setTimeout(a,0)}}
;function Ab(){this.b=""}
Ab.prototype.ua=!0;Ab.prototype.ta=function(){return this.b};
function Bb(a){var b=new Ab;b.b=a;return b}
Bb("<!DOCTYPE html>");Bb("");Bb("<br>");function Cb(a,b){Db||Eb();Fb||(Db(),Fb=!0);var c=Gb,d=mb.get();d.set(a,b);c.g?c.g.next=d:c.b=d;c.g=d}
var Db;function Eb(){if(-1!=String(n.Promise).indexOf("[native code]")){var a=n.Promise.resolve(void 0);Db=function(){a.then(Hb)}}else Db=function(){var a=Hb;
!fa(n.setImmediate)||n.Window&&n.Window.prototype&&!E("Edge")&&n.Window.prototype.setImmediate==n.setImmediate?(yb||(yb=zb()),yb(a)):n.setImmediate(a)}}
var Fb=!1,Gb=new kb;function Hb(){for(var a;a=Gb.remove();){try{a.b.call(a.scope)}catch(b){xb(b)}qa(mb,a)}Fb=!1}
;function Ib(a,b){var c;c=b instanceof ob?b:sb(b);a.href=qb(c)}
function Jb(a,b){a.rel="stylesheet";a.href=b instanceof ub&&b.constructor===ub&&b.g===vb?b.b:"type_error:TrustedResourceUrl"}
;function G(a){C.call(this);this.o=1;this.i=[];this.j=0;this.b=[];this.f={};this.C=!!a}
x(G,C);l=G.prototype;l.subscribe=function(a,b,c){var d=this.f[a];d||(d=this.f[a]=[]);var e=this.o;this.b[e]=a;this.b[e+1]=b;this.b[e+2]=c;this.o=e+3;d.push(e);return e};
function Kb(a,b,c,d){if(b=a.f[b]){var e=a.b;(b=bb(b,function(a){return e[a+1]==c&&e[a+2]==d}))&&a.P(b)}}
l.P=function(a){var b=this.b[a];if(b){var c=this.f[b];0!=this.j?(this.i.push(a),this.b[a+1]=aa):(c&&db(c,a),delete this.b[a],delete this.b[a+1],delete this.b[a+2])}return!!b};
l.N=function(a,b){var c=this.f[a];if(c){for(var d=Array(arguments.length-1),e=1,f=arguments.length;e<f;e++)d[e-1]=arguments[e];if(this.C)for(e=0;e<c.length;e++){var g=c[e];Lb(this.b[g+1],this.b[g+2],d)}else{this.j++;try{for(e=0,f=c.length;e<f;e++)g=c[e],this.b[g+1].apply(this.b[g+2],d)}finally{if(this.j--,0<this.i.length&&0==this.j)for(;c=this.i.pop();)this.P(c)}}return 0!=e}return!1};
function Lb(a,b,c){Cb(function(){a.apply(b,c)})}
l.clear=function(a){if(a){var b=this.f[a];b&&(F(b,this.P,this),delete this.f[a])}else this.b.length=0,this.f={}};
l.aa=function(a){if(a){var b=this.f[a];return b?b.length:0}a=0;for(b in this.f)a+=this.aa(b);return a};
l.A=function(){G.B.A.call(this);this.clear();this.i.length=0};var Mb=r("yt.pubsub.instance_")||new G;G.prototype.subscribe=G.prototype.subscribe;G.prototype.unsubscribeByKey=G.prototype.P;G.prototype.publish=G.prototype.N;G.prototype.clear=G.prototype.clear;q("yt.pubsub.instance_",Mb,void 0);var Nb=r("yt.pubsub.subscribedKeys_")||{};q("yt.pubsub.subscribedKeys_",Nb,void 0);var Ob=r("yt.pubsub.topicToKeys_")||{};q("yt.pubsub.topicToKeys_",Ob,void 0);var Pb=r("yt.pubsub.isSynchronous_")||{};q("yt.pubsub.isSynchronous_",Pb,void 0);
var Qb=r("yt.pubsub.skipSubId_")||null;q("yt.pubsub.skipSubId_",Qb,void 0);function Rb(a,b,c){var d=Sb();if(d){var e=d.subscribe(a,function(){if(!Qb||Qb!=e){var d=arguments,g;g=function(){Nb[e]&&b.apply(c||window,d)};
try{Pb[a]?g():A(g,0)}catch(k){Ma(k)}}},c);
Nb[e]=!0;Ob[a]||(Ob[a]=[]);Ob[a].push(e);return e}return 0}
function Tb(a){var b=Sb();b&&("number"==typeof a?a=[a]:"string"==typeof a&&(a=[parseInt(a,10)]),F(a,function(a){b.unsubscribeByKey(a);delete Nb[a]}))}
function Ub(a,b){var c=Sb();return c?c.publish.apply(c,arguments):!1}
function Vb(a){Ob[a]&&(a=Ob[a],F(a,function(a){Nb[a]&&delete Nb[a]}),a.length=0)}
function Wb(a){var b=Sb();if(b)if(b.clear(a),a)Vb(a);else for(var c in Ob)Vb(c)}
function Sb(){return r("yt.pubsub.instance_")}
;function Xb(a,b){if(window.spf){var c="";if(a){var d=a.indexOf("jsbin/"),e=a.lastIndexOf(".js"),f=d+6;-1<d&&-1<e&&e>f&&(c=a.substring(f,e),c=c.replace(Yb,""),c=c.replace(Zb,""),c=c.replace("debug-",""),c=c.replace("tracing-",""))}spf.script.load(a,c,b)}else $b(a,b)}
function $b(a,b){var c=ac(a),d=document.getElementById(c),e=d&&B(d,"loaded"),f=d&&!e;if(e)b&&b();else{if(b){var e=Rb(c,b),g=""+ia(b);bc[g]=e}f||(d=cc(a,c,function(){B(d,"loaded")||(Pa(d,"loaded","true"),Ub(c),A(na(Wb,c),0))}))}}
function cc(a,b,c){var d=document.createElement("script");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
d.onreadystatechange=function(){switch(d.readyState){case "loaded":case "complete":d.onload()}};
d.src=a;a=document.getElementsByTagName("head")[0]||document.body;a.insertBefore(d,a.firstChild);return d}
function dc(a,b){if(a&&b){var c=""+ia(b);(c=bc[c])&&Tb(c)}}
function ac(a){var b=document.createElement("a");Ib(b,a);a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"js-"+Ga(a)}
var Yb=/\.vflset|-vfl[a-zA-Z0-9_+=-]+/,Zb=/-[a-zA-Z]{2,3}_[a-zA-Z]{2,3}(?=(\/|$))/,bc={};var ec=null;function fc(){var a=z("BG_I",null),b=z("BG_IU",null),c=z("BG_P",void 0);b?Xb(b,function(){ec=new botguard.bg(c)}):a&&(eval(a),ec=new botguard.bg(c))}
function gc(){return null!=ec}
function hc(){return ec?ec.invoke():null}
;var ic=[],jc=!1;function kc(){function a(){jc=!0;"google_ad_status"in window?y("DCLKSTAT",1):y("DCLKSTAT",2)}
Xb("//static.doubleclick.net/instream/ad_status.js",a);ic.push(nb(function(){jc||"google_ad_status"in window||(dc("//static.doubleclick.net/instream/ad_status.js",a),y("DCLKSTAT",3))},5E3))}
function lc(){return parseInt(z("DCLKSTAT",0),10)}
;function nc(a){if(!a)return"";a=a.split("#")[0].split("?")[0];a=a.toLowerCase();0==a.indexOf("//")&&(a=window.location.protocol+a);/^[\w\-]*:\/\//.test(a)||(a=window.location.href);var b=a.substring(a.indexOf("://")+3),c=b.indexOf("/");-1!=c&&(b=b.substring(0,c));a=a.substring(0,a.indexOf("://"));if("http"!==a&&"https"!==a&&"chrome-extension"!==a&&"file"!==a&&"android-app"!==a)throw Error("Invalid URI scheme in origin");var c="",d=b.indexOf(":");if(-1!=d){var e=b.substring(d+1),b=b.substring(0,d);
if("http"===a&&"80"!==e||"https"===a&&"443"!==e)c=":"+e}return a+"://"+b+c}
;function oc(){function a(){e[0]=1732584193;e[1]=4023233417;e[2]=2562383102;e[3]=271733878;e[4]=3285377520;u=m=0}
function b(a){for(var b=g,c=0;64>c;c+=4)b[c/4]=a[c]<<24|a[c+1]<<16|a[c+2]<<8|a[c+3];for(c=16;80>c;c++)a=b[c-3]^b[c-8]^b[c-14]^b[c-16],b[c]=(a<<1|a>>>31)&4294967295;a=e[0];for(var d=e[1],f=e[2],h=e[3],k=e[4],m,u,c=0;80>c;c++)40>c?20>c?(m=h^d&(f^h),u=1518500249):(m=d^f^h,u=1859775393):60>c?(m=d&f|h&(d|f),u=2400959708):(m=d^f^h,u=3395469782),m=((a<<5|a>>>27)&4294967295)+m+k+u+b[c]&4294967295,k=h,h=f,f=(d<<30|d>>>2)&4294967295,d=a,a=m;e[0]=e[0]+a&4294967295;e[1]=e[1]+d&4294967295;e[2]=e[2]+f&4294967295;
e[3]=e[3]+h&4294967295;e[4]=e[4]+k&4294967295}
function c(a,c){if("string"===typeof a){a=unescape(encodeURIComponent(a));for(var d=[],e=0,g=a.length;e<g;++e)d.push(a.charCodeAt(e));a=d}c||(c=a.length);d=0;if(0==m)for(;d+64<c;)b(a.slice(d,d+64)),d+=64,u+=64;for(;d<c;)if(f[m++]=a[d++],u++,64==m)for(m=0,b(f);d+64<c;)b(a.slice(d,d+64)),d+=64,u+=64}
function d(){var a=[],d=8*u;56>m?c(k,56-m):c(k,64-(m-56));for(var g=63;56<=g;g--)f[g]=d&255,d>>>=8;b(f);for(g=d=0;5>g;g++)for(var h=24;0<=h;h-=8)a[d++]=e[g]>>h&255;return a}
for(var e=[],f=[],g=[],k=[128],h=1;64>h;++h)k[h]=0;var m,u;a();return{reset:a,update:c,digest:d,kb:function(){for(var a=d(),b="",c=0;c<a.length;c++)b+="0123456789ABCDEF".charAt(Math.floor(a[c]/16))+"0123456789ABCDEF".charAt(a[c]%16);return b}}}
;/*
 gapi.loader.OBJECT_CREATE_TEST_OVERRIDE &&*/
var pc=window,qc=document,rc=pc.location;function sc(){}
var tc=/\[native code\]/;function H(a,b,c){return a[b]=a[b]||c}
function uc(a){for(var b=0;b<this.length;b++)if(this[b]===a)return b;return-1}
function vc(a){a=a.sort();for(var b=[],c=void 0,d=0;d<a.length;d++){var e=a[d];e!=c&&b.push(e);c=e}return b}
function I(){var a;if((a=Object.create)&&tc.test(a))a=a(null);else{a={};for(var b in a)a[b]=void 0}return a}
var wc=H(pc,"gapi",{});function xc(a){return/^\s*$/.test(a)?!1:/^[\],:{}\s\u2028\u2029]*$/.test(a.replace(/\\["\\\/bfnrtu]/g,"@").replace(/(?:"[^"\\\n\r\u2028\u2029\x00-\x08\x0a-\x1f]*"|true|false|null|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)[\s\u2028\u2029]*(?=:|,|]|}|$)/g,"]").replace(/(?:^|:|,)(?:[\s\u2028\u2029]*\[)+/g,""))}
function yc(a){a=String(a);if(xc(a))try{return eval("("+a+")")}catch(b){}throw Error("Invalid JSON string: "+a);}
function zc(a){return eval("("+a+")")}
function Ac(a){var b=[];Bc(new Cc,a,b);return b.join("")}
function Cc(){}
function Bc(a,b,c){if(null==b)c.push("null");else{if("object"==typeof b){if(da(b)){var d=b;b=d.length;c.push("[");for(var e="",f=0;f<b;f++)c.push(e),e=d[f],Bc(a,e,c),e=",";c.push("]");return}if(b instanceof String||b instanceof Number||b instanceof Boolean)b=b.valueOf();else{c.push("{");f="";for(d in b)Object.prototype.hasOwnProperty.call(b,d)&&(e=b[d],"function"!=typeof e&&(c.push(f),Dc(d,c),c.push(":"),Bc(a,e,c),f=","));c.push("}");return}}switch(typeof b){case "string":Dc(b,c);break;case "number":c.push(isFinite(b)&&
!isNaN(b)?String(b):"null");break;case "boolean":c.push(String(b));break;case "function":c.push("null");break;default:throw Error("Unknown type: "+typeof b);}}}
var Ec={'"':'\\"',"\\":"\\\\","/":"\\/","\b":"\\b","\f":"\\f","\n":"\\n","\r":"\\r","\t":"\\t","\x0B":"\\u000b"},Fc=/\uffff/.test("\uffff")?/[\\\"\x00-\x1f\x7f-\uffff]/g:/[\\\"\x00-\x1f\x7f-\xff]/g;function Dc(a,b){b.push('"',a.replace(Fc,function(a){var b=Ec[a];b||(b="\\u"+(a.charCodeAt(0)|65536).toString(16).substr(1),Ec[a]=b);return b}),'"')}
;function Gc(a,b){this.width=a;this.height=b}
l=Gc.prototype;l.aspectRatio=function(){return this.width/this.height};
l.isEmpty=function(){return!(this.width*this.height)};
l.ceil=function(){this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
l.floor=function(){this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
l.round=function(){this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function Hc(a){this.b=a||{cookie:""}}
var Ic=/\s*;\s*/;l=Hc.prototype;l.isEnabled=function(){return navigator.cookieEnabled};
l.set=function(a,b,c,d,e,f){if(/[;=\s]/.test(a))throw Error('Invalid cookie name "'+a+'"');if(/[;\r\n]/.test(b))throw Error('Invalid cookie value "'+b+'"');p(c)||(c=-1);e=e?";domain="+e:"";d=d?";path="+d:"";f=f?";secure":"";c=0>c?"":0==c?";expires="+(new Date(1970,1,1)).toUTCString():";expires="+(new Date(w()+1E3*c)).toUTCString();this.b.cookie=a+"="+b+e+d+c+f};
l.get=function(a,b){for(var c=a+"=",d=(this.b.cookie||"").split(Ic),e=0,f;f=d[e];e++){if(0==f.lastIndexOf(c,0))return f.substr(c.length);if(f==a)return""}return b};
l.remove=function(a,b,c){var d=p(this.get(a));this.set(a,"",0,b,c);return d};
l.isEmpty=function(){return!this.b.cookie};
l.aa=function(){return this.b.cookie?(this.b.cookie||"").split(Ic).length:0};
l.clear=function(){for(var a=(this.b.cookie||"").split(Ic),b=[],c=[],d,e,f=0;e=a[f];f++)d=e.indexOf("="),-1==d?(b.push(""),c.push(e)):(b.push(e.substring(0,d)),c.push(e.substring(d+1)));for(a=b.length-1;0<=a;a--)this.remove(b[a])};
var Jc=new Hc("undefined"==typeof document?null:document);Jc.g=3950;function Kc(a){a.prototype.then=a.prototype.then;a.prototype.$goog_Thenable=!0}
;function Lc(a,b){var c=Mc;return Object.prototype.hasOwnProperty.call(c,a)?c[a]:c[a]=b(a)}
;function Nc(){}
;function Oc(a){this.type="";this.state=this.source=this.data=this.currentTarget=this.relatedTarget=this.target=null;this.charCode=this.keyCode=0;this.shiftKey=this.ctrlKey=this.altKey=!1;this.clientY=this.clientX=0;this.changedTouches=null;if(a=a||window.event){this.event=a;for(var b in a)b in Pc||(this[b]=a[b]);(b=a.target||a.srcElement)&&3==b.nodeType&&(b=b.parentNode);this.target=b;if(b=a.relatedTarget)try{b=b.nodeName?b:null}catch(c){b=null}else"mouseover"==this.type?b=a.fromElement:"mouseout"==
this.type&&(b=a.toElement);this.relatedTarget=b;this.clientX=void 0!=a.clientX?a.clientX:a.pageX;this.clientY=void 0!=a.clientY?a.clientY:a.pageY;this.keyCode=a.keyCode?a.keyCode:a.which;this.charCode=a.charCode||("keypress"==this.type?this.keyCode:0);this.altKey=a.altKey;this.ctrlKey=a.ctrlKey;this.shiftKey=a.shiftKey}}
Oc.prototype.preventDefault=function(){this.event&&(this.event.returnValue=!1,this.event.preventDefault&&this.event.preventDefault())};
Oc.prototype.stopPropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopPropagation&&this.event.stopPropagation())};
Oc.prototype.stopImmediatePropagation=function(){this.event&&(this.event.cancelBubble=!0,this.event.stopImmediatePropagation&&this.event.stopImmediatePropagation())};
var Pc={stopImmediatePropagation:1,stopPropagation:1,preventMouseEvent:1,preventManipulation:1,preventDefault:1,layerX:1,layerY:1,screenX:1,screenY:1,scale:1,rotation:1,webkitMovementX:1,webkitMovementY:1};function Qc(a,b,c){this.b=a;this.f=b;this.g=c}
var Rc=1;function Sc(a){var b={};void 0!==a.b?b.trackingParams=a.b:(b.veType=a.f,null!=a.g&&(b.veCounter=a.g));return b}
;var Tc=null;"undefined"!=typeof XMLHttpRequest?Tc=function(){return new XMLHttpRequest}:"undefined"!=typeof ActiveXObject&&(Tc=function(){return new ActiveXObject("Microsoft.XMLHTTP")});
function Uc(a){switch(a&&"status"in a?a.status:-1){case 200:case 201:case 202:case 203:case 204:case 205:case 206:case 304:return!0;default:return!1}}
;function Vc(a){this.b=a}
Vc.prototype.set=function(a,b){p(b)?this.b.set(a,Ac(b)):this.b.remove(a)};
Vc.prototype.get=function(a){var b;try{b=this.b.get(a)}catch(c){return}if(null!==b)try{return yc(b)}catch(c){throw"Storage: Invalid value was encountered";}};
Vc.prototype.remove=function(a){this.b.remove(a)};function Wc(a){return z("EXPERIMENT_FLAGS",{})[a]}
;function Xc(){return{apiaryHost:z("APIARY_HOST",void 0),hb:z("APIARY_HOST_FIRSTPARTY",void 0),gapiHintOverride:z("GAPI_HINT_OVERRIDE"),gapiHintParams:z("GAPI_HINT_PARAMS",void 0),innertubeApiKey:z("INNERTUBE_API_KEY",void 0),innertubeApiVersion:z("INNERTUBE_API_VERSION",void 0),tb:z("INNERTUBE_CONTEXT_CLIENT_NAME","WEB"),innertubeContextClientVersion:z("INNERTUBE_CONTEXT_CLIENT_VERSION",void 0),vb:z("INNERTUBE_CONTEXT_HL",void 0),ub:z("INNERTUBE_CONTEXT_GL",void 0),Vb:z("XHR_APIARY_HOST",void 0)}}
function Yc(a){a={client:{hl:a.vb,gl:a.ub,clientName:a.tb,clientVersion:a.innertubeContextClientVersion}};z("DELEGATED_SESSION_ID")&&(a.user={onBehalfOfUser:z("DELEGATED_SESSION_ID")});return a}
;var J;J=H(pc,"___jsl",I());H(J,"I",0);H(J,"hel",10);function Zc(){var a=rc.href,b;if(J.dpo)b=J.h;else{b=J.h;var c=RegExp("([#].*&|[#])jsh=([^&#]*)","g"),d=RegExp("([?#].*&|[?#])jsh=([^&#]*)","g");if(a=a&&(c.exec(a)||d.exec(a)))try{b=decodeURIComponent(a[2])}catch(e){}}return b}
function $c(a){var b=H(J,"PQ",[]);J.PQ=[];var c=b.length;if(0===c)a();else for(var d=0,e=function(){++d===c&&a()},f=0;f<c;f++)b[f](e)}
function ad(a){return H(H(J,"H",I()),a,I())}
;function bd(){return E("iPhone")&&!E("iPod")&&!E("iPad")}
;function cd(a){this.b=a}
x(cd,Vc);function dd(a){this.data=a}
function ed(a){return!p(a)||a instanceof dd?a:new dd(a)}
cd.prototype.set=function(a,b){cd.B.set.call(this,a,ed(b))};
cd.prototype.g=function(a){a=cd.B.get.call(this,a);if(!p(a)||a instanceof Object)return a;throw"Storage: Invalid value was encountered";};
cd.prototype.get=function(a){if(a=this.g(a)){if(a=a.data,!p(a))throw"Storage: Invalid value was encountered";}else a=void 0;return a};var fd=/^(?:([^:/?#.]+):)?(?:\/\/(?:([^/?#]*)@)?([^/#?]*?)(?::([0-9]+))?(?=[/#?]|$))?([^?#]+)?(?:\?([^#]*))?(?:#([\s\S]*))?$/;function K(a){return a.match(fd)}
function gd(a){return a?decodeURI(a):a}
function hd(a){if(a[1]){var b=a[0],c=b.indexOf("#");0<=c&&(a.push(b.substr(c)),a[0]=b=b.substr(0,c));c=b.indexOf("?");0>c?a[1]="?":c==b.length-1&&(a[1]=void 0)}return a.join("")}
function id(a,b,c){if(da(b))for(var d=0;d<b.length;d++)id(a,String(b[d]),c);else null!=b&&c.push("&",a,""===b?"":"=",encodeURIComponent(String(b)))}
function jd(a,b,c){for(c=c||0;c<b.length;c+=2)id(b[c],b[c+1],a);return a}
function kd(a,b){for(var c in b)id(c,b[c],a);return a}
function ld(a){a=kd([],a);a[0]="";return a.join("")}
function md(a,b){return hd(2==arguments.length?jd([a],arguments[1],0):jd([a],arguments,1))}
;function nd(a,b,c){var d=[],e=[];if(1==(da(c)?2:1))return e=[b,a],F(d,function(a){e.push(a)}),od(e.join(" "));
var f=[],g=[];F(c,function(a){g.push(a.key);f.push(a.value)});
c=Math.floor((new Date).getTime()/1E3);e=0==f.length?[c,b,a]:[f.join(":"),c,b,a];F(d,function(a){e.push(a)});
a=od(e.join(" "));a=[c,a];0==g.length||a.push(g.join(""));return a.join("_")}
function od(a){var b=oc();b.update(a);return b.kb().toLowerCase()}
;var pd=H(J,"perf",I());H(pd,"g",I());var qd=H(pd,"i",I());H(pd,"r",[]);I();I();function rd(a,b,c){b&&0<b.length&&(b=sd(b),c&&0<c.length&&(b+="___"+sd(c)),28<b.length&&(b=b.substr(0,28)+(b.length-28)),c=b,b=H(qd,"_p",I()),H(b,c,I())[a]=(new Date).getTime(),b=pd.r,"function"===typeof b?b(a,"_p",c):b.push([a,"_p",c]))}
function sd(a){return a.join("__").replace(/\./g,"_").replace(/\-/g,"_").replace(/\,/g,"_")}
;function ud(a){if(a.classList)return a.classList;a=a.className;return t(a)&&a.match(/\S+/g)||[]}
function vd(a,b){return a.classList?a.classList.contains(b):cb(ud(a),b)}
function wd(a,b){a.classList?a.classList.add(b):vd(a,b)||(a.className+=0<a.className.length?" "+b:b)}
function xd(a,b){a.classList?a.classList.remove(b):vd(a,b)&&(a.className=Za(ud(a),function(a){return a!=b}).join(" "))}
function yd(a,b,c){c?wd(a,b):xd(a,b)}
;function zd(a){this.b=a}
x(zd,cd);zd.prototype.set=function(a,b,c){if(b=ed(b)){if(c){if(c<w()){zd.prototype.remove.call(this,a);return}b.expiration=c}b.creation=w()}zd.B.set.call(this,a,b)};
zd.prototype.g=function(a,b){var c=zd.B.g.call(this,a);if(c){var d;if(d=!b){d=c.creation;var e=c.expiration;d=!!e&&e<w()||!!d&&d>w()}if(d)zd.prototype.remove.call(this,a);else return c}};function Ad(a){"?"==a.charAt(0)&&(a=a.substr(1));a=a.split("&");for(var b={},c=0,d=a.length;c<d;c++){var e=a[c].split("=");if(1==e.length&&e[0]||2==e.length){var f=decodeURIComponent((e[0]||"").replace(/\+/g," ")),e=decodeURIComponent((e[1]||"").replace(/\+/g," "));f in b?da(b[f])?gb(b[f],e):b[f]=[b[f],e]:b[f]=e}}return b}
function Bd(a,b){var c=a.split("#",2);a=c[0];var c=1<c.length?"#"+c[1]:"",d=a.split("?",2);a=d[0];var d=Ad(d[1]||""),e;for(e in b)d[e]=b[e];return hd(kd([a],d))+c}
;var Cd=I(),Dd=[];function Ed(a){throw Error("Bad hint"+(a?": "+a:""));}
Dd.push(["jsl",function(a){for(var b in a)if(Object.prototype.hasOwnProperty.call(a,b)){var c=a[b];"object"==typeof c?J[b]=H(J,b,[]).concat(c):H(J,b,c)}if(b=a.u)a=H(J,"us",[]),a.push(b),(b=/^https:(.*)$/.exec(b))&&a.push("http:"+b[1])}]);
var Fd=/^(\/[a-zA-Z0-9_\-]+)+$/,Gd=[/\/amp\//,/\/amp$/,/^\/amp$/],Hd=/^[a-zA-Z0-9\-_\.,!]+$/,Id=/^gapi\.loaded_[0-9]+$/,Jd=/^[a-zA-Z0-9,._-]+$/;function Kd(a,b,c,d){var e=a.split(";"),f=e.shift(),g=Cd[f],k=null;g?k=g(e,b,c,d):Ed("no hint processor for: "+f);k||Ed("failed to generate load url");b=k;c=b.match(Ld);(d=b.match(Md))&&1===d.length&&Nd.test(b)&&c&&1===c.length||Ed("failed sanity: "+a);return k}
function Od(a,b,c,d){function e(a){return encodeURIComponent(a).replace(/%2C/g,",")}
a=Pd(a);Id.test(c)||Ed("invalid_callback");b=Qd(b);d=d&&d.length?Qd(d):null;return[encodeURIComponent(a.Jb).replace(/%2C/g,",").replace(/%2F/g,"/"),"/k=",e(a.version),"/m=",e(b),d?"/exm="+e(d):"","/rt=j/sv=1/d=1/ed=1",a.Ea?"/am="+e(a.Ea):"",a.Pa?"/rs="+e(a.Pa):"",a.Wa?"/t="+e(a.Wa):"","/cb=",e(c)].join("")}
function Pd(a){"/"!==a.charAt(0)&&Ed("relative path");for(var b=a.substring(1).split("/"),c=[];b.length;){a=b.shift();if(!a.length||0==a.indexOf("."))Ed("empty/relative directory");else if(0<a.indexOf("=")){b.unshift(a);break}c.push(a)}a={};for(var d=0,e=b.length;d<e;++d){var f=b[d].split("="),g=decodeURIComponent(f[0]),k=decodeURIComponent(f[1]);2==f.length&&g&&k&&(a[g]=a[g]||k)}b="/"+c.join("/");Fd.test(b)||Ed("invalid_prefix");c=0;for(d=Gd.length;c<d;++c)Gd[c].test(b)&&Ed("invalid_prefix");c=Rd(a,
"k",!0);d=Rd(a,"am");e=Rd(a,"rs");a=Rd(a,"t");return{Jb:b,version:c,Ea:d,Pa:e,Wa:a}}
function Qd(a){for(var b=[],c=0,d=a.length;c<d;++c){var e=a[c].replace(/\./g,"_").replace(/-/g,"_");Jd.test(e)&&b.push(e)}return b.join(",")}
function Rd(a,b,c){a=a[b];!a&&c&&Ed("missing: "+b);if(a){if(Hd.test(a))return a;Ed("invalid: "+b)}return null}
var Nd=/^https?:\/\/[a-z0-9_.-]+\.google\.com(:\d+)?\/[a-zA-Z0-9_.,!=\-\/]+$/,Md=/\/cb=/g,Ld=/\/\//g;function Sd(){var a=Zc();if(!a)throw Error("Bad hint");return a}
Cd.m=function(a,b,c,d){(a=a[0])||Ed("missing_hint");return"https://apis.google.com"+Od(a,b,c,d)};
var Td=decodeURI("%73cript"),Ud=/^[-+_0-9\/A-Za-z]+={0,2}$/;function Vd(a,b){for(var c=[],d=0;d<a.length;++d){var e=a[d];e&&0>uc.call(b,e)&&c.push(e)}return c}
function Wd(){var a=J.nonce;if(void 0!==a)return a&&a===String(a)&&a.match(Ud)?a:J.nonce=null;var b=H(J,"us",[]);if(!b||!b.length)return J.nonce=null;for(var c=qc.getElementsByTagName(Td),d=0,e=c.length;d<e;++d){var f=c[d];if(f.src&&(a=String(f.getAttribute("nonce")||"")||null)){for(var g=0,k=b.length;g<k&&b[g]!==f.src;++g);if(g!==k&&a&&a===String(a)&&a.match(Ud))return J.nonce=a}}return null}
function Xd(a){if("loading"!=qc.readyState)Yd(a);else{var b=Wd(),c="";null!==b&&(c=' nonce="'+b+'"');qc.write("<"+Td+' src="'+encodeURI(a)+'"'+c+"></"+Td+">")}}
function Yd(a){var b=qc.createElement(Td);b.setAttribute("src",a);a=Wd();null!==a&&b.setAttribute("nonce",a);b.async="true";(a=qc.getElementsByTagName(Td)[0])?a.parentNode.insertBefore(b,a):(qc.head||qc.body||qc.documentElement).appendChild(b)}
function Zd(a,b){var c=b&&b._c;if(c)for(var d=0;d<Dd.length;d++){var e=Dd[d][0],f=Dd[d][1];f&&Object.prototype.hasOwnProperty.call(c,e)&&f(c[e],a,b)}}
function $d(a,b,c){ae(function(){var c;c=b===Zc()?H(wc,"_",I()):I();c=H(ad(b),"_",c);a(c)},c)}
function be(a,b){var c=b||{};"function"==typeof b&&(c={},c.callback=b);Zd(a,c);var d=a?a.split(":"):[],e=c.h||Sd(),f=H(J,"ah",I());if(f["::"]&&d.length){for(var g=[],k=null;k=d.shift();){var h=k.split("."),h=f[k]||f[h[1]&&"ns:"+h[0]||""]||e,m=g.length&&g[g.length-1]||null,u=m;m&&m.hint==h||(u={hint:h,features:[]},g.push(u));u.features.push(k)}var Z=g.length;if(1<Z){var ib=c.callback;ib&&(c.callback=function(){0==--Z&&ib()})}for(;d=g.shift();)ce(d.features,c,d.hint)}else ce(d||[],c,e)}
function ce(a,b,c){function d(a,b){if(Z)return 0;pc.clearTimeout(u);ib.push.apply(ib,ha);var d=((wc||{}).config||{}).update;d?d(f):f&&H(J,"cu",[]).push(f);if(b){rd("me0",a,mc);try{$d(b,c,m)}finally{rd("me1",a,mc)}}return 1}
a=vc(a)||[];var e=b.callback,f=b.config,g=b.timeout,k=b.ontimeout,h=b.onerror,m=void 0;"function"==typeof h&&(m=h);var u=null,Z=!1;if(g&&!k||!g&&k)throw"Timeout requires both the timeout parameter and ontimeout parameter to be set";var h=H(ad(c),"r",[]).sort(),ib=H(ad(c),"L",[]).sort(),mc=[].concat(h);0<g&&(u=pc.setTimeout(function(){Z=!0;k()},g));
var ha=Vd(a,ib);if(ha.length){var ha=Vd(a,h),Aa=H(J,"CP",[]),Ba=Aa.length;Aa[Ba]=function(a){function b(){var a=Aa[Ba+1];a&&a()}
function c(b){Aa[Ba]=null;d(ha,a)&&$c(function(){e&&e();b()})}
if(!a)return 0;rd("ml1",ha,mc);0<Ba&&Aa[Ba-1]?Aa[Ba]=function(){c(b)}:c(b)};
if(ha.length){var td="loaded_"+J.I++;wc[td]=function(a){Aa[Ba](a);wc[td]=null};
a=Kd(c,ha,"gapi."+td,h);h.push.apply(h,ha);rd("ml0",ha,mc);b.sync||pc.___gapisync?Xd(a):Yd(a)}else Aa[Ba](sc)}else d(ha)&&e&&e()}
function ae(a,b){if(J.hee&&0<J.hel)try{return a()}catch(c){b&&b(c),J.hel--,be("debug_error",function(){try{window.___jsl.hefn(c)}catch(d){throw c;}})}else try{return a()}catch(c){throw b&&b(c),c;
}}
wc.load=function(a,b){return ae(function(){return be(a,b)})};var de="StopIteration"in n?n.StopIteration:{message:"StopIteration",stack:""};function ee(){}
ee.prototype.next=function(){throw de;};
ee.prototype.$=function(){return this};
function fe(a){if(a instanceof ee)return a;if("function"==typeof a.$)return a.$(!1);if(ea(a)){var b=0,c=new ee;c.next=function(){for(;;){if(b>=a.length)throw de;if(b in a)return a[b++];b++}};
return c}throw Error("Not implemented");}
function ge(a,b){if(ea(a))try{F(a,b,void 0)}catch(c){if(c!==de)throw c;}else{a=fe(a);try{for(;;)b.call(void 0,a.next(),void 0,a)}catch(c){if(c!==de)throw c;}}}
function he(a){if(ea(a))return fb(a);a=fe(a);var b=[];ge(a,function(a){b.push(a)});
return b}
;function L(a,b){this.l=p(a)?a:0;this.w=p(b)?b:0}
L.prototype.equals=function(a){return a instanceof L&&(this==a?!0:this&&a?this.l==a.l&&this.w==a.w:!1)};
L.prototype.ceil=function(){this.l=Math.ceil(this.l);this.w=Math.ceil(this.w);return this};
L.prototype.floor=function(){this.l=Math.floor(this.l);this.w=Math.floor(this.w);return this};
L.prototype.round=function(){this.l=Math.round(this.l);this.w=Math.round(this.w);return this};var ie=E("Opera"),M=E("Trident")||E("MSIE"),je=E("Edge"),ke=E("Gecko")&&!(-1!=D.toLowerCase().indexOf("webkit")&&!E("Edge"))&&!(E("Trident")||E("MSIE"))&&!E("Edge"),le=-1!=D.toLowerCase().indexOf("webkit")&&!E("Edge"),me=E("Macintosh"),ne=E("Windows"),oe=E("Android"),pe=bd(),qe=E("iPad"),re=E("iPod");function se(){var a=n.document;return a?a.documentMode:void 0}
var te;a:{var ue="",ve=function(){var a=D;if(ke)return/rv\:([^\);]+)(\)|;)/.exec(a);if(je)return/Edge\/([\d\.]+)/.exec(a);if(M)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a);if(le)return/WebKit\/(\S+)/.exec(a);if(ie)return/(?:Version)[ \/]?(\S+)/.exec(a)}();
ve&&(ue=ve?ve[1]:"");if(M){var we=se();if(null!=we&&we>parseFloat(ue)){te=String(we);break a}}te=ue}var xe=te,Mc={};
function N(a){return Lc(a,function(){for(var b=0,c=Ea(String(xe)).split("."),d=Ea(String(a)).split("."),e=Math.max(c.length,d.length),f=0;0==b&&f<e;f++){var g=c[f]||"",k=d[f]||"";do{g=/(\d*)(\D*)(.*)/.exec(g)||["","","",""];k=/(\d*)(\D*)(.*)/.exec(k)||["","","",""];if(0==g[0].length&&0==k[0].length)break;b=Fa(0==g[1].length?0:parseInt(g[1],10),0==k[1].length?0:parseInt(k[1],10))||Fa(0==g[2].length,0==k[2].length)||Fa(g[2],k[2]);g=g[3];k=k[3]}while(0==b)}return 0<=b})}
var ye;var ze=n.document;ye=ze&&M?se()||("CSS1Compat"==ze.compatMode?parseInt(xe,10):5):void 0;!ke&&!M||M&&9<=Number(ye)||ke&&N("1.9.1");var Ae=M&&!N("9");function Be(a){Ce();var b=new ub;b.b=a;return b}
var Ce=aa;function De(a){this.b=a}
x(De,zd);function Ee(){}
x(Ee,Nc);Ee.prototype.aa=function(){var a=0;ge(this.$(!0),function(){a++});
return a};
Ee.prototype.clear=function(){var a=he(this.$(!0)),b=this;F(a,function(a){b.remove(a)})};var Fe=E("Firefox"),Ge=bd()||E("iPod"),He=E("iPad"),Ie=E("Android")&&!(wb()||E("Firefox")||E("Opera")||E("Silk")),Je=wb(),Ke=E("Safari")&&!(wb()||E("Coast")||E("Opera")||E("Edge")||E("Silk")||E("Android"))&&!(bd()||E("iPad")||E("iPod"));function Le(a){return a?new Me(Ne(a)):sa||(sa=new Me)}
function Oe(a){var b=document;return t(a)?b.getElementById(a):a}
function Pe(a){var b=document;return b.querySelectorAll&&b.querySelector?b.querySelectorAll("."+a):Qe(a)}
function Qe(a){var b,c,d,e;b=document;if(b.querySelectorAll&&b.querySelector&&a)return b.querySelectorAll(""+(a?"."+a:""));if(a&&b.getElementsByClassName){var f=b.getElementsByClassName(a);return f}f=b.getElementsByTagName("*");if(a){e={};for(c=d=0;b=f[c];c++){var g=b.className;"function"==typeof g.split&&cb(g.split(/\s+/),a)&&(e[d++]=b)}e.length=d;return e}return f}
function Re(a){a=a.document;a=Se(a)?a.documentElement:a.body;return new Gc(a.clientWidth,a.clientHeight)}
function Te(a){var b=a.scrollingElement?a.scrollingElement:!le&&Se(a)?a.documentElement:a.body||a.documentElement;a=a.parentWindow||a.defaultView;return M&&N("10")&&a.pageYOffset!=b.scrollTop?new L(b.scrollLeft,b.scrollTop):new L(a.pageXOffset||b.scrollLeft,a.pageYOffset||b.scrollTop)}
function Se(a){return"CSS1Compat"==a.compatMode}
function Ue(a){for(var b;b=a.firstChild;)a.removeChild(b)}
function Ve(a){if(!a)return null;if(a.firstChild)return a.firstChild;for(;a&&!a.nextSibling;)a=a.parentNode;return a?a.nextSibling:null}
function We(a){if(!a)return null;if(!a.previousSibling)return a.parentNode;for(a=a.previousSibling;a&&a.lastChild;)a=a.lastChild;return a}
function Ne(a){return 9==a.nodeType?a:a.ownerDocument||a.document}
function Xe(a,b){if("textContent"in a)a.textContent=b;else if(3==a.nodeType)a.data=b;else if(a.firstChild&&3==a.firstChild.nodeType){for(;a.lastChild!=a.firstChild;)a.removeChild(a.lastChild);a.firstChild.data=b}else Ue(a),a.appendChild(Ne(a).createTextNode(String(b)))}
var Ye={SCRIPT:1,STYLE:1,HEAD:1,IFRAME:1,OBJECT:1},Ze={IMG:" ",BR:"\n"};function $e(a){if(Ae&&null!==a&&"innerText"in a)a=a.innerText.replace(/(\r\n|\r|\n)/g,"\n");else{var b=[];af(a,b,!0);a=b.join("")}a=a.replace(/ \xAD /g," ").replace(/\xAD/g,"");a=a.replace(/\u200B/g,"");Ae||(a=a.replace(/ +/g," "));" "!=a&&(a=a.replace(/^\s*/,""));return a}
function af(a,b,c){if(!(a.nodeName in Ye))if(3==a.nodeType)c?b.push(String(a.nodeValue).replace(/(\r\n|\r|\n)/g,"")):b.push(a.nodeValue);else if(a.nodeName in Ze)b.push(Ze[a.nodeName]);else for(a=a.firstChild;a;)af(a,b,c),a=a.nextSibling}
function bf(a){var b=cf.Za;return b?df(a,function(a){return!b||t(a.className)&&cb(a.className.split(/\s+/),b)},!0,void 0):null}
function df(a,b,c,d){a&&!c&&(a=a.parentNode);for(c=0;a&&(null==d||c<=d);){if(b(a))return a;a=a.parentNode;c++}return null}
function Me(a){this.b=a||n.document||document}
Me.prototype.getElementsByTagName=function(a,b){return(b||this.b).getElementsByTagName(String(a))};
Me.prototype.createElement=function(a){return this.b.createElement(String(a))};
Me.prototype.isElement=function(a){return ga(a)&&1==a.nodeType};
Me.prototype.contains=function(a,b){if(!a||!b)return!1;if(a.contains&&1==b.nodeType)return a==b||a.contains(b);if("undefined"!=typeof a.compareDocumentPosition)return a==b||!!(a.compareDocumentPosition(b)&16);for(;b&&a!=b;)b=b.parentNode;return b==a};function O(a,b){this.b=0;this.C=void 0;this.i=this.g=this.f=null;this.j=this.o=!1;if(a!=aa)try{var c=this;a.call(b,function(a){ef(c,2,a)},function(a){ef(c,3,a)})}catch(d){ef(this,3,d)}}
function ff(){this.next=this.context=this.g=this.f=this.b=null;this.i=!1}
ff.prototype.reset=function(){this.context=this.g=this.f=this.b=null;this.i=!1};
var gf=new pa(function(){return new ff},function(a){a.reset()},100);
function hf(a,b,c){var d=gf.get();d.f=a;d.g=b;d.context=c;return d}
function jf(a){if(a instanceof O)return a;var b=new O(aa);ef(b,2,a);return b}
function kf(a){return new O(function(b,c){c(a)})}
O.prototype.then=function(a,b,c){return lf(this,fa(a)?a:null,fa(b)?b:null,c)};
Kc(O);O.prototype.cancel=function(a){0==this.b&&Cb(function(){var b=new mf(a);nf(this,b)},this)};
function nf(a,b){if(0==a.b)if(a.f){var c=a.f;if(c.g){for(var d=0,e=null,f=null,g=c.g;g&&(g.i||(d++,g.b==a&&(e=g),!(e&&1<d)));g=g.next)e||(f=g);e&&(0==c.b&&1==d?nf(c,b):(f?(d=f,d.next==c.i&&(c.i=d),d.next=d.next.next):of(c),pf(c,e,3,b)))}a.f=null}else ef(a,3,b)}
function qf(a,b){a.g||2!=a.b&&3!=a.b||rf(a);a.i?a.i.next=b:a.g=b;a.i=b}
function lf(a,b,c,d){var e=hf(null,null,null);e.b=new O(function(a,g){e.f=b?function(c){try{var e=b.call(d,c);a(e)}catch(m){g(m)}}:a;
e.g=c?function(b){try{var e=c.call(d,b);!p(e)&&b instanceof mf?g(b):a(e)}catch(m){g(m)}}:g});
e.b.f=a;qf(a,e);return e.b}
O.prototype.F=function(a){this.b=0;ef(this,2,a)};
O.prototype.J=function(a){this.b=0;ef(this,3,a)};
function ef(a,b,c){if(0==a.b){a===c&&(b=3,c=new TypeError("Promise cannot resolve to itself"));a.b=1;var d;a:{var e=c,f=a.F,g=a.J;if(e instanceof O)qf(e,hf(f||aa,g||null,a)),d=!0;else{var k;if(e)try{k=!!e.$goog_Thenable}catch(m){k=!1}else k=!1;if(k)e.then(f,g,a),d=!0;else{if(ga(e))try{var h=e.then;if(fa(h)){sf(e,h,f,g,a);d=!0;break a}}catch(m){g.call(a,m);d=!0;break a}d=!1}}}d||(a.C=c,a.b=b,a.f=null,rf(a),3!=b||c instanceof mf||tf(a,c))}}
function sf(a,b,c,d,e){function f(a){k||(k=!0,d.call(e,a))}
function g(a){k||(k=!0,c.call(e,a))}
var k=!1;try{b.call(a,g,f)}catch(h){f(h)}}
function rf(a){a.o||(a.o=!0,Cb(a.G,a))}
function of(a){var b=null;a.g&&(b=a.g,a.g=b.next,b.next=null);a.g||(a.i=null);return b}
O.prototype.G=function(){for(var a;a=of(this);)pf(this,a,this.b,this.C);this.o=!1};
function pf(a,b,c,d){if(3==c&&b.g&&!b.i)for(;a&&a.j;a=a.f)a.j=!1;if(b.b)b.b.f=null,uf(b,c,d);else try{b.i?b.f.call(b.context):uf(b,c,d)}catch(e){vf.call(null,e)}qa(gf,b)}
function uf(a,b,c){2==b?a.f.call(a.context,c):a.g&&a.g.call(a.context,c)}
function tf(a,b){a.j=!0;Cb(function(){a.j&&vf.call(null,b)})}
var vf=xb;function mf(a){ra.call(this,a)}
x(mf,ra);mf.prototype.name="cancel";function wf(a){this.b=a}
x(wf,Ee);l=wf.prototype;l.isAvailable=function(){if(!this.b)return!1;try{return this.b.setItem("__sak","1"),this.b.removeItem("__sak"),!0}catch(a){return!1}};
l.set=function(a,b){try{this.b.setItem(a,b)}catch(c){if(0==this.b.length)throw"Storage mechanism: Storage disabled";throw"Storage mechanism: Quota exceeded";}};
l.get=function(a){a=this.b.getItem(a);if(!t(a)&&null!==a)throw"Storage mechanism: Invalid value was encountered";return a};
l.remove=function(a){this.b.removeItem(a)};
l.aa=function(){return this.b.length};
l.$=function(a){var b=0,c=this.b,d=new ee;d.next=function(){if(b>=c.length)throw de;var d=c.key(b++);if(a)return d;d=c.getItem(d);if(!t(d))throw"Storage mechanism: Invalid value was encountered";return d};
return d};
l.clear=function(){this.b.clear()};
l.key=function(a){return this.b.key(a)};function xf(){var a=null;try{a=window.localStorage||null}catch(b){}this.b=a}
x(xf,wf);function yf(){var a=null;try{a=window.sessionStorage||null}catch(b){}this.b=a}
x(yf,wf);var zf=r("yt.dom.getNextId_");if(!zf){zf=function(){return++Af};
q("yt.dom.getNextId_",zf,void 0);var Af=0}function Bf(){var a=document,b;ab(["fullscreenElement","webkitFullscreenElement","mozFullScreenElement","msFullscreenElement"],function(c){b=a[c];return!!b});
return b}
;function Cf(a){this.b=a||Xc();Df||(Df=Ef(this.b))}
var Df=null;function Ef(a){return(new O(function(b){try{var c={gapiHintOverride:a.gapiHintOverride,_c:{jsl:{h:a.gapiHintParams}},callback:b},d=fa(c)?{callback:c}:c||{};d._c&&d._c.jsl&&d._c.jsl.h||Da(d,{_c:{jsl:{h:z("GAPI_HINT_PARAMS",void 0)}}});if(d.gapiHintOverride||z("GAPI_HINT_OVERRIDE")){var e;var f=document.location.href;if(-1!=f.indexOf("?")){var f=(f||"").split("#")[0],g=f.split("?",2);e=Ad(1<g.length?g[1]:g[0])}else e={};var k=e.gapi_jsh;k&&Da(d,{_c:{jsl:{h:k}}})}be("client",d)}catch(h){Ma(h)}})).then(function(){})}
Cf.prototype.i=function(){var a=r("gapi.config.update");a("googleapis.config/auth/useFirstPartyAuth",!0);var b=this.b.apiaryHost;/^[\s\xa0]*$/.test(null==b?"":String(b))||a("googleapis.config/root",(-1==b.indexOf("://")?"//":"")+b);b=this.b.hb;/^[\s\xa0]*$/.test(null==b?"":String(b))||a("googleapis.config/root-1p",(-1==b.indexOf("://")?"//":"")+b);a("googleapis.config/sessionIndex",z("SESSION_INDEX"));r("gapi.client.setApiKey")(this.b.innertubeApiKey)};
Cf.prototype.g=function(){return{context:Yc(this.b)}};
Cf.prototype.f=function(a,b,c){var d,e=!1;0<c.timeout&&(d=A(function(){e||(e=!0,c.T&&c.T())},c.timeout));
Ff(this,a,b,function(a){if(!e)if(e=!0,d&&La(d),a)c.H&&c.H(a);else if(c.onError)c.onError()})};
function Ff(a,b,c,d){var e={path:"/youtubei/"+a.b.innertubeApiVersion+"/"+b,headers:{"X-Goog-Visitor-Id":z("VISITOR_DATA")},method:"POST",body:Ac(c)},f=v(a.i,a);Df.then(function(){f();r("gapi.client.request")(e).execute(d||aa)})}
;var va=r("yt.events.listeners_")||{};q("yt.events.listeners_",va,void 0);var Gf=r("yt.events.counter_")||{count:0};q("yt.events.counter_",Gf,void 0);function Hf(a,b,c,d){a.addEventListener&&("mouseenter"!=b||"onmouseenter"in document?"mouseleave"!=b||"onmouseenter"in document?"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"):b="mouseout":b="mouseover");return ua(function(e){return e[0]==a&&e[1]==b&&e[2]==c&&e[4]==!!d})}
function P(a,b,c,d){if(!a||!a.addEventListener&&!a.attachEvent)return"";d=!!d;var e=Hf(a,b,c,d);if(e)return e;var e=++Gf.count+"",f=!("mouseenter"!=b&&"mouseleave"!=b||!a.addEventListener||"onmouseenter"in document),g;g=f?function(d){d=new Oc(d);if(!df(d.relatedTarget,function(b){return b==a},!0))return d.currentTarget=a,d.type=b,c.call(a,d)}:function(b){b=new Oc(b);
b.currentTarget=a;return c.call(a,b)};
g=Ka(g);a.addEventListener?("mouseenter"==b&&f?b="mouseover":"mouseleave"==b&&f?b="mouseout":"mousewheel"==b&&"MozBoxSizing"in document.documentElement.style&&(b="MozMousePixelScroll"),a.addEventListener(b,g,d)):a.attachEvent("on"+b,g);va[e]=[a,b,c,g,d];return e}
function If(a){a&&("string"==typeof a&&(a=[a]),F(a,function(a){if(a in va){var b=va[a],d=b[0],e=b[1],f=b[3],b=b[4];d.removeEventListener?d.removeEventListener(e,f,b):d.detachEvent&&d.detachEvent("on"+e,f);delete va[a]}}))}
;var Jf={log_event:"events",log_interaction:"interactions"},Kf={},Lf={},Mf=0,xa=r("yt.logging.transport.logsQueue_")||{};q("yt.logging.transport.logsQueue_",xa,void 0);function Nf(a,b){xa[a.endpoint]=xa[a.endpoint]||[];var c=xa[a.endpoint];c.push(a.Ma);Lf[a.endpoint]=b;c.length>=(Number(Wc("web_logging_max_batch")||0)||20)?Of():Pf()}
function Of(){La(Mf);if(!wa()){for(var a in xa){var b=Kf[a];if(!b){b=Lf[a];if(!b)continue;b=new b;Kf[a]=b}var c=b.g();c.requestTimeMs=Math.round(Na());c[Jf[a]]=xa[a];b.f(a,c,{});delete xa[a]}wa()||Pf()}}
function Pf(){La(Mf);Mf=A(Of,z("LOGGING_BATCH_TIMEOUT",1E4))}
;function Qf(a,b,c,d,e,f,g){function k(){4==(h&&"readyState"in h?h.readyState:0)&&b&&Ka(b)(h)}
var h=Tc&&Tc();if(!("open"in h))return null;"onloadend"in h?h.addEventListener("loadend",k,!1):h.onreadystatechange=k;c=(c||"GET").toUpperCase();d=d||"";h.open(c,a,!0);f&&(h.responseType=f);g&&(h.withCredentials=!0);f="POST"==c;if(e=Rf(a,e))for(var m in e)h.setRequestHeader(m,e[m]),"content-type"==m.toLowerCase()&&(f=!1);f&&h.setRequestHeader("Content-Type","application/x-www-form-urlencoded");h.send(d);return h}
function Rf(a,b){b=b||{};var c;c||(c=window.location.href);var d=K(a)[1]||null,e=gd(K(a)[3]||null);d&&e?(d=c,c=K(a),d=K(d),c=c[3]==d[3]&&c[1]==d[1]&&c[4]==d[4]):c=e?gd(K(c)[3]||null)==e&&(Number(K(c)[4]||null)||null)==(Number(K(a)[4]||null)||null):!0;for(var f in Sf){if((e=d=z(Sf[f]))&&!(e=c)){var e=f,g=z("CORS_HEADER_WHITELIST")||{},k=gd(K(a)[3]||null);e=k?(g=g[k])?cb(g,e):!1:!0}e&&(b[f]=d)}return b}
function Tf(a,b){b.method="POST";b.D||(b.D={});Uf(a,b)}
function Vf(a,b){var c=z("XSRF_FIELD_NAME",void 0),d;b.headers&&(d=b.headers["Content-Type"]);return!b.gc&&(!gd(K(a)[3]||null)||b.withCredentials||gd(K(a)[3]||null)==document.location.hostname)&&"POST"==b.method&&(!d||"application/x-www-form-urlencoded"==d)&&!(b.D&&b.D[c])}
function Uf(a,b){var c=b.format||"JSON";b.sb&&(a=document.location.protocol+"//"+document.location.hostname+(document.location.port?":"+document.location.port:"")+a);var d=z("XSRF_FIELD_NAME",void 0),e=z("XSRF_TOKEN",void 0),f=b.xa;f&&(f[d]&&delete f[d],a=Bd(a,f||{}));var g=b.postBody||"",f=b.D;Vf(a,b)&&(f||(f={}),f[d]=e);f&&t(g)&&(d=Ad(g),Da(d,f),g=b.Na&&"JSON"==b.Na?JSON.stringify(d):ld(d));var k=!1,h,m=Qf(a,function(a){if(!k){k=!0;h&&La(h);var d=Uc(a),e=null;if(d||400<=a.status&&500>a.status)e=
Wf(c,a,b.fc);if(d)a:if(204==a.status)d=!0;else{switch(c){case "XML":d=0==parseInt(e&&e.return_code,10);break a;case "RAW":d=!0;break a}d=!!e}var e=e||{},f=b.context||n;d?b.H&&b.H.call(f,a,e):b.onError&&b.onError.call(f,a,e);b.wa&&b.wa.call(f,a,e)}},b.method,g,b.headers,b.responseType,b.withCredentials);
b.T&&0<b.timeout&&(h=A(function(){k||(k=!0,m.abort(),La(h),b.T.call(b.context||n,m))},b.timeout))}
function Wf(a,b,c){var d=null;switch(a){case "JSON":a=b.responseText;b=b.getResponseHeader("Content-Type")||"";a&&0<=b.indexOf("json")&&(d=zc(a));break;case "XML":if(b=(b=b.responseXML)?Xf(b):null)d={},F(b.getElementsByTagName("*"),function(a){d[a.tagName]=Yf(a)})}c&&Zf(d);
return d}
function Zf(a){if(ga(a))for(var b in a){var c;(c="html_content"==b)||(c=b.length-5,c=0<=c&&b.indexOf("_html",c)==c);if(c){c=b;var d;d=Bb(a[b]);a[c]=d}else Zf(a[b])}}
function Xf(a){return a?(a=("responseXML"in a?a.responseXML:a).getElementsByTagName("root"))&&0<a.length?a[0]:null:null}
function Yf(a){var b="";F(a.childNodes,function(a){b+=a.nodeValue});
return b}
var Sf={"X-Goog-Visitor-Id":"SANDBOXED_VISITOR_ID","X-YouTube-Client-Name":"INNERTUBE_CONTEXT_CLIENT_NAME","X-YouTube-Client-Version":"INNERTUBE_CONTEXT_CLIENT_VERSION","X-Youtube-Identity-Token":"ID_TOKEN","X-YouTube-Page-CL":"PAGE_CL","X-YouTube-Page-Label":"PAGE_BUILD_LABEL","X-YouTube-Variants-Checksum":"VARIANTS_CHECKSUM"};function $f(){if(!ag&&!bg||!window.JSON)return null;var a;try{a=ag.get("yt-player-two-stage-token")}catch(b){}if(!t(a))try{a=bg.get("yt-player-two-stage-token")}catch(b){}if(!t(a))return null;try{a=JSON.parse(a,void 0)}catch(b){}return a}
var bg,cg=new xf;bg=cg.isAvailable()?new De(cg):null;var ag,dg=new yf;ag=dg.isAvailable()?new De(dg):null;function eg(){this.b=Xc()}
eg.prototype.g=function(){return{context:Yc(this.b)}};
eg.prototype.f=function(a,b,c){b={headers:{"Content-Type":"application/json","X-Goog-Visitor-Id":z("VISITOR_DATA")},D:b,Na:"JSON",T:c.T,H:c.H,onError:c.onError,timeout:c.timeout,withCredentials:!0};a:{c=[];var d=nc(String(n.location.href)),e=n.__OVERRIDE_SID;null==e&&(e=(new Hc(document)).get("SID"));if(e&&(d=(e=0==d.indexOf("https:")||0==d.indexOf("chrome-extension:"))?n.__SAPISID:n.__APISID,null==d&&(d=(new Hc(document)).get(e?"SAPISID":"APISID")),d)){var e=e?"SAPISIDHASH":"APISIDHASH",f=String(n.location.href);
c=f&&d&&e?[e,nd(nc(f),d,c||null)].join(" "):null;break a}c=null}c&&(b.headers.Authorization=c,b.headers["X-Goog-AuthUser"]=z("SESSION_INDEX",0));Tf("//"+this.b.Vb+("/youtubei/"+this.b.innertubeApiVersion+"/"+a)+"?alt=json&key="+this.b.innertubeApiKey,b)};function fg(){if(null==r("_lact",window)){var a=parseInt(z("LACT"),10),a=isFinite(a)?w()-Math.max(a,0):-1;q("_lact",a,window);-1==a&&gg();P(document,"keydown",gg);P(document,"keyup",gg);P(document,"mousedown",gg);P(document,"mouseup",gg);Rb("page-mouse",gg);Rb("page-scroll",gg);Rb("page-resize",gg)}}
function gg(){null==r("_lact",window)&&(fg(),r("_lact",window));var a=w();q("_lact",a,window);Ub("USER_ACTIVE")}
function hg(){var a=r("_lact",window);return null==a?-1:Math.max(w()-a,0)}
;var ig={},jg=0;function kg(a,b,c,d){var e={};e.eventTimeMs=Math.round(d||Na());e[a]=b;Wc("web_gel_lact")&&(e.context={lastActivityMs:hg()});Nf({endpoint:"log_event",Ma:e},c)}
;function lg(a,b,c){mg(ng(),{attachChild:{csn:a,parentVisualElement:Sc(b),visualElements:[Sc(c)]}},void 0)}
function og(a,b){var c=ng(),d=$a(b,function(a){return Sc(a)});
mg(c,{visibilityUpdate:{csn:a,visualElements:d}})}
function mg(a,b,c){b.eventTimeMs=Math.round(Na());b.lactMs=hg();c&&(b.clientData=pg(c));Nf({endpoint:"log_interaction",Ma:b},a)}
function pg(a){var b={};a.analyticsChannelData&&(b.analyticsDatas=$a(a.analyticsChannelData,function(a){return{tabName:a.tabName,cardName:a.cardName,isChannelScreen:a.isChannelScreen,insightId:a.insightId,externalChannelId:a.externalChannelId,externalContentOwnerId:a.externalContentOwnerId}}));
return{playbackData:{clientPlaybackNonce:a.clientPlaybackNonce},analyticsChannelData:b,externalLinkData:a.externalLinkData}}
;function ng(){return Wc("enable_youtubei_innertube")?eg:Cf}
;function qg(){var a=z("ROOT_VE_TYPE",void 0);return a?new Qc(void 0,a,void 0):null}
function rg(){var a=z("client-screen-nonce",void 0);a||(a=z("EVENT_ID",void 0));return a}
;var sg=w().toString();function tg(a,b,c){b=void 0===b?{}:b;c=void 0===c?!1:c;var d=z("EVENT_ID");d&&(b.ei||(b.ei=d));if(b){var d=a,e=z("VALID_SESSION_TEMPDATA_DOMAINS",[]),f=gd(K(window.location.href)[3]||null);f&&e.push(f);f=gd(K(d)[3]||null);if(cb(e,f)||!f&&0==d.lastIndexOf("/",0))if(Wc("autoescape_tempdata_url")&&(e=document.createElement("a"),Ib(e,d),d=e.href),d){var f=K(d),d=f[5],e=f[6],f=f[7],g="";d&&(g+=d);e&&(g+="?"+e);f&&(g+="#"+f);d=g;e=d.indexOf("#");if(d=0>e?d:d.substr(0,e)){if(b.itct||b.ved)b.csn=b.csn||rg();
d="ST-"+Ga(d).toString(36);e=b?ld(b):"";Jc.set(""+d,e,5,"/","youtube.com");b&&(b=b.itct||b.ved,d=r("yt.logging.screen.storeParentElement"),b&&d&&d(new Qc(b)))}}}if(c)return!1;if((window.ytspf||{}).enabled)spf.navigate(a);else{var k,h;k=void 0===k?{}:k;h=void 0===h?"":h;c=window.location;a=hd(kd([a],k))+h;a=a instanceof ob?a:sb(a);c.href=qb(a)}return!0}
;function ug(a){a=a||{};this.url=a.url||"";this.urlV9As2=a.url_v9as2||"";this.args=a.args||za(vg);this.assets=a.assets||{};this.attrs=a.attrs||za(wg);this.params=a.params||za(xg);this.minVersion=a.min_version||"8.0.0";this.fallback=a.fallback||null;this.fallbackMessage=a.fallbackMessage||null;this.html5=!!a.html5;this.disable=a.disable||{};this.loaded=!!a.loaded;this.messages=a.messages||{}}
var vg={enablejsapi:1},wg={},xg={allowscriptaccess:"always",allowfullscreen:"true",bgcolor:"#000000"};function yg(a){a instanceof ug||(a=new ug(a));return a}
function zg(a){var b=new ug,c;for(c in a)if(a.hasOwnProperty(c)){var d=a[c];b[c]="object"==ca(d)?za(d):d}return b}
;function Ag(){this.f=this.g=this.b=0;this.i="";var a=r("window.navigator.plugins"),b=r("window.navigator.mimeTypes"),a=a&&a["Shockwave Flash"],b=b&&b["application/x-shockwave-flash"],b=a&&b&&b.enabledPlugin&&a.description||"";if(a=b){var c=a.indexOf("Shockwave Flash");0<=c&&(a=a.substr(c+15));for(var c=a.split(" "),d="",a="",e=0,f=c.length;e<f;e++)if(d)if(a)break;else a=c[e];else d=c[e];d=d.split(".");c=parseInt(d[0],10)||0;d=parseInt(d[1],10)||0;e=0;if("r"==a.charAt(0)||"d"==a.charAt(0))e=parseInt(a.substr(1),
10)||0;a=[c,d,e]}else a=[0,0,0];this.i=b;b=a;this.b=b[0];this.g=b[1];this.f=b[2];if(0>=this.b){var g,k,h,m;if(Oa)try{g=new ActiveXObject("ShockwaveFlash.ShockwaveFlash")}catch(u){g=null}else h=document.body,m=document.createElement("object"),m.setAttribute("type","application/x-shockwave-flash"),g=h.appendChild(m);if(g&&"GetVariable"in g)try{k=g.GetVariable("$version")}catch(u){k=""}h&&m&&h.removeChild(m);(g=k||"")?(g=g.split(" ")[1].split(","),g=[parseInt(g[0],10)||0,parseInt(g[1],10)||0,parseInt(g[2],
10)||0]):g=[0,0,0];this.b=g[0];this.g=g[1];this.f=g[2]}}
ba(Ag);function Bg(a,b,c,d){b="string"==typeof b?b.split("."):[b,c,d];b[0]=parseInt(b[0],10)||0;b[1]=parseInt(b[1],10)||0;b[2]=parseInt(b[2],10)||0;return a.b>b[0]||a.b==b[0]&&a.g>b[1]||a.b==b[0]&&a.g==b[1]&&a.f>=b[2]}
;function Cg(){C.call(this);this.b=new G;Ta(this,na(Ua,this.b))}
x(Cg,C);Cg.prototype.subscribe=function(a,b,c){return this.g?0:this.b.subscribe(a,b,c)};
Cg.prototype.P=function(a){return this.g?!1:this.b.P(a)};
Cg.prototype.j=function(a,b){this.g||this.b.N.apply(this.b,arguments)};function Dg(a,b,c,d){this.top=a;this.right=b;this.bottom=c;this.left=d}
l=Dg.prototype;l.getHeight=function(){return this.bottom-this.top};
l.contains=function(a){return this&&a?a instanceof Dg?a.left>=this.left&&a.right<=this.right&&a.top>=this.top&&a.bottom<=this.bottom:a.l>=this.left&&a.l<=this.right&&a.w>=this.top&&a.w<=this.bottom:!1};
l.ceil=function(){this.top=Math.ceil(this.top);this.right=Math.ceil(this.right);this.bottom=Math.ceil(this.bottom);this.left=Math.ceil(this.left);return this};
l.floor=function(){this.top=Math.floor(this.top);this.right=Math.floor(this.right);this.bottom=Math.floor(this.bottom);this.left=Math.floor(this.left);return this};
l.round=function(){this.top=Math.round(this.top);this.right=Math.round(this.right);this.bottom=Math.round(this.bottom);this.left=Math.round(this.left);return this};function Eg(a,b,c,d){this.left=a;this.top=b;this.width=c;this.height=d}
Eg.prototype.contains=function(a){return a instanceof L?a.l>=this.left&&a.l<=this.left+this.width&&a.w>=this.top&&a.w<=this.top+this.height:this.left<=a.left&&this.left+this.width>=a.left+a.width&&this.top<=a.top&&this.top+this.height>=a.top+a.height};
Eg.prototype.ceil=function(){this.left=Math.ceil(this.left);this.top=Math.ceil(this.top);this.width=Math.ceil(this.width);this.height=Math.ceil(this.height);return this};
Eg.prototype.floor=function(){this.left=Math.floor(this.left);this.top=Math.floor(this.top);this.width=Math.floor(this.width);this.height=Math.floor(this.height);return this};
Eg.prototype.round=function(){this.left=Math.round(this.left);this.top=Math.round(this.top);this.width=Math.round(this.width);this.height=Math.round(this.height);return this};function Fg(a,b){var c=Ne(a);return c.defaultView&&c.defaultView.getComputedStyle&&(c=c.defaultView.getComputedStyle(a,null))?c[b]||c.getPropertyValue(b)||"":""}
function Gg(a,b){return Fg(a,b)||(a.currentStyle?a.currentStyle[b]:null)||a.style&&a.style[b]}
function Hg(a){var b;try{b=a.getBoundingClientRect()}catch(c){return{left:0,top:0,right:0,bottom:0}}M&&a.ownerDocument.body&&(a=a.ownerDocument,b.left-=a.documentElement.clientLeft+a.body.clientLeft,b.top-=a.documentElement.clientTop+a.body.clientTop);return b}
function Ig(a,b){"number"==typeof a&&(a=(b?Math.round(a):a)+"px");return a}
function Jg(a){var b=Kg;if("none"!=Gg(a,"display"))return b(a);var c=a.style,d=c.display,e=c.visibility,f=c.position;c.visibility="hidden";c.position="absolute";c.display="inline";a=b(a);c.display=d;c.position=f;c.visibility=e;return a}
function Kg(a){var b=a.offsetWidth,c=a.offsetHeight,d=le&&!b&&!c;return p(b)&&!d||!a.getBoundingClientRect?new Gc(b,c):(a=Hg(a),new Gc(a.right-a.left,a.bottom-a.top))}
function Lg(a,b){if(/^\d+px?$/.test(b))return parseInt(b,10);var c=a.style.left,d=a.runtimeStyle.left;a.runtimeStyle.left=a.currentStyle.left;a.style.left=b;var e=a.style.pixelLeft;a.style.left=c;a.runtimeStyle.left=d;return+e}
function Mg(a,b){var c=a.currentStyle?a.currentStyle[b]:null;return c?Lg(a,c):0}
var Ng={thin:2,medium:4,thick:6};function Og(a,b){if("none"==(a.currentStyle?a.currentStyle[b+"Style"]:null))return 0;var c=a.currentStyle?a.currentStyle[b+"Width"]:null;return c in Ng?Ng[c]:Lg(a,c)}
;function Pg(a,b,c,d){C.call(this);this.i=b||null;this.G="*";this.j=c||null;this.b=null;this.channel=d||null;this.L=!!a;this.F=v(this.M,this);window.addEventListener("message",this.F)}
x(Pg,C);Pg.prototype.M=function(a){if(!("*"!=this.j&&a.origin!=this.j||this.i&&a.source!=this.i)&&t(a.data)){var b;try{b=yc(a.data)}catch(c){return}if(!(null==b||this.L&&(this.b&&this.b!=b.id||this.channel&&this.channel!=b.channel))&&b)switch(b.event){case "listening":"null"!=a.origin?this.j=this.G=a.origin:Ma(Error("MessageEvent origin is null"),"WARNING");this.i=a.source;this.b=b.id;this.f&&(this.f(),this.f=null);break;case "command":this.o&&(this.C&&!cb(this.C,b.func)||this.o(b.func,b.args))}}};
Pg.prototype.sendMessage=function(a,b){var c=b||this.i;if(c){this.b&&(a.id=this.b);this.channel&&(a.channel=this.channel);try{var d=Ac(a);c.postMessage(d,this.G)}catch(e){Ma(e,"WARNING")}}};
Pg.prototype.A=function(){window.removeEventListener("message",this.F);Pg.B.A.call(this)};function Qg(a,b,c){Pg.call(this,a,b,c||z("POST_MESSAGE_ORIGIN",void 0)||window.document.location.protocol+"//"+window.document.location.hostname,"widget");this.C=this.f=this.o=null}
x(Qg,Pg);function Rg(){var a=Bf();return a?a:null}
;function Sg(a){if(window.spf){var b=a.match(Tg);spf.style.load(a,b?b[1]:"",void 0)}else Ug(a)}
function Ug(a){var b=Vg(a),c=document.getElementById(b),d=c&&B(c,"loaded");d||c&&!d||(c=Wg(a,b,function(){B(c,"loaded")||(Pa(c,"loaded","true"),Ub(b),A(na(Wb,b),0))}))}
function Wg(a,b,c){var d=document.createElement("link");d.id=b;d.onload=function(){c&&setTimeout(c,0)};
a=Be(a);Jb(d,a);(document.getElementsByTagName("head")[0]||document.body).appendChild(d);return d}
function Vg(a){var b=document.createElement("a");Ib(b,a);a=b.href.replace(/^[a-zA-Z]+:\/\//,"//");return"css-"+Ga(a)}
var Tg=/cssbin\/(?:debug-)?([a-zA-Z0-9_-]+?)(?:-2x|-web|-rtl|-vfl|.css)/;var Xg={},Yg=0;function Zg(a,b){a&&(z("USE_NET_AJAX_FOR_PING_TRANSPORT",!1)?Qf(a,b):$g(a,b))}
function $g(a,b){var c=new Image,d=""+Yg++;Xg[d]=c;c.onload=c.onerror=function(){b&&Xg[d]&&b();delete Xg[d]};
c.src=a}
;function ah(){var a=za(bh);return new O(function(b,c){a.H=function(a){Uc(a)?b(a):c(new ch("Request failed, status="+a.status,"net.badstatus"))};
a.onError=function(){c(new ch("Unknown request error","net.unknown"))};
a.T=function(){c(new ch("Request timed out","net.timeout"))};
Uf("//googleads.g.doubleclick.net/pagead/id",a)})}
function ch(a,b){ra.call(this,a+", errorCode="+b);this.errorCode=b}
x(ch,ra);ch.prototype.name="PromiseAjaxError";var dh;var eh=D,eh=eh.toLowerCase();if(-1!=eh.indexOf("android")){var fh=eh.match(/android\D*(\d\.\d)[^\;|\)]*[\;\)]/);if(fh)dh=Number(fh[1]);else{var gh={cupcake:1.5,donut:1.6,eclair:2,froyo:2.2,gingerbread:2.3,honeycomb:3,"ice cream sandwich":4,jellybean:4.1},hh=[],ih=0,jh;for(jh in gh)hh[ih++]=jh;var kh=eh.match("("+hh.join("|")+")");dh=kh?gh[kh[0]]:0}}else dh=void 0;var lh=D,mh=lh.match(/\((BB10|PlayBook|BlackBerry);/);!mh||2>mh.length||lh.match(/Version\/(\d+\.\d+)/);D.match(/Mozilla\/[\d\.]+ \(Mobile;.* rv:([\d\.]+)\) Gecko\/[\d\.]+ Firefox\/[\d\.]+/);var nh;var oh=D,ph=oh.match(/\((iPad|iPhone|iPod)( Simulator)?;/);if(!ph||2>ph.length)nh=void 0;else{var qh=oh.match(/\((iPad|iPhone|iPod)( Simulator)?; (U; )?CPU (iPhone )?OS (\d+_\d)[_ ]/);nh=qh&&6==qh.length?Number(qh[5].replace("_",".")):0}0<=nh&&0<=D.search("Safari")&&D.search("Version");var rh=['video/mp4; codecs="avc1.42001E, mp4a.40.2"','video/webm; codecs="vp8.0, vorbis"'],sh=['audio/mp4; codecs="mp4a.40.2"'];M&&N("9");!le||N("528");ke&&N("1.9b")||M&&N("8")||ie&&N("9.5")||le&&N("528");ke&&!N("8")||M&&N("9");function th(a){C.call(this);this.b=[];this.f=a||this}
x(th,C);function uh(a,b,c,d){d=Ka(v(d,a.f));d={target:b,name:c,pa:d};b.addEventListener(c,d.pa,void 0);a.b.push(d)}
function vh(a){for(;a.b.length;){var b=a.b.pop();b.target.removeEventListener(b.name,b.pa)}}
th.prototype.A=function(){vh(this);th.B.A.call(this)};function Q(a,b){this.version=a;this.args=b}
function wh(a){if(!a.Ua){var b={};a.call(b);a.Ua=b.version}return a.Ua}
function xh(a,b){function c(){a.apply(this,b.args)}
if(!b.args||!b.version)throw Error("yt.pubsub2.Data.deserialize(): serializedData is incomplete.");var d;try{d=wh(a)}catch(e){}if(!d||b.version!=d)throw Error("yt.pubsub2.Data.deserialize(): serializedData version is incompatible.");c.prototype=a.prototype;try{return new c}catch(e){throw e.message="yt.pubsub2.Data.deserialize(): "+e.message,e;}}
function R(a,b){this.topic=a;this.b=b}
R.prototype.toString=function(){return this.topic};var yh=window.performance||window.mozPerformance||window.msPerformance||window.webkitPerformance||{};function zh(a){Q.call(this,1,arguments)}
x(zh,Q);var Ah=new R("timing-sent",zh);var Bh=r("yt.pubsub2.instance_")||new G;G.prototype.subscribe=G.prototype.subscribe;G.prototype.unsubscribeByKey=G.prototype.P;G.prototype.publish=G.prototype.N;G.prototype.clear=G.prototype.clear;q("yt.pubsub2.instance_",Bh,void 0);var Ch=r("yt.pubsub2.subscribedKeys_")||{};q("yt.pubsub2.subscribedKeys_",Ch,void 0);var Dh=r("yt.pubsub2.topicToKeys_")||{};q("yt.pubsub2.topicToKeys_",Dh,void 0);var Eh=r("yt.pubsub2.isAsync_")||{};q("yt.pubsub2.isAsync_",Eh,void 0);q("yt.pubsub2.skipSubKey_",null,void 0);
function S(a,b){var c=Fh();c&&c.publish.call(c,a.toString(),a,b)}
function T(a,b,c){var d=Fh();if(!d)return 0;var e=d.subscribe(a.toString(),function(d,g){if(!window.yt.pubsub2.skipSubKey_||window.yt.pubsub2.skipSubKey_!=e){var f=function(){if(Ch[e])try{if(g&&a instanceof R&&a!=d)try{g=xh(a.b,g)}catch(h){throw h.message="yt.pubsub2 cross-binary conversion error for "+a.toString()+": "+h.message,h;}b.call(c||window,g)}catch(h){Ma(h)}};
Eh[a.toString()]?r("yt.scheduler.instance")?nb(f,void 0):A(f,0):f()}});
Ch[e]=!0;Dh[a.toString()]||(Dh[a.toString()]=[]);Dh[a.toString()].push(e);return e}
function Gh(a){var b=Fh();b&&("number"==typeof a&&(a=[a]),F(a,function(a){b.unsubscribeByKey(a);delete Ch[a]}))}
function Fh(){return r("yt.pubsub2.instance_")}
;function Hh(a,b,c){C.call(this);this.b=a;this.j=b||0;this.f=c;this.i=v(this.mb,this)}
x(Hh,C);l=Hh.prototype;l.ba=0;l.A=function(){Hh.B.A.call(this);this.stop();delete this.b;delete this.f};
l.start=function(a){this.stop();var b=this.i;a=p(a)?a:this.j;if(!fa(b))if(b&&"function"==typeof b.handleEvent)b=v(b.handleEvent,b);else throw Error("Invalid listener argument");this.ba=2147483647<Number(a)?-1:n.setTimeout(b,a||0)};
l.stop=function(){this.isActive()&&n.clearTimeout(this.ba);this.ba=0};
l.isActive=function(){return 0!=this.ba};
l.mb=function(){this.ba=0;this.b&&this.b.call(this.f)};var Ih={vc:!0},Jh={ad_at:"adType",cpn:"clientPlaybackNonce",csn:"clientScreenNonce",yt_lt:"loadType",yt_ad:"isMonetized",yt_ad_pr:"prerollAllowed",yt_red:"isRedSubscriber",yt_vis:"isVisible",docid:"videoId",plid:"videoId"},Kh=["ei","cver"],Lh=["isMonetized","prerollAllowed","isRedSubscriber","isVisible"],Mh=v(yh.clearResourceTimings||yh.webkitClearResourceTimings||yh.mozClearResourceTimings||yh.msClearResourceTimings||yh.oClearResourceTimings||aa,yh);
function Nh(a,b){if(!b&&"_"!=a[0]){var c=a;yh.mark&&(0==c.lastIndexOf("mark_",0)||(c="mark_"+c),yh.mark(c))}var c=Oh(),d=b||Na();c[a]&&(c["_"+a]=c["_"+a]||[c[a]],c["_"+a].push(d));c[a]=d;(Ph()["tick_"+a]=b)||Na();Wc("csi_on_gel")?(c=Qh(),"_start"==a?kg("latencyActionBaselined",{clientActionNonce:c},eg,b):kg("latencyActionTicked",{tickName:a,clientActionNonce:c},eg,b),c=!0):c=!1;if(c=!c)c=!r("yt.timing.pingSent_");if(c&&(d=z("TIMING_ACTION",void 0),c=Oh(),r("yt.timing.ready_")&&d&&c._start&&Rh())){var d=
!0,e=z("TIMING_WAIT",[]);if(e.length)for(var f=0,g=e.length;f<g;++f)if(!(e[f]in c)){d=!1;break}d&&Sh()}}
function Th(){var a=Uh().info.yt_lt="hot_bg";Ph().info_yt_lt=a;if(Wc("csi_on_gel"))if("yt_lt"in Jh){var b={},c=Jh.yt_lt;cb(Lh,c)&&(a=!!a);b[c]=a;a=Qh();b.clientActionNonce=a;kg("latencyActionInfo",b,eg)}else"yt_lt"in Kh||Ma(Error("Unknown label yt_lt logged with GEL CSI."))}
function Rh(){var a=Oh();if(a.aft)return a.aft;for(var b=z("TIMING_AFT_KEYS",["ol"]),c=b.length,d=0;d<c;d++){var e=a[b[d]];if(e)return e}return NaN}
function Sh(){if(!Wc("csi_on_gel")){var a=Oh(),b=Uh().info,c=a._start,d;for(d in a)if(0==d.lastIndexOf("_",0)&&da(a[d])){var e=d.slice(1);if(e in Ih){var f=$a(a[d],function(a){return Math.round(a-c)});
b["all_"+e]=f.join()}delete a[d]}e=!!b.ap;if(f=r("yt.timing.reportbuilder_")){if(f=f(a,b,void 0))Vh(f,e),Wh(),Mh(),Xh(!1,void 0),y("PREVIOUS_ACTION",z("TIMING_ACTION")),y("TIMING_ACTION","")}else{var g=z("CSI_SERVICE_NAME","youtube"),f={v:2,s:g,action:z("TIMING_ACTION",void 0)},k=b.srt;void 0!==a.srt&&delete b.srt;if(b.h5jse){var h=window.location.protocol+r("ytplayer.config.assets.js");(h=yh.getEntriesByName?yh.getEntriesByName(h)[0]:null)?b.h5jse=Math.round(b.h5jse-h.responseEnd):delete b.h5jse}a.aft=
Rh();Yh()&&"youtube"==g&&(Th(),g=a.vc,h=a.pbs,delete a.aft,b.aft=Math.round(h-g));for(var m in b)"_"!=m.charAt(0)&&(f[m]=b[m]);a.ps=Na();b={};m=[];for(d in a)"_"!=d.charAt(0)&&(g=Math.round(a[d]-c),b[d]=g,m.push(d+"."+g));f.rt=m.join(",");(a=r("ytdebug.logTiming"))&&a(f,b);Vh(f,e,void 0);S(Ah,new zh(b.aft+(k||0)))}}}
function Vh(a,b,c){if(Wc("debug_csi_data")){var d=r("yt.timing.csiData");d||(d=[],q("yt.timing.csiData",d,void 0));d.push({page:location.href,time:new Date,args:a})}var d="",e;for(e in a)d+="&"+e+"="+a[e];a="/csi_204?"+d.substring(1);if(window.navigator&&window.navigator.sendBeacon&&b)try{window.navigator&&window.navigator.sendBeacon&&window.navigator.sendBeacon(a,"")||Zg(a,void 0)}catch(f){Zg(a,void 0)}else Zg(a);Xh(!0,c)}
function Qh(){var a=Uh().nonce;if(!a){var b;a:{if(window.crypto&&window.crypto.getRandomValues)try{var c=Array(16),d=new Uint8Array(16);window.crypto.getRandomValues(d);for(a=0;a<c.length;a++)c[a]=d[a];b=c;break a}catch(e){}b=Array(16);for(c=0;16>c;c++){d=w();for(a=0;a<d%23;a++)b[c]=Math.random();b[c]=Math.floor(256*Math.random())}if(sg)for(c=1,d=0;d<sg.length;d++)b[c%16]=b[c%16]^b[(c-1)%16]/4^sg.charCodeAt(d),c++}c=[];for(d=0;d<b.length;d++)c.push("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_".charAt(b[d]&
63));a=c.join("");Uh().nonce=a}return a}
function Oh(){return Uh().tick}
function Ph(){var a=Uh();"gel"in a||(a.gel={});return a.gel}
function Uh(){return r("ytcsi.data_")||Wh()}
function Wh(){var a={tick:{},info:{}};q("ytcsi.data_",a,void 0);return a}
function Xh(a,b){q("yt.timing."+(b||"")+"pingSent_",a,void 0)}
function Yh(){var a=Oh(),b=a.pbr,c=a.vc,a=a.pbs;return b&&c&&a&&b<c&&c<a&&1==Uh().info.yt_pvis}
;new Hh(Zh,1E3);function Zh(){Nh("vptl",0);Nh("vpl",0)}
;var $h={"api.invalidparam":2,auth:150,"drm.auth":150,"heartbeat.net":150,"heartbeat.servererror":150,"heartbeat.stop":150,"html5.unsupportedads":5,"fmt.noneavailable":5,"fmt.decode":5,"fmt.unplayable":5,"html5.missingapi":5,"html5.unsupportedlive":5,"drm.unavailable":5};function ai(a,b){C.call(this);this.C=this.o=a;this.Y=b;this.F=!1;this.f={};this.fa=this.X=null;this.Z=new G;Ta(this,na(Ua,this.Z));this.j={};this.L=this.ga=this.i=this.oa=this.b=null;this.ca=!1;this.M=this.G=this.V=this.W=null;this.ha={};this.fb=["onReady"];this.da=new th(this);Ta(this,na(Ua,this.da));this.ma=null;this.Ca=NaN;this.ea={};bi(this);this.K("onDetailedError",v(this.Bb,this));this.K("onTabOrderChange",v(this.jb,this));this.K("onTabAnnounce",v(this.Da,this));this.K("WATCH_LATER_VIDEO_ADDED",
v(this.Cb,this));this.K("WATCH_LATER_VIDEO_REMOVED",v(this.Db,this));Fe||(this.K("onMouseWheelCapture",v(this.zb,this)),this.K("onMouseWheelRelease",v(this.Ab,this)));this.K("onAdAnnounce",v(this.Da,this));this.R=new th(this);Ta(this,na(Ua,this.R));this.na=!1;this.la=null}
x(ai,C);var ci=["drm.unavailable","fmt.noneavailable","html5.missingapi","html5.unsupportedads","html5.unsupportedlive"];l=ai.prototype;l.ya=function(a,b){this.g||(di(this,a),ei(this,b),this.F&&fi(this))};
function di(a,b){a.oa=b;a.b=zg(b);a.i=a.b.attrs.id||a.i;"video-player"==a.i&&(a.i=a.Y,a.b.attrs.id=a.Y);a.C.id==a.i&&(a.i+="-player",a.b.attrs.id=a.i);a.b.args.enablejsapi="1";a.b.args.playerapiid=a.Y;a.ga||(a.ga=gi(a,a.b.args.jsapicallback||"onYouTubePlayerReady"));a.b.args.jsapicallback=null;var c=a.b.attrs.width;c&&(a.C.style.width=Ig(Number(c)||c,!0));if(c=a.b.attrs.height)a.C.style.height=Ig(Number(c)||c,!0)}
l.pb=function(){return this.oa};
function fi(a){a.b.loaded||(a.b.loaded=!0,"0"!=a.b.args.autoplay?a.f.loadVideoByPlayerVars(a.b.args):a.f.cueVideoByPlayerVars(a.b.args))}
function hi(a){if(!p(a.b.disable.flash)){var b=a.b.disable,c;c=Bg(Ag.getInstance(),a.b.minVersion);b.flash=!c}return!a.b.disable.flash}
function ii(a,b){if((!b||(5!=($h[b.errorCode]||5)?0:-1!=ci.indexOf(b.errorCode)))&&hi(a)){var c=ji(a);c&&c.stopVideo&&c.stopVideo();var d=a.b;c&&c.getUpdatedConfigurationData&&(c=c.getUpdatedConfigurationData(),d=yg(c));d.args.autoplay=1;d.args.html5_unavailable="1";di(a,d);ei(a,"flash")}}
function ei(a,b){if(!a.g){if(!b){var c;if(!(c=!a.b.html5&&hi(a))){if(!p(a.b.disable.html5)){var d;c=!0;void 0!=a.b.args.deviceHasDisplay&&(c=a.b.args.deviceHasDisplay);if(2.2==dh)d=!0;else{a:{var e=c;c=r("yt.player.utils.videoElement_");c||(c=document.createElement("VIDEO"),q("yt.player.utils.videoElement_",c,void 0));try{if(c.canPlayType)for(var e=e?rh:sh,f=0;f<e.length;f++)if(c.canPlayType(e[f])){d=null;break a}d="fmt.noneavailable"}catch(g){d="html5.missingapi"}}d=!d}d&&(d=ki(a)||a.b.assets.js);
a.b.disable.html5=!d;d||(a.b.args.html5_unavailable="1")}c=!!a.b.disable.html5}b=c?hi(a)?"flash":"unsupported":"html5"}("flash"==b?a.Tb:a.Ub).call(a)}}
function ki(a){var b=!0,c=ji(a);c&&a.b&&(a=a.b,b=B(c,"version")==a.assets.js);return b&&!!r("yt.player.Application.create")}
l.Ub=function(){if(!this.ca){var a=ki(this);a&&"html5"==li(this)?(this.L="html5",this.F||this.U()):(mi(this),this.L="html5",a&&this.V?(this.o.appendChild(this.V),this.U()):(this.b.loaded=!0,this.W=v(function(){var a=this.o,c=zg(this.b);r("yt.player.Application.create")(a,c);this.U()},this),this.ca=!0,a?this.W():(Xb(this.b.assets.js,this.W),Sg(this.b.assets.css))))}};
l.Tb=function(){var a=zg(this.b);if(!this.G){var b=ji(this);b&&(this.G=document.createElement("SPAN"),this.G.tabIndex=0,uh(this.da,this.G,"focus",this.Ia),this.M=document.createElement("SPAN"),this.M.tabIndex=0,uh(this.da,this.M,"focus",this.Ia),b.parentNode&&b.parentNode.insertBefore(this.G,b),b.parentNode&&b.parentNode.insertBefore(this.M,b.nextSibling))}a.attrs.width=a.attrs.width||"100%";a.attrs.height=a.attrs.height||"100%";if("flash"==li(this))this.L="flash",this.F||this.U();else{mi(this);this.L=
"flash";this.b.loaded=!0;var b=Ag.getInstance(),c=(-1<b.i.indexOf("Gnash")&&-1==b.i.indexOf("AVM2")||9==b.b&&1==b.g||9==b.b&&0==b.g&&1==b.f?0:9<=b.b)||-1<navigator.userAgent.indexOf("Sony/COM2")&&!Bg(b,9,1,58)?a.url:a.urlV9As2;window!=window.top&&document.referrer&&(a.args.framer=document.referrer.substring(0,128));b=this.o;if(c){var b=t(b)?Oe(b):b,d=za(a.attrs);d.tabindex=0;var e=za(a.params);e.flashvars=ld(a.args);if(Oa){d.classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000";e.movie=c;var a=document.createElement("object"),
f;for(f in d)a.setAttribute(f,d[f]);for(var g in e)f=document.createElement("param"),f.setAttribute("name",g),f.setAttribute("value",e[g]),a.appendChild(f)}else{d.type="application/x-shockwave-flash";d.src=c;a=document.createElement("embed");a.setAttribute("name",d.id);for(var k in d)a.setAttribute(k,d[k]);for(var h in e)a.setAttribute(h,e[h])}g=document.createElement("div");g.appendChild(a);b.innerHTML=g.innerHTML}this.U()}};
l.Ia=function(){ji(this).focus()};
function ji(a){var b=Oe(a.i);!b&&a.C&&a.C.querySelector&&(b=a.C.querySelector("#"+a.i));return b}
l.U=function(){if(!this.g){var a=ji(this),b=!1;try{a&&a.getApiInterface&&a.getApiInterface()&&(b=!0)}catch(f){}if(b)if(this.ca=!1,a.isNotServable&&a.isNotServable(this.b.args.video_id))ii(this);else{bi(this);this.F=!0;a=ji(this);a.addEventListener&&(this.X=ni(this,a,"addEventListener"));a.removeEventListener&&(this.fa=ni(this,a,"removeEventListener"));for(var b=a.getApiInterface(),b=b.concat(a.getInternalApiInterface()),c=0;c<b.length;c++){var d=b[c];this.f[d]||(this.f[d]=ni(this,a,d))}for(var e in this.j)this.X(e,
this.j[e]);fi(this);this.ga&&this.ga(this.f);this.Z.N("onReady",this.f)}else this.Ca=A(v(this.U,this),50)}};
function ni(a,b,c){var d=b[c];return function(){try{return a.ma=null,d.apply(b,arguments)}catch(e){"Bad NPObject as private data!"!=e.message&&"sendAbandonmentPing"!=c&&(e.message+=" ("+c+")",a.ma=e,Ma(e,"WARNING"))}}}
function bi(a){a.F=!1;if(a.fa)for(var b in a.j)a.fa(b,a.j[b]);for(var c in a.ea)La(parseInt(c,10));a.ea={};a.X=null;a.fa=null;for(var d in a.f)a.f[d]=null;a.f.addEventListener=v(a.K,a);a.f.removeEventListener=v(a.Lb,a);a.f.destroy=v(a.dispose,a);a.f.getLastError=v(a.qb,a);a.f.getPlayerType=v(a.rb,a);a.f.getCurrentVideoConfig=v(a.pb,a);a.f.loadNewVideoConfig=v(a.ya,a);a.f.isReady=v(a.Wb,a)}
l.Wb=function(){return this.F};
l.K=function(a,b){if(!this.g){var c=gi(this,b);if(c){if(!cb(this.fb,a)&&!this.j[a]){var d=oi(this,a);this.X&&this.X(a,d)}this.Z.subscribe(a,c);"onReady"==a&&this.F&&A(na(c,this.f),0)}}};
l.Lb=function(a,b){if(!this.g){var c=gi(this,b);c&&Kb(this.Z,a,c)}};
function gi(a,b){var c=b;if("string"==typeof b){if(a.ha[b])return a.ha[b];c=function(){var a=r(b);a&&a.apply(n,arguments)};
a.ha[b]=c}return c?c:null}
function oi(a,b){var c="ytPlayer"+b+a.Y;a.j[b]=c;n[c]=function(c){var d=A(function(){if(!a.g){a.Z.N(b,c);var e=a.ea,g=String(d);g in e&&delete e[g]}},0);
ya(a.ea,String(d))};
return c}
l.jb=function(a){a=a?We:Ve;for(var b=a(document.activeElement);b&&(1!=b.nodeType||b==this.G||b==this.M||(b.focus(),b!=document.activeElement));)b=a(b)};
l.Da=function(a){Ub("a11y-announce",a)};
l.Bb=function(a){ii(this,a)};
l.Cb=function(a){Ub("WATCH_LATER_VIDEO_ADDED",a)};
l.Db=function(a){Ub("WATCH_LATER_VIDEO_REMOVED",a)};
l.zb=function(){this.na||(Je?(this.la=Te(document),uh(this.R,window,"scroll",this.Ib),uh(this.R,this.o,"touchmove",this.Gb)):(uh(this.R,this.o,"mousewheel",this.La),uh(this.R,this.o,"wheel",this.La)),this.na=!0)};
l.Ab=function(){vh(this.R);this.na=!1};
l.La=function(a){a=a||window.event;a.returnValue=!1;a.preventDefault&&a.preventDefault()};
l.Ib=function(){window.scrollTo(this.la.l,this.la.w)};
l.Gb=function(a){a.preventDefault()};
l.rb=function(){return this.L||li(this)};
l.qb=function(){return this.ma};
function li(a){return(a=ji(a))?"div"==a.tagName.toLowerCase()?"html5":"flash":null}
function mi(a){Nh("dcp");a.cancel();bi(a);a.L=null;a.b&&(a.b.loaded=!1);var b=ji(a);"html5"==li(a)?a.V=b:b&&b.destroy&&b.destroy();Ue(a.o);vh(a.da);a.G=null;a.M=null}
l.cancel=function(){this.W&&dc(this.b.assets.js,this.W);La(this.Ca);this.ca=!1};
l.A=function(){mi(this);if(this.V&&this.b)try{this.V.destroy()}catch(b){Ma(b)}this.ha=null;for(var a in this.j)n[this.j[a]]=null;this.oa=this.b=this.f=null;delete this.o;delete this.C;ai.B.A.call(this)};var pi={},qi="player_uid_"+(1E9*Math.random()>>>0);function ri(a,b){a=t(a)?Oe(a):a;b=yg(b);var c=qi+"_"+ia(a),d=pi[c];if(d)return d.ya(b),d.f;d=new ai(a,c);pi[c]=d;Ub("player-added",d.f);Ta(d,na(si,d));A(function(){d.ya(b)},0);
return d.f}
function si(a){pi[a.Y]=null}
function ti(a){a=Oe(a);if(!a)return null;var b=qi+"_"+ia(a),c=pi[b];c||(c=new ai(a,b),pi[b]=c);return c.f}
;var ui=r("yt.abuse.botguardInitialized")||gc;q("yt.abuse.botguardInitialized",ui,void 0);var vi=r("yt.abuse.invokeBotguard")||hc;q("yt.abuse.invokeBotguard",vi,void 0);var wi=r("yt.abuse.dclkstatus.checkDclkStatus")||lc;q("yt.abuse.dclkstatus.checkDclkStatus",wi,void 0);var xi=r("yt.player.exports.navigate")||tg;q("yt.player.exports.navigate",xi,void 0);var yi=r("yt.player.embed")||ri;q("yt.player.embed",yi,void 0);var zi=r("yt.player.getPlayerByElement")||ti;q("yt.player.getPlayerByElement",zi,void 0);
var Ai=r("yt.util.activity.init")||fg;q("yt.util.activity.init",Ai,void 0);var Bi=r("yt.util.activity.getTimeSinceActive")||hg;q("yt.util.activity.getTimeSinceActive",Bi,void 0);var Ci=r("yt.util.activity.setTimestamp")||gg;q("yt.util.activity.setTimestamp",Ci,void 0);function Di(a){Q.call(this,1,arguments);this.b=a}
x(Di,Q);function U(a){Q.call(this,1,arguments);this.b=a}
x(U,Q);function Ei(a,b,c){Q.call(this,3,arguments);this.f=a;this.g=b;this.b=null!=c?!!c:null}
x(Ei,Q);function Fi(a,b,c,d,e){Q.call(this,2,arguments);this.g=a;this.b=b;this.i=c||null;this.f=d||null;this.source=e||null}
x(Fi,Q);function Gi(a,b,c){Q.call(this,1,arguments);this.b=a;this.subscriptionId=b}
x(Gi,Q);function Hi(a,b,c,d,e,f,g){Q.call(this,1,arguments);this.g=a;this.subscriptionId=b;this.b=c;this.j=d||null;this.i=e||null;this.f=f||null;this.source=g||null}
x(Hi,Q);
var Ii=new R("subscription-batch-subscribe",Di),Ji=new R("subscription-batch-unsubscribe",Di),Ki=new R("subscription-subscribe",Fi),Li=new R("subscription-subscribe-loading",U),Mi=new R("subscription-subscribe-loaded",U),Ni=new R("subscription-subscribe-success",Gi),Oi=new R("subscription-subscribe-external",Fi),Pi=new R("subscription-unsubscribe",Hi),Qi=new R("subscription-unsubscirbe-loading",U),Ri=new R("subscription-unsubscribe-loaded",U),Si=new R("subscription-unsubscribe-success",U),Ti=new R("subscription-external-unsubscribe",
Hi),Ui=new R("subscription-enable-ypc",U),Vi=new R("subscription-disable-ypc",U),Wi=new R("subscription-prefs",Ei),Xi=new R("subscription-prefs-success",Ei),Yi=new R("subscription-prefs-failure",Ei);function Zi(a,b){var c=document.location.protocol+"//"+document.domain+"/post_login";b&&(c=md(c,"mode",b));c=md("/signin?context=popup","next",c);c=md(c,"feature","sub_button");if(c=window.open(c,"loginPopup","width=375,height=440,resizable=yes,scrollbars=yes",!0)){var d=Rb("LOGGED_IN",function(b){Tb(z("LOGGED_IN_PUBSUB_KEY",void 0));y("LOGGED_IN",!0);a(b)});
y("LOGGED_IN_PUBSUB_KEY",d);c.moveTo((screen.width-375)/2,(screen.height-440)/2)}}
q("yt.pubsub.publish",Ub,void 0);function $i(){var a=z("PLAYER_CONFIG");return a&&a.args&&void 0!==a.args.authuser?!0:!(!z("SESSION_INDEX")&&!z("LOGGED_IN"))}
;function aj(a,b){(a=Oe(a))&&a.style&&(a.style.display=b?"":"none",yd(a,"hid",!b))}
function bj(a){F(arguments,function(a){!ea(a)||a instanceof Element?aj(a,!0):F(a,function(a){bj(a)})})}
function cj(a){F(arguments,function(a){!ea(a)||a instanceof Element?aj(a,!1):F(a,function(a){cj(a)})})}
;var dj={},ej="ontouchstart"in document;function fj(a,b,c){var d;switch(a){case "mouseover":case "mouseout":d=3;break;case "mouseenter":case "mouseleave":d=9}return df(c,function(a){return vd(a,b)},!0,d)}
function V(a){var b="mouseover"==a.type&&"mouseenter"in dj||"mouseout"==a.type&&"mouseleave"in dj,c=a.type in dj||b;if("HTML"!=a.target.tagName&&c){if(b){var b="mouseover"==a.type?"mouseenter":"mouseleave",c=dj[b],d;for(d in c.f){var e=fj(b,d,a.target);e&&!df(a.relatedTarget,function(a){return a==e},!0)&&c.N(d,e,b,a)}}if(b=dj[a.type])for(d in b.f)(e=fj(a.type,d,a.target))&&b.N(d,e,a.type,a)}}
P(document,"blur",V,!0);P(document,"change",V,!0);P(document,"click",V);P(document,"focus",V,!0);P(document,"mouseover",V);P(document,"mouseout",V);P(document,"mousedown",V);P(document,"keydown",V);P(document,"keyup",V);P(document,"keypress",V);P(document,"cut",V);P(document,"paste",V);ej&&(P(document,"touchstart",V),P(document,"touchend",V),P(document,"touchcancel",V));function gj(a){this.j=a;this.f={};this.ja=[];this.i=[]}
function W(a,b){return"yt-uix"+(a.j?"-"+a.j:"")+(b?"-"+b:"")}
gj.prototype.unregister=function(){Tb(this.ja);this.ja.length=0;Gh(this.i);this.i.length=0};
gj.prototype.init=aa;gj.prototype.dispose=aa;function hj(a,b,c){a.i.push(T(b,c,a))}
function ij(a,b,c){var d=W(a,void 0),e=v(c,a);b in dj||(dj[b]=new G);dj[b].subscribe(d,e);a.f[c]=e}
function jj(a,b,c){if(b in dj){var d=dj[b];Kb(d,W(a,void 0),a.f[c]);0>=d.aa()&&(d.dispose(),delete dj[b])}delete a.f[c]}
function kj(a,b){Pa(a,"tooltip-text",b)}
;function lj(){gj.call(this,"tooltip");this.b=0;this.g={}}
x(lj,gj);ba(lj);l=lj.prototype;l.register=function(){ij(this,"mouseover",this.ia);ij(this,"mouseout",this.O);ij(this,"focus",this.Ha);ij(this,"blur",this.Fa);ij(this,"click",this.O);ij(this,"touchstart",this.Ta);ij(this,"touchend",this.ka);ij(this,"touchcancel",this.ka)};
l.unregister=function(){jj(this,"mouseover",this.ia);jj(this,"mouseout",this.O);jj(this,"focus",this.Ha);jj(this,"blur",this.Fa);jj(this,"click",this.O);jj(this,"touchstart",this.Ta);jj(this,"touchend",this.ka);jj(this,"touchcancel",this.ka);this.dispose();lj.B.unregister.call(this)};
l.dispose=function(){for(var a in this.g)this.O(this.g[a]);this.g={}};
l.ia=function(a){if(!(this.b&&1E3>w()-this.b)){var b=parseInt(B(a,"tooltip-hide-timer"),10);b&&(Ra(a,"tooltip-hide-timer"),La(b));var b=v(function(){mj(this,a);Ra(a,"tooltip-show-timer")},this),c=parseInt(B(a,"tooltip-show-delay"),10)||0,b=A(b,c);
Pa(a,"tooltip-show-timer",b.toString());a.title&&(kj(a,nj(a)),a.title="");b=ia(a).toString();this.g[b]=a}};
l.O=function(a){var b=parseInt(B(a,"tooltip-show-timer"),10);b&&(La(b),Ra(a,"tooltip-show-timer"));b=v(function(){if(a){var b=Oe(oj(this,a));b&&(pj(b),b&&b.parentNode&&b.parentNode.removeChild(b),Ra(a,"content-id"));(b=Oe(oj(this,a,"arialabel")))&&b.parentNode&&b.parentNode.removeChild(b)}Ra(a,"tooltip-hide-timer")},this);
b=A(b,50);Pa(a,"tooltip-hide-timer",b.toString());if(b=B(a,"tooltip-text"))a.title=b;b=ia(a).toString();delete this.g[b]};
l.Ha=function(a){this.b=0;this.ia(a)};
l.Fa=function(a){this.b=0;this.O(a)};
l.Ta=function(a,b,c){c.changedTouches&&(this.b=0,(a=fj(b,W(this),c.changedTouches[0].target))&&this.ia(a))};
l.ka=function(a,b,c){c.changedTouches&&(this.b=w(),(a=fj(b,W(this),c.changedTouches[0].target))&&this.O(a))};
function qj(a,b){kj(a,b);var c=B(a,"content-id");(c=Oe(c))&&Xe(c,b)}
function nj(a){return B(a,"tooltip-text")||a.title}
function mj(a,b){if(b){var c=nj(b);if(c){var d=Oe(oj(a,b));if(!d){d=document.createElement("div");d.id=oj(a,b);d.className=W(a,"tip");var e=document.createElement("div");e.className=W(a,"tip-body");var f=document.createElement("div");f.className=W(a,"tip-arrow");var g=document.createElement("div");g.setAttribute("aria-hidden","true");g.className=W(a,"tip-content");var k=rj(a,b),h=oj(a,b,"content");g.id=h;Pa(b,"content-id",h);e.appendChild(g);k&&d.appendChild(k);d.appendChild(e);d.appendChild(f);var m=
$e(b),h=oj(a,b,"arialabel"),f=document.createElement("div");wd(f,W(a,"arialabel"));f.id=h;m=b.hasAttribute("aria-label")?b.getAttribute("aria-label"):"rtl"==document.body.getAttribute("dir")?c+" "+m:m+" "+c;Xe(f,m);b.setAttribute("aria-labelledby",h);h=Rg()||document.body;h.appendChild(f);h.appendChild(d);qj(b,c);(c=parseInt(B(b,"tooltip-max-width"),10))&&e.offsetWidth>c&&(e.style.width=c+"px",wd(g,W(a,"normal-wrap")));g=vd(b,W(a,"reverse"));sj(a,b,d,e,k,g)||sj(a,b,d,e,k,!g);var u=W(a,"tip-visible");
A(function(){wd(d,u)},0)}}}}
function sj(a,b,c,d,e,f){var g;yd(c,W(a,"tip-reverse"),f);var k=0;f&&(k=1);a=Jg(b);f=new L((a.width-10)/2,f?a.height:0);var h=Ne(b);g=new L(0,0);var m;m=h?Ne(h):document;m=!M||9<=Number(ye)||Se(Le(m).b)?m.documentElement:m.body;b!=m&&(m=Hg(b),h=Te(Le(h).b),g.l=m.left+h.l,g.w=m.top+h.w);f=new L(g.l+f.l,g.w+f.w);f=new L(f.l,f.w);g=(k&8&&"rtl"==Gg(c,"direction")?k^4:k)&-9;k=Jg(c);h=new Gc(k.width,k.height);f=new L(f.l,f.w);h=new Gc(h.width,h.height);0!=g&&(g&4?f.l-=h.width+0:g&2&&(f.l-=h.width/2),g&
1&&(f.w-=h.height+0));g=new Eg(0,0,0,0);g.left=f.l;g.top=f.w;g.width=h.width;g.height=h.height;f=g;g=0;if(!(g&496||(g=f,h=new L(g.left,g.top),h instanceof L?(g=h.l,h=h.w):(g=h,h=void 0),c.style.left=Ig(g,!1),c.style.top=Ig(h,!1),h=new Gc(f.width,f.height),k==h||k&&h&&k.width==h.width&&k.height==h.height)))if(k=h,g=Se(Le(Ne(c)).b),!M||N("10")||g&&N("8"))f=c.style,ke?f.MozBoxSizing="border-box":le?f.WebkitBoxSizing="border-box":f.boxSizing="border-box",f.width=Math.max(k.width,0)+"px",f.height=Math.max(k.height,
0)+"px";else if(f=c.style,g){if(M){g=Mg(c,"paddingLeft");h=Mg(c,"paddingRight");m=Mg(c,"paddingTop");var u=Mg(c,"paddingBottom");g=new Dg(m,h,u,g)}else g=Fg(c,"paddingLeft"),h=Fg(c,"paddingRight"),m=Fg(c,"paddingTop"),u=Fg(c,"paddingBottom"),g=new Dg(parseFloat(m),parseFloat(h),parseFloat(u),parseFloat(g));if(!M||9<=Number(ye))h=Fg(c,"borderLeftWidth"),m=Fg(c,"borderRightWidth"),u=Fg(c,"borderTopWidth"),Z=Fg(c,"borderBottomWidth"),h=new Dg(parseFloat(u),parseFloat(m),parseFloat(Z),parseFloat(h));
else{h=Og(c,"borderLeft");m=Og(c,"borderRight");var u=Og(c,"borderTop"),Z=Og(c,"borderBottom"),h=new Dg(u,m,Z,h)}f.pixelWidth=k.width-h.left-g.left-g.right-h.right;f.pixelHeight=k.height-h.top-g.top-g.bottom-h.bottom}else f.pixelWidth=k.width,f.pixelHeight=k.height;f=Re(window);1==c.nodeType?(c=Hg(c),h=new L(c.left,c.top)):(c=c.changedTouches?c.changedTouches[0]:c,h=new L(c.clientX,c.clientY));c=Jg(d);m=Math.floor(c.width/2);k=!!(f.height<h.w+a.height);a=!!(h.w<a.height);g=!!(h.l<m);f=!!(f.width<
h.l+m);h=(c.width+3)/-2- -5;b=B(b,"force-tooltip-direction");if("left"==b||g)h=-5;else if("right"==b||f)h=20-c.width-3;b=Math.floor(h)+"px";d.style.left=b;e&&(e.style.left=b,e.style.height=c.height+"px",e.style.width=c.width+"px");return!(k||a)}
function oj(a,b,c){a=W(a);var d=b.__yt_uid_key;d||(d=zf(),b.__yt_uid_key=d);b=a+d;c&&(b+="-"+c);return b}
function rj(a,b){var c=null;ne&&vd(b,W(a,"masked"))&&((c=Oe("yt-uix-tooltip-shared-mask"))?(c.parentNode.removeChild(c),bj(c)):(c=document.createElement("iframe"),c.src='javascript:""',c.id="yt-uix-tooltip-shared-mask",c.className=W(a,"tip-mask")));return c}
function pj(a){var b=Oe("yt-uix-tooltip-shared-mask"),c=b&&df(b,function(b){return b==a},!1,2);
b&&c&&(b.parentNode.removeChild(b),cj(b),document.body.appendChild(b))}
;function tj(){gj.call(this,"subscription-button")}
x(tj,gj);ba(tj);tj.prototype.register=function(){ij(this,"click",this.qa);hj(this,Li,this.Ka);hj(this,Mi,this.Ja);hj(this,Ni,this.Fb);hj(this,Qi,this.Ka);hj(this,Ri,this.Ja);hj(this,Si,this.Hb);hj(this,Ui,this.yb);hj(this,Vi,this.xb)};
tj.prototype.unregister=function(){jj(this,"click",this.qa);tj.B.unregister.call(this)};
var cf={za:"hover-enabled",Xa:"yt-uix-button-subscribe",Ya:"yt-uix-button-subscribed",Xb:"ypc-enabled",Za:"yt-uix-button-subscription-container",$a:"yt-subscription-button-disabled-mask-container"},uj={Yb:"channel-external-id",ab:"subscriber-count-show-when-subscribed",bb:"subscriber-count-tooltip",cb:"subscriber-count-title",Zb:"href",$b:"insecure",Aa:"is-subscribed",ac:"parent-url",cc:"clicktracking",eb:"style-type",Ba:"subscription-id",dc:"target",gb:"ypc-enabled"};l=tj.prototype;
l.qa=function(a){var b=B(a,"href"),c=B(a,"insecure"),d=$i(),c=c&&!0;if(b)a=B(a,"target")||"_self",window.open(b,a);else if(!c)if(d){b=B(a,"channel-external-id");d=B(a,"clicktracking");if(B(a,"ypc-enabled"))var c=B(a,"ypc-item-type"),e=B(a,"ypc-item-id"),c={itemType:c,itemId:e,subscriptionElement:a};else c=null;e=B(a,"parent-url");if(B(a,"is-subscribed")){var f=B(a,"subscription-id");S(Pi,new Hi(b,f,c,a,d,e))}else S(Ki,new Fi(b,c,d,e))}else vj(this,a)};
l.Ka=function(a){this.S(a.b,this.Ra,!0)};
l.Ja=function(a){this.S(a.b,this.Ra,!1)};
l.Fb=function(a){this.S(a.b,this.Sa,!0,a.subscriptionId)};
l.Hb=function(a){this.S(a.b,this.Sa,!1)};
l.yb=function(a){this.S(a.b,this.nb)};
l.xb=function(a){this.S(a.b,this.lb)};
l.Sa=function(a,b,c){b?(Pa(a,uj.Aa,"true"),c&&Pa(a,uj.Ba,c)):(Ra(a,uj.Aa),Ra(a,uj.Ba));wj(a)};
l.Ra=function(a,b){var c;c=bf(a);yd(c,cf.$a,b);a.setAttribute("aria-busy",b?"true":"false");a.disabled=b};
function wj(a){var b=B(a,uj.eb),c=!!B(a,"is-subscribed"),b="-"+b,d=cf.Ya+b;yd(a,cf.Xa+b,!c);yd(a,d,c);B(a,uj.bb)&&!B(a,uj.ab)&&(b=W(lj.getInstance()),yd(a,b,!c),a.title=c?"":B(a,uj.cb));c?A(function(){wd(a,cf.za)},1E3):xd(a,cf.za)}
l.nb=function(a){var b=!!B(a,"ypc-item-type"),c=!!B(a,"ypc-item-id");!B(a,"ypc-enabled")&&b&&c&&(wd(a,"ypc-enabled"),Pa(a,uj.gb,"true"))};
l.lb=function(a){B(a,"ypc-enabled")&&(xd(a,"ypc-enabled"),Ra(a,"ypc-enabled"))};
function xj(a,b){return Za(Pe(W(a)),function(a){return b==B(a,"channel-external-id")},a)}
l.ib=function(a,b,c){var d=jb(arguments,2);F(a,function(a){b.apply(this,eb(a,d))},this)};
l.S=function(a,b,c){var d=xj(this,a);this.ib.apply(this,eb([d],jb(arguments,1)))};
function vj(a,b){var c=v(function(a){a.discoverable_subscriptions&&y("SUBSCRIBE_EMBED_DISCOVERABLE_SUBSCRIPTIONS",a.discoverable_subscriptions);this.qa(b)},a);
Zi(c,"subscribe")}
;var yj=window.yt&&window.yt.uix&&window.yt.uix.widgets_||{};q("yt.uix.widgets_",yj,void 0);function zj(a){return(0==a.search("cue")||0==a.search("load"))&&"loadModule"!=a}
function Aj(a,b,c){t(a)&&(a={mediaContentUrl:a,startSeconds:b,suggestedQuality:c});b=/\/([ve]|embed)\/([^#?]+)/.exec(a.mediaContentUrl);a.videoId=b&&b[2]?b[2]:null;return Bj(a)}
function Bj(a,b,c){if(ga(a)){b="endSeconds startSeconds mediaContentUrl suggestedQuality videoId two_stage_token".split(" ");c={};for(var d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}return{videoId:a,startSeconds:b,suggestedQuality:c}}
function Cj(a,b,c,d){if(ga(a)&&!da(a)){b="playlist list listType index startSeconds suggestedQuality".split(" ");c={};for(d=0;d<b.length;d++){var e=b[d];a[e]&&(c[e]=a[e])}return c}c={index:b,startSeconds:c,suggestedQuality:d};t(a)&&16==a.length?c.list="PL"+a:c.playlist=a;return c}
function Dj(a){var b=a.video_id||a.videoId;if(t(b)){var c=$f()||{},d=$f()||{};p(void 0)?d[b]=void 0:delete d[b];var e=w()+3E5,f=bg;if(f&&window.JSON){t(d)||(d=JSON.stringify(d,void 0));try{f.set("yt-player-two-stage-token",d,e)}catch(g){f.remove("yt-player-two-stage-token")}}(b=c[b])&&(a.two_stage_token=b)}}
;var Ej=null,Fj=[];function Gj(a){return{externalChannelId:a.externalChannelId,wb:!!a.isChannelPaid,source:a.source,subscriptionId:a.subscriptionId}}
function Hj(a){a&&a.externalChannelId&&Ij(Gj(a))}
function Ij(a){$i()?(S(Ki,new Fi(a.externalChannelId,a.wb?{itemType:"U",itemId:a.externalChannelId}:null)),a=ld({event:"subscribe",source:a.source}),Zg("/gen_204?"+a,void 0)):Jj(a)}
function Jj(a){Zi(function(b){b.subscription_ajax&&Ij(a)},null)}
function Kj(a){a=Gj(a);S(Pi,new Hi(a.externalChannelId,a.subscriptionId,null));a=ld({event:"unsubscribe",source:a.source});Zg("/gen_204?"+a,void 0)}
function Lj(a){Ej&&Ej.channelSubscribed(a.b,a.subscriptionId)}
function Mj(a){Ej&&Ej.channelUnsubscribed(a.b)}
;function Nj(a){C.call(this);this.f=a;this.f.subscribe("command",this.Oa,this);this.i={};this.j=!1}
x(Nj,C);l=Nj.prototype;l.start=function(){this.j||this.g||(this.j=!0,Oj(this.f,"RECEIVING"))};
l.Oa=function(a,b){if(this.j&&!this.g){var c=b||{};switch(a){case "addEventListener":if(t(c.event)&&(c=c.event,!(c in this.i))){var d=v(this.Nb,this,c);this.i[c]=d;this.addEventListener(c,d)}break;case "removeEventListener":t(c.event)&&Pj(this,c.event);break;default:this.b.isReady()&&this.b[a]&&(c=Qj(a,b||{}),c=this.b[a].apply(this.b,c),(c=Rj(a,c))&&this.j&&!this.g&&Oj(this.f,a,c))}}};
l.Nb=function(a,b){this.j&&!this.g&&Oj(this.f,a,this.ra(a,b))};
l.ra=function(a,b){if(null!=b)return{value:b}};
function Pj(a,b){b in a.i&&(a.removeEventListener(b,a.i[b]),delete a.i[b])}
l.A=function(){var a=this.f;a.g||Kb(a.b,"command",this.Oa,this);this.f=null;for(var b in this.i)Pj(this,b);Nj.B.A.call(this)};new G;function Sj(a,b,c){Cg.call(this);this.f=a;this.i=b;this.o=c}
x(Sj,Cg);function Oj(a,b,c){if(!a.g){var d=a.f;d.g||a.i!=d.b||(a={id:a.o,command:b},c&&(a.data=c),d.b.postMessage(Ac(a),d.i))}}
Sj.prototype.A=function(){this.i=this.f=null;Sj.B.A.call(this)};function Tj(){var a=this.g=new Qg(!!z("WIDGET_ID_ENFORCE")),b=v(this.Kb,this);a.o=b;a.C=null;this.g.channel="widget";if(a=z("WIDGET_ID"))this.g.b=a;this.i=[];this.o=!1;this.j={}}
l=Tj.prototype;l.Kb=function(a,b){if("addEventListener"==a&&b){var c=b[0];this.j[c]||"onReady"==c||(this.addEventListener(c,Uj(this,c)),this.j[c]=!0)}else this.Va(a,b)};
l.Va=function(){};
function Uj(a,b){return v(function(a){this.sendMessage(b,a)},a)}
l.addEventListener=function(){};
l.ob=function(){this.o=!0;this.sendMessage("initialDelivery",this.sa());this.sendMessage("onReady");F(this.i,this.Qa,this);this.i=[]};
l.sa=function(){return null};
function Vj(a,b){a.sendMessage("infoDelivery",b)}
l.Qa=function(a){this.o?this.g.sendMessage(a):this.i.push(a)};
l.sendMessage=function(a,b){this.Qa({event:a,info:void 0==b?null:b})};
l.dispose=function(){this.g=null};function Wj(a,b,c){C.call(this);this.b=a;this.i=c;this.j=P(window,"message",v(this.o,this));this.f=new Sj(this,a,b);Ta(this,na(Ua,this.f))}
x(Wj,C);Wj.prototype.o=function(a){var b;if(b=!this.g)if(b=a.origin==this.i)a:{b=this.b;do{var c;b:{c=a.source;do{if(c==b){c=!0;break b}if(c==c.parent)break;c=c.parent}while(null!=c);c=!1}if(c){b=!0;break a}b=b.opener}while(null!=b);b=!1}if(b&&(a=a.data,t(a))){try{a=yc(a)}catch(d){return}a.command&&(b=this.f,b.g||b.j("command",a.command,a.data))}};
Wj.prototype.A=function(){If(this.j);this.b=null;Wj.B.A.call(this)};function Xj(a,b){Nj.call(this,b);this.b=a;this.start()}
x(Xj,Nj);Xj.prototype.addEventListener=function(a,b){this.b.addEventListener(a,b)};
Xj.prototype.removeEventListener=function(a,b){this.b.removeEventListener(a,b)};
function Qj(a,b){switch(a){case "loadVideoById":return b=Bj(b),Dj(b),[b];case "cueVideoById":return b=Bj(b),Dj(b),[b];case "loadVideoByPlayerVars":return Dj(b),[b];case "cueVideoByPlayerVars":return Dj(b),[b];case "loadPlaylist":return b=Cj(b),Dj(b),[b];case "cuePlaylist":return b=Cj(b),Dj(b),[b];case "seekTo":return[b.seconds,b.allowSeekAhead];case "playVideoAt":return[b.index];case "setVolume":return[b.volume];case "setPlaybackQuality":return[b.suggestedQuality];case "setPlaybackRate":return[b.suggestedRate];
case "setLoop":return[b.loopPlaylists];case "setShuffle":return[b.shufflePlaylist];case "getOptions":return[b.module];case "getOption":return[b.module,b.option];case "setOption":return[b.module,b.option,b.value];case "handleGlobalKeyDown":return[b.keyCode,b.shiftKey]}return[]}
function Rj(a,b){switch(a){case "isMuted":return{muted:b};case "getVolume":return{volume:b};case "getPlaybackRate":return{playbackRate:b};case "getAvailablePlaybackRates":return{availablePlaybackRates:b};case "getVideoLoadedFraction":return{videoLoadedFraction:b};case "getPlayerState":return{playerState:b};case "getCurrentTime":return{currentTime:b};case "getPlaybackQuality":return{playbackQuality:b};case "getAvailableQualityLevels":return{availableQualityLevels:b};case "getDuration":return{duration:b};
case "getVideoUrl":return{videoUrl:b};case "getVideoEmbedCode":return{videoEmbedCode:b};case "getPlaylist":return{playlist:b};case "getPlaylistIndex":return{playlistIndex:b};case "getOptions":return{options:b};case "getOption":return{option:b}}}
Xj.prototype.ra=function(a,b){switch(a){case "onReady":return;case "onStateChange":return{playerState:b};case "onPlaybackQualityChange":return{playbackQuality:b};case "onPlaybackRateChange":return{playbackRate:b};case "onError":return{errorCode:b}}return Xj.B.ra.call(this,a,b)};
Xj.prototype.A=function(){Xj.B.A.call(this);delete this.b};function Yj(a){Tj.call(this);this.b=a;this.f=[];this.addEventListener("onReady",v(this.Eb,this));this.addEventListener("onVideoProgress",v(this.Rb,this));this.addEventListener("onVolumeChange",v(this.Sb,this));this.addEventListener("onApiChange",v(this.Mb,this));this.addEventListener("onPlaybackQualityChange",v(this.Ob,this));this.addEventListener("onPlaybackRateChange",v(this.Pb,this));this.addEventListener("onStateChange",v(this.Qb,this))}
x(Yj,Tj);l=Yj.prototype;l.Va=function(a,b){if(this.b[a]){b=b||[];if(0<b.length&&zj(a)){var c;c=b;if(ga(c[0])&&!da(c[0]))c=c[0];else{var d={};switch(a){case "loadVideoById":case "cueVideoById":d=Bj.apply(window,c);break;case "loadVideoByUrl":case "cueVideoByUrl":d=Aj.apply(window,c);break;case "loadPlaylist":case "cuePlaylist":d=Cj.apply(window,c)}c=d}Dj(c);b.length=1;b[0]=c}this.b[a].apply(this.b,b);zj(a)&&Vj(this,this.sa())}};
l.Eb=function(){var a=v(this.ob,this);this.g.f=a};
l.addEventListener=function(a,b){this.f.push({eventType:a,listener:b});this.b.addEventListener(a,b)};
l.sa=function(){if(!this.b)return null;var a=this.b.getApiInterface();db(a,"getVideoData");for(var b={apiInterface:a},c=0,d=a.length;c<d;c++){var e=a[c],f=e;if(0==f.search("get")||0==f.search("is")){var f=e,g=0;0==f.search("get")?g=3:0==f.search("is")&&(g=2);f=f.charAt(g).toLowerCase()+f.substr(g+1);try{var k=this.b[e]();b[f]=k}catch(h){}}}b.videoData=this.b.getVideoData();b.currentTimeLastUpdated_=w()/1E3;return b};
l.Qb=function(a){a={playerState:a,currentTime:this.b.getCurrentTime(),duration:this.b.getDuration(),videoData:this.b.getVideoData(),videoStartBytes:0,videoBytesTotal:this.b.getVideoBytesTotal(),videoLoadedFraction:this.b.getVideoLoadedFraction(),playbackQuality:this.b.getPlaybackQuality(),availableQualityLevels:this.b.getAvailableQualityLevels(),videoUrl:this.b.getVideoUrl(),playlist:this.b.getPlaylist(),playlistIndex:this.b.getPlaylistIndex(),currentTimeLastUpdated_:w()/1E3,playbackRate:this.b.getPlaybackRate(),
mediaReferenceTime:this.b.getMediaReferenceTime()};this.b.getProgressState&&(a.progressState=this.b.getProgressState());this.b.getStoryboardFormat&&(a.storyboardFormat=this.b.getStoryboardFormat());Vj(this,a)};
l.Ob=function(a){Vj(this,{playbackQuality:a})};
l.Pb=function(a){Vj(this,{playbackRate:a})};
l.Mb=function(){for(var a=this.b.getOptions(),b={namespaces:a},c=0,d=a.length;c<d;c++){var e=a[c],f=this.b.getOptions(e);b[e]={options:f};for(var g=0,k=f.length;g<k;g++){var h=f[g],m=this.b.getOption(e,h);b[e][h]=m}}this.sendMessage("apiInfoDelivery",b)};
l.Sb=function(){Vj(this,{muted:this.b.isMuted(),volume:this.b.getVolume()})};
l.Rb=function(a){a={currentTime:a,videoBytesLoaded:this.b.getVideoBytesLoaded(),videoLoadedFraction:this.b.getVideoLoadedFraction(),currentTimeLastUpdated_:w()/1E3,playbackRate:this.b.getPlaybackRate(),mediaReferenceTime:this.b.getMediaReferenceTime()};this.b.getProgressState&&(a.progressState=this.b.getProgressState());Vj(this,a)};
l.dispose=function(){Yj.B.dispose.call(this);for(var a=0;a<this.f.length;a++){var b=this.f[a];this.b.removeEventListener(b.eventType,b.listener)}this.f=[]};var Zj=document,X=window;var ak=!1,bk="";function ck(a){a=a.match(/[\d]+/g);if(!a)return"";a.length=3;return a.join(".")}
(function(){if(navigator.plugins&&navigator.plugins.length){var a=navigator.plugins["Shockwave Flash"];if(a&&(ak=!0,a.description)){bk=ck(a.description);return}if(navigator.plugins["Shockwave Flash 2.0"]){ak=!0;bk="2.0.0.11";return}}if(navigator.mimeTypes&&navigator.mimeTypes.length&&(a=navigator.mimeTypes["application/x-shockwave-flash"],ak=!(!a||!a.enabledPlugin))){bk=ck(a.enabledPlugin.description);return}try{var b=new ActiveXObject("ShockwaveFlash.ShockwaveFlash.7");ak=!0;bk=ck(b.GetVariable("$version"));
return}catch(c){}try{b=new ActiveXObject("ShockwaveFlash.ShockwaveFlash.6");ak=!0;bk="6.0.21";return}catch(c){}try{b=new ActiveXObject("ShockwaveFlash.ShockwaveFlash"),ak=!0,bk=ck(b.GetVariable("$version"))}catch(c){}})();
var dk=ak,ek=bk;(function(){var a;return ne?(a=/Windows NT ([0-9.]+)/,(a=a.exec(D))?a[1]:"0"):me?(a=/10[_.][0-9_.]+/,(a=a.exec(D))?a[0].replace(/_/g,"."):"10"):oe?(a=/Android\s+([^\);]+)(\)|;)/,(a=a.exec(D))?a[1]:""):pe||qe||re?(a=/(?:iPhone|CPU)\s+OS\s+(\S+)/,(a=a.exec(D))?a[1].replace(/_/g,"."):""):""})();function fk(a){return(a=a.exec(D))?a[1]:""}
(function(){if(Fe)return fk(/Firefox\/([0-9.]+)/);if(M||je||ie)return xe;if(Je)return fk(/Chrome\/([0-9.]+)/);if(Ke&&!(bd()||E("iPad")||E("iPod")))return fk(/Version\/([0-9.]+)/);if(Ge||He){var a=/Version\/(\S+).*Mobile\/(\S+)/.exec(D);if(a)return a[1]+"."+a[2]}else if(Ie)return(a=fk(/Android\s+([0-9.]+)/))?a:fk(/Version\/([0-9.]+)/);return""})();(function(){var a=!1;try{var b=Object.defineProperty({},"passive",{get:function(){a=!0}});
n.addEventListener("test",null,b)}catch(c){}return a})();var gk=(new Date).getTime();function hk(a){ra.call(this,a.message||a.description||a.name);this.b=a instanceof mf}
x(hk,ra);hk.prototype.name="BiscottiError";function ik(a,b){this.g=a;this.b=b}
ik.prototype.then=function(a,b,c){try{if(p(this.g))return a?jf(a.call(c,this.g)):jf(this.g);if(p(this.b)){if(!b)return kf(this.b);var d=b.call(c,this.b);return!p(d)&&this.b.b?kf(this.b):jf(d)}throw Error("Invalid Result_ state");}catch(e){return kf(e)}};
Kc(ik);var bh={format:"RAW",method:"GET",timeout:5E3,withCredentials:!0},jk=null;function kk(a){a=a.responseText;if(0!=a.lastIndexOf(")]}'",0))return lk(""),jk=new ik(""),"";a=JSON.parse(a.substr(4)).id;lk(a);jk=new ik(a);mk(18E5,2);return a}
function nk(a,b){var c=new hk(b);lk("");jk=new ik(void 0,c);0<a&&mk(12E4,a-1);throw c;}
function mk(a,b){A(function(){var a=v(nk,n,b),a=ah().then(kk,a);lf(a,null,aa,void 0)},a)}
function lk(a){q("yt.www.ads.biscotti.lastId_",a,void 0)}
;function ok(){}
function pk(){try{var a;try{var b=r("yt.www.ads.biscotti.getId_"),c;if(b)c=b();else{if(!jk){var d=v(nk,n,2);jk=ah().then(kk,d)}c=jk}a=c}catch(e){a=kf(e)}a.then(qk,ok);A(pk,18E5)}catch(e){Ma(e)}}
function qk(a){var b;a:{try{b=window.top.location.href}catch(u){b=2;break a}b=null!=b?b==window.document.location.href?0:1:2}b={dt:gk,flash:ek||"0",frm:b};b.u_tz=-(new Date).getTimezoneOffset();var c;try{c=X.history.length}catch(u){c=0}b.u_his=c;b.u_java=!!X.navigator&&"unknown"!==typeof X.navigator.javaEnabled&&!!X.navigator.javaEnabled&&X.navigator.javaEnabled();X.screen&&(b.u_h=X.screen.height,b.u_w=X.screen.width,b.u_ah=X.screen.availHeight,b.u_aw=X.screen.availWidth,b.u_cd=X.screen.colorDepth);
X.navigator&&X.navigator.plugins&&(b.u_nplug=X.navigator.plugins.length);X.navigator&&X.navigator.mimeTypes&&(b.u_nmime=X.navigator.mimeTypes.length);b.bid=a;b.ca_type=dk?"flash":"image";if(Wc("enable_server_side_search_pyv")||Wc("enable_server_side_mweb_search_pyv")){var d;a=window;try{d=a.screenX;var e=a.screenY}catch(u){}try{var f=a.outerWidth,g=a.outerHeight}catch(u){}try{var k=a.innerWidth,h=a.innerHeight}catch(u){}d=[a.screenLeft,a.screenTop,d,e,a.screen?a.screen.availWidth:void 0,a.screen?
a.screen.availTop:void 0,f,g,k,h];var m;e=window.top||X;try{m=e.document&&!e.document.body?new Gc(-1,-1):Re(e||window).round()}catch(u){m=new Gc(-12245933,-12245933)}e=0;window.SVGElement&&document.createElementNS&&(e|=1);oa(b,{bc:e,bih:m.height,biw:m.width,brdim:d.join(),vis:{visible:1,hidden:2,prerender:3,preview:4}[Zj.webkitVisibilityState||Zj.mozVisibilityState||Zj.visibilityState||""]||0,wgl:!!X.WebGLRenderingContext})}Tf("/ad_data_204",{sb:!0,D:b})}
;function rk(){this.b=z("ALT_PREF_COOKIE_NAME","PREF");var a;if(a=Jc.get(""+this.b,void 0)){a=unescape(a).split("&");for(var b=0;b<a.length;b++){var c=a[b].split("="),d=c[0];(c=c[1])&&(Y[d]=c.toString())}}}
ba(rk);var Y=r("yt.prefs.UserPrefs.prefs_")||{};q("yt.prefs.UserPrefs.prefs_",Y,void 0);function sk(a){if(/^f([1-9][0-9]*)$/.test(a))throw Error("ExpectedRegexMatch: "+a);}
function tk(a){if(!/^\w+$/.test(a))throw Error("ExpectedRegexMismatch: "+a);}
function uk(a){a=void 0!==Y[a]?Y[a].toString():null;return null!=a&&/^[A-Fa-f0-9]+$/.test(a)?parseInt(a,16):null}
rk.prototype.get=function(a,b){tk(a);sk(a);var c=void 0!==Y[a]?Y[a].toString():null;return null!=c?c:b?b:""};
rk.prototype.set=function(a,b){tk(a);sk(a);if(null==b)throw Error("ExpectedNotNull");Y[a]=b.toString()};
rk.prototype.remove=function(a){tk(a);sk(a);delete Y[a]};
rk.prototype.clear=function(){Y={}};function vk(a){for(var b=0;b<a.length;b++){var c=a[b];"send_follow_on_ping_action"==c.name&&c.data&&c.data.follow_on_url&&Zg(c.data.follow_on_url)}}
;function wk(a){Q.call(this,1,arguments);this.pa=a}
x(wk,Q);function xk(a,b){Q.call(this,2,arguments);this.g=a;this.b=b}
x(xk,Q);function yk(a,b,c,d){Q.call(this,1,arguments);this.b=b;this.g=c||null;this.itemId=d||null}
x(yk,Q);function zk(a,b){Q.call(this,1,arguments);this.g=a;this.b=b||null}
x(zk,Q);function Ak(a){Q.call(this,1,arguments)}
x(Ak,Q);var Bk=new R("ypc-core-load",wk),Ck=new R("ypc-guide-sync-success",xk),Dk=new R("ypc-purchase-success",yk),Ek=new R("ypc-subscription-cancel",Ak),Fk=new R("ypc-subscription-cancel-success",zk),Gk=new R("ypc-init-subscription",Ak);var Hk=!1,Ik=[],Jk=[];function Kk(a){a.b?Hk?S(Oi,a):S(Bk,new wk(function(){S(Gk,new Ak(a.b))})):Lk(a.g,a.i,a.f,a.source)}
function Mk(a){a.b?Hk?S(Ti,a):S(Bk,new wk(function(){S(Ek,new Ak(a.b))})):Nk(a.g,a.subscriptionId,a.i,a.f,a.source)}
function Ok(a){Pk(fb(a.b))}
function Qk(a){Rk(fb(a.b))}
function Sk(a){Tk(a.f,a.g,a.b)}
function Uk(a){var b=a.itemId,c=a.b.subscriptionId;b&&c&&S(Ni,new Gi(b,c,a.b.channelInfo))}
function Vk(a){var b=a.b;ta(a.g,function(a,d){S(Ni,new Gi(d,a,b[d]))})}
function Wk(a){S(Si,new U(a.g.itemId));a.b&&a.b.length&&(Xk(a.b,Si),Xk(a.b,Ui))}
function Lk(a,b,c,d){var e=new U(a);S(Li,e);var f={};f.c=a;c&&(f.eurl=c);d&&(f.source=d);c={};(d=z("PLAYBACK_ID"))&&(c.plid=d);(d=z("EVENT_ID"))&&(c.ei=d);b&&Yk(b,c);Uf("/subscription_ajax?action_create_subscription_to_channel=1",{method:"POST",xa:f,D:c,H:function(b,c){var d=c.response;S(Ni,new Gi(a,d.id,d.channel_info));d.show_feed_privacy_dialog&&Ub("SHOW-FEED-PRIVACY-SUBSCRIBE-DIALOG",a);d.actions&&vk(d.actions)},
wa:function(){S(Mi,e)}})}
function Nk(a,b,c,d,e){var f=new U(a);S(Qi,f);var g={};d&&(g.eurl=d);e&&(g.source=e);d={};d.c=a;d.s=b;(a=z("PLAYBACK_ID"))&&(d.plid=a);(a=z("EVENT_ID"))&&(d.ei=a);c&&Yk(c,d);Uf("/subscription_ajax?action_remove_subscriptions=1",{method:"POST",xa:g,D:d,H:function(a,b){var c=b.response;S(Si,f);c.actions&&vk(c.actions)},
wa:function(){S(Ri,f)}})}
function Tk(a,b,c){if(a){var d={};d.channel_id=a;switch(b){case "receive-all-updates":d.receive_all_updates=!0;break;case "receive-no-updates":d.receive_no_updates=!0;d.receive_post_updates=!1;break;case "receive-highlight-updates":d.receive_all_updates=!1;d.receive_no_updates=!1;break;default:return}null===c||d.receive_no_updates||(d.receive_post_updates=c);var e=new Ei(a,b,c);Uf("/subscription_ajax?action_update_subscription_preferences=1",{method:"POST",D:d,onError:function(){S(Yi,e)},
H:function(){S(Xi,e)}})}}
function Pk(a){if(a.length){var b=hb(a,0,40);S("subscription-batch-subscribe-loading");Xk(b,Li);var c={};c.a=b.join(",");var d=function(){S("subscription-batch-subscribe-loaded");Xk(b,Mi)};
Uf("/subscription_ajax?action_create_subscription_to_all=1",{method:"POST",D:c,H:function(c,f){d();var e=f.response,k=e.id;if(da(k)&&k.length==b.length){var h=e.channel_info_map;F(k,function(a,c){var d=b[c];S(Ni,new Gi(d,a,h[d]))});
a.length?Pk(a):S("subscription-batch-subscribe-finished")}},
onError:function(){d();S("subscription-batch-subscribe-failure")}})}}
function Rk(a){if(a.length){var b=hb(a,0,40);S("subscription-batch-unsubscribe-loading");Xk(b,Qi);var c={};c.c=b.join(",");var d=function(){S("subscription-batch-unsubscribe-loaded");Xk(b,Ri)};
Uf("/subscription_ajax?action_remove_subscriptions=1",{method:"POST",D:c,H:function(){d();Xk(b,Si);a.length&&Rk(a)},
onError:function(){d()}})}}
function Xk(a,b){F(a,function(a){S(b,new U(a))})}
function Yk(a,b){var c=Ad(a);oa(b,c)}
;var Zk=null,$k=null,al=null,bl={};function cl(a){kg(a.payload_name,a.payload,Cf,void 0)}
function dl(a){var b=a.id;a=a.ve_type;var c=Rc++;a=new Qc(void 0,a,c);bl[b]=a;b=rg();c=qg();b&&c&&lg(b,c,a)}
function el(a){var b=a.csn;a=a.root_ve_type;if(b&&a&&(y("client-screen-nonce",b),y("ROOT_VE_TYPE",a),a=qg()))for(var c in bl)lg(b,a,bl[c])}
function fl(a){bl[a.id]=new Qc(a.tracking_params)}
function gl(a){var b=rg();a=bl[a.id];b&&a&&mg(ng(),{click:{csn:b,visualElement:Sc(a)}},void 0)}
function hl(a){a=a.ids;var b=rg();if(b){for(var c=[],d=0;d<a.length;d++){var e=bl[a[d]];e&&c.push(e)}c.length&&og(b,c)}}
function il(){var a=Zk;a&&a.startInteractionLogging&&a.startInteractionLogging()}
;q("yt.setConfig",y,void 0);q("yt.setMsg",function(a){Ja(Ia,arguments)},void 0);
q("yt.logging.errors.log",function(a,b,c,d,e){c={name:c||z("INNERTUBE_CONTEXT_CLIENT_NAME",1),version:d||z("INNERTUBE_CONTEXT_CLIENT_VERSION",void 0)};e=window&&window.yterr||e||!1;if(a&&e&&!(5<=jg)){e=a.stacktrace;d=a.columnNumber;var f=r("window.location.href");if(t(a))a={message:a,name:"Unknown error",lineNumber:"Not available",fileName:f,stack:"Not available"};else{var g,k,h=!1;try{g=a.lineNumber||a.hc||"Not available"}catch(Z){g="Not available",h=!0}try{k=a.fileName||a.filename||a.sourceURL||
n.$googDebugFname||f}catch(Z){k="Not available",h=!0}a=!h&&a.lineNumber&&a.fileName&&a.stack&&a.message&&a.name?a:{message:a.message||"Not available",name:a.name||"UnknownError",lineNumber:g,fileName:k,stack:a.stack||"Not available"}}e=e||a.stack;g=a.lineNumber.toString();isNaN(g)||isNaN(d)||(g=g+":"+d);if(!(ig[a.message]||0<=e.indexOf("/YouTubeCenter.js")||0<=e.indexOf("/mytube.js"))){b={xa:{a:"logerror",t:"jserror",type:a.name,msg:a.message.substr(0,1E3),line:g,level:b||"ERROR"},D:{url:z("PAGE_NAME",
window.location.href),file:a.fileName},method:"POST"};e&&(b.D.stack=e);for(var m in c)b.D["client."+m]=c[m];if(m=z("LATEST_ECATCHER_SERVICE_TRACKING_PARAMS",void 0))for(var u in m)b.D[u]=m[u];Uf("/error_204",b);ig[a.message]=!0;jg++}}},void 0);
q("writeEmbed",function(){var a=z("PLAYER_CONFIG",void 0);"1"!=a.privembed&&pk();"gvn"==a.args.ps&&(document.body.style.backgroundColor="transparent");var b=document.referrer,c=z("POST_MESSAGE_ORIGIN");window!=window.top&&b&&b!=document.URL&&(a.args.loaderUrl=b);z("LIGHTWEIGHT_AUTOPLAY")&&(a.args.autoplay="1");a.args.autoplay&&Dj(a.args);Zk=a=ri("player",a);a.addEventListener("onScreenChanged",el);a.addEventListener("onLogClientVeCreated",dl);a.addEventListener("onLogServerVeCreated",fl);a.addEventListener("onLogToGel",
cl);a.addEventListener("onLogVeClicked",gl);a.addEventListener("onLogVesShown",hl);a.addEventListener("onReady",il);b=z("POST_MESSAGE_ID","player");z("ENABLE_JS_API")?al=new Yj(a):z("ENABLE_POST_API")&&t(b)&&t(c)&&($k=new Wj(window.parent,b,c),al=new Xj(a,$k.f));z("BG_P")&&(z("BG_I")||z("BG_IU"))&&fc();kc();Ej=a;Ej.addEventListener("SUBSCRIBE",Hj);Ej.addEventListener("UNSUBSCRIBE",Kj);Fj.push(T(Ni,Lj),T(Si,Mj))},void 0);
q("yt.www.watch.ads.restrictioncookie.spr",function(a){Zg(a+"mac_204?action_fcts=1");return!0},void 0);
var jl=Ka(function(){Nh("ol");Hk=!0;Jk.push(T(Ki,Kk),T(Pi,Mk));Hk||Jk.push(T(Oi,Kk),T(Ti,Mk),T(Ii,Ok),T(Ji,Qk),T(Wi,Sk),T(Dk,Uk),T(Fk,Wk),T(Ck,Vk));var a=rk.getInstance(),b=1<window.devicePixelRatio;if(!!((uk("f"+(Math.floor(119/31)+1))||0)&67108864)!=b){var c="f"+(Math.floor(119/31)+1),d=uk(c)||0,d=b?d|67108864:d&-67108865;0==d?delete Y[c]:Y[c]=d.toString(16).toString();var a=a.b,b=[],e;for(e in Y)b.push(e+"="+escape(Y[e]));Jc.set(""+a,b.join("&"),63072E3,"/","youtube.com")}}),kl=Ka(function(){var a=
Zk;
a&&a.sendAbandonmentPing&&a.sendAbandonmentPing();z("PL_ATT")&&(ec=null);for(var a=0,b=ic.length;a<b;a++){var c=ic[a];if(!isNaN(c)){var d=r("yt.scheduler.instance.cancelJob");d?d(c):La(c)}}ic.length=0;a=ac("//static.doubleclick.net/instream/ad_status.js");if(b=document.getElementById(a))Wb(a),b.parentNode.removeChild(b);jc=!1;y("DCLKSTAT",0);Tb(Ik);Ik.length=0;Gh(Jk);Jk.length=0;Hk=!1;Ej&&(Ej.removeEventListener("SUBSCRIBE",Ij),Ej.removeEventListener("UNSUBSCRIBE",Kj));Ej=null;Gh(Fj);Fj.length=0;
Va(al,$k);if(a=Zk)a.removeEventListener("onScreenChanged",el),a.removeEventListener("onLogClientVeCreated",dl),a.removeEventListener("onLogServerVeCreated",fl),a.removeEventListener("onLogToGel",cl),a.removeEventListener("onLogVeClicked",gl),a.removeEventListener("onLogVesShown",hl),a.removeEventListener("onReady",il),a.destroy();bl={}});
window.addEventListener?(window.addEventListener("load",jl),window.addEventListener("unload",kl)):window.attachEvent&&(window.attachEvent("onload",jl),window.attachEvent("onunload",kl));var ll=tj.getInstance(),ml=W(ll);ml in yj||(ll.register(),ll.ja.push(Rb("yt-uix-init-"+ml,ll.init,ll)),ll.ja.push(Rb("yt-uix-dispose-"+ml,ll.dispose,ll)),yj[ml]=ll);}).call(this);
