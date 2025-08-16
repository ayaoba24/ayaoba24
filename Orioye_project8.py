<!DOCTYPE html>
<!-- saved from url=(0073)https://colab.research.google.com/drive/1GxAEOdWL568uMzUjdoXwNV13x4jAU5xu -->
<html lang="en" theme="dark" editor="Default Dark" data-headlessui-focus-visible=""><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8"><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta http-equiv="origin-trial" content="A7vZI3v+Gz7JfuRolKNM4Aff6zaGuT7X0mf3wtoZTnKv6497cVMnhy03KDqX7kBz/q/iidW7srW31oQbBt4VhgoAAACUeyJvcmlnaW4iOiJodHRwczovL3d3dy5nb29nbGUuY29tOjQ0MyIsImZlYXR1cmUiOiJEaXNhYmxlVGhpcmRQYXJ0eVN0b3JhZ2VQYXJ0aXRpb25pbmczIiwiZXhwaXJ5IjoxNzU3OTgwODAwLCJpc1N1YmRvbWFpbiI6dHJ1ZSwiaXNUaGlyZFBhcnR5Ijp0cnVlfQ=="><meta name="og-profile-acct" content="orioyeesther2019@gmail.com"><script type="text/javascript" async="" charset="utf-8" src="./Orioye.E.project8.ipy_files/recaptcha__en_gb.js.download" crossorigin="anonymous" integrity="sha384-HyGZePWYiBoxOI8rEIIvh7dYm8XXVDx0IRdD421yDk3fSsOiQgyN0vbYAuZaZZTP" nonce=""></script><script type="text/javascript" async="" charset="utf-8" src="./Orioye.E.project8.ipy_files/recaptcha__en_gb.js.download" crossorigin="anonymous" integrity="sha384-HyGZePWYiBoxOI8rEIIvh7dYm8XXVDx0IRdD421yDk3fSsOiQgyN0vbYAuZaZZTP" nonce=""></script><script src="./Orioye.E.project8.ipy_files/cb=gapi.loaded_1" nonce="" async=""></script><script type="text/javascript" async="" src="./Orioye.E.project8.ipy_files/js" nonce=""></script><script src="./Orioye.E.project8.ipy_files/cb=gapi.loaded_0" nonce="" async=""></script><script async="" src="./Orioye.E.project8.ipy_files/analytics.js.download"></script><script nonce="">
      document.addEventListener('keydown', (e) => {
        // Stop propagation on ESC because otherwise it will halt outbound XHRs
        // See b/131755324 for more info.
        if (e.key === 'Escape') {
          e.stopPropagation();
          e.preventDefault();
        }
      });
    </script><meta name="referrer" content="origin"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Orioye.E.project8.ipy - Colab</title><style type="text/css">:root, :host {
  --fa-font-solid: normal 900 1em/1 "Font Awesome 6 Free";
  --fa-font-regular: normal 400 1em/1 "Font Awesome 6 Free";
  --fa-font-light: normal 300 1em/1 "Font Awesome 6 Pro";
  --fa-font-thin: normal 100 1em/1 "Font Awesome 6 Pro";
  --fa-font-duotone: normal 900 1em/1 "Font Awesome 6 Duotone";
  --fa-font-duotone-regular: normal 400 1em/1 "Font Awesome 6 Duotone";
  --fa-font-duotone-light: normal 300 1em/1 "Font Awesome 6 Duotone";
  --fa-font-duotone-thin: normal 100 1em/1 "Font Awesome 6 Duotone";
  --fa-font-brands: normal 400 1em/1 "Font Awesome 6 Brands";
  --fa-font-sharp-solid: normal 900 1em/1 "Font Awesome 6 Sharp";
  --fa-font-sharp-regular: normal 400 1em/1 "Font Awesome 6 Sharp";
  --fa-font-sharp-light: normal 300 1em/1 "Font Awesome 6 Sharp";
  --fa-font-sharp-thin: normal 100 1em/1 "Font Awesome 6 Sharp";
  --fa-font-sharp-duotone-solid: normal 900 1em/1 "Font Awesome 6 Sharp Duotone";
  --fa-font-sharp-duotone-regular: normal 400 1em/1 "Font Awesome 6 Sharp Duotone";
  --fa-font-sharp-duotone-light: normal 300 1em/1 "Font Awesome 6 Sharp Duotone";
  --fa-font-sharp-duotone-thin: normal 100 1em/1 "Font Awesome 6 Sharp Duotone";
}

svg:not(:root).svg-inline--fa, svg:not(:host).svg-inline--fa {
  overflow: visible;
  box-sizing: content-box;
}

.svg-inline--fa {
  display: var(--fa-display, inline-block);
  height: 1em;
  overflow: visible;
  vertical-align: -0.125em;
}
.svg-inline--fa.fa-2xs {
  vertical-align: 0.1em;
}
.svg-inline--fa.fa-xs {
  vertical-align: 0em;
}
.svg-inline--fa.fa-sm {
  vertical-align: -0.0714285705em;
}
.svg-inline--fa.fa-lg {
  vertical-align: -0.2em;
}
.svg-inline--fa.fa-xl {
  vertical-align: -0.25em;
}
.svg-inline--fa.fa-2xl {
  vertical-align: -0.3125em;
}
.svg-inline--fa.fa-pull-left {
  margin-right: var(--fa-pull-margin, 0.3em);
  width: auto;
}
.svg-inline--fa.fa-pull-right {
  margin-left: var(--fa-pull-margin, 0.3em);
  width: auto;
}
.svg-inline--fa.fa-li {
  width: var(--fa-li-width, 2em);
  top: 0.25em;
}
.svg-inline--fa.fa-fw {
  width: var(--fa-fw-width, 1.25em);
}

.fa-layers svg.svg-inline--fa {
  bottom: 0;
  left: 0;
  margin: auto;
  position: absolute;
  right: 0;
  top: 0;
}

.fa-layers-counter, .fa-layers-text {
  display: inline-block;
  position: absolute;
  text-align: center;
}

.fa-layers {
  display: inline-block;
  height: 1em;
  position: relative;
  text-align: center;
  vertical-align: -0.125em;
  width: 1em;
}
.fa-layers svg.svg-inline--fa {
  transform-origin: center center;
}

.fa-layers-text {
  left: 50%;
  top: 50%;
  transform: translate(-50%, -50%);
  transform-origin: center center;
}

.fa-layers-counter {
  background-color: var(--fa-counter-background-color, #ff253a);
  border-radius: var(--fa-counter-border-radius, 1em);
  box-sizing: border-box;
  color: var(--fa-inverse, #fff);
  line-height: var(--fa-counter-line-height, 1);
  max-width: var(--fa-counter-max-width, 5em);
  min-width: var(--fa-counter-min-width, 1.5em);
  overflow: hidden;
  padding: var(--fa-counter-padding, 0.25em 0.5em);
  right: var(--fa-right, 0);
  text-overflow: ellipsis;
  top: var(--fa-top, 0);
  transform: scale(var(--fa-counter-scale, 0.25));
  transform-origin: top right;
}

.fa-layers-bottom-right {
  bottom: var(--fa-bottom, 0);
  right: var(--fa-right, 0);
  top: auto;
  transform: scale(var(--fa-layers-scale, 0.25));
  transform-origin: bottom right;
}

.fa-layers-bottom-left {
  bottom: var(--fa-bottom, 0);
  left: var(--fa-left, 0);
  right: auto;
  top: auto;
  transform: scale(var(--fa-layers-scale, 0.25));
  transform-origin: bottom left;
}

.fa-layers-top-right {
  top: var(--fa-top, 0);
  right: var(--fa-right, 0);
  transform: scale(var(--fa-layers-scale, 0.25));
  transform-origin: top right;
}

.fa-layers-top-left {
  left: var(--fa-left, 0);
  right: auto;
  top: var(--fa-top, 0);
  transform: scale(var(--fa-layers-scale, 0.25));
  transform-origin: top left;
}

.fa-1x {
  font-size: 1em;
}

.fa-2x {
  font-size: 2em;
}

.fa-3x {
  font-size: 3em;
}

.fa-4x {
  font-size: 4em;
}

.fa-5x {
  font-size: 5em;
}

.fa-6x {
  font-size: 6em;
}

.fa-7x {
  font-size: 7em;
}

.fa-8x {
  font-size: 8em;
}

.fa-9x {
  font-size: 9em;
}

.fa-10x {
  font-size: 10em;
}

.fa-2xs {
  font-size: 0.625em;
  line-height: 0.1em;
  vertical-align: 0.225em;
}

.fa-xs {
  font-size: 0.75em;
  line-height: 0.0833333337em;
  vertical-align: 0.125em;
}

.fa-sm {
  font-size: 0.875em;
  line-height: 0.0714285718em;
  vertical-align: 0.0535714295em;
}

.fa-lg {
  font-size: 1.25em;
  line-height: 0.05em;
  vertical-align: -0.075em;
}

.fa-xl {
  font-size: 1.5em;
  line-height: 0.0416666682em;
  vertical-align: -0.125em;
}

.fa-2xl {
  font-size: 2em;
  line-height: 0.03125em;
  vertical-align: -0.1875em;
}

.fa-fw {
  text-align: center;
  width: 1.25em;
}

.fa-ul {
  list-style-type: none;
  margin-left: var(--fa-li-margin, 2.5em);
  padding-left: 0;
}
.fa-ul > li {
  position: relative;
}

.fa-li {
  left: calc(-1 * var(--fa-li-width, 2em));
  position: absolute;
  text-align: center;
  width: var(--fa-li-width, 2em);
  line-height: inherit;
}

.fa-border {
  border-color: var(--fa-border-color, #eee);
  border-radius: var(--fa-border-radius, 0.1em);
  border-style: var(--fa-border-style, solid);
  border-width: var(--fa-border-width, 0.08em);
  padding: var(--fa-border-padding, 0.2em 0.25em 0.15em);
}

.fa-pull-left {
  float: left;
  margin-right: var(--fa-pull-margin, 0.3em);
}

.fa-pull-right {
  float: right;
  margin-left: var(--fa-pull-margin, 0.3em);
}

.fa-beat {
  animation-name: fa-beat;
  animation-delay: var(--fa-animation-delay, 0s);
  animation-direction: var(--fa-animation-direction, normal);
  animation-duration: var(--fa-animation-duration, 1s);
  animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  animation-timing-function: var(--fa-animation-timing, ease-in-out);
}

.fa-bounce {
  animation-name: fa-bounce;
  animation-delay: var(--fa-animation-delay, 0s);
  animation-direction: var(--fa-animation-direction, normal);
  animation-duration: var(--fa-animation-duration, 1s);
  animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.28, 0.84, 0.42, 1));
}

.fa-fade {
  animation-name: fa-fade;
  animation-delay: var(--fa-animation-delay, 0s);
  animation-direction: var(--fa-animation-direction, normal);
  animation-duration: var(--fa-animation-duration, 1s);
  animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.4, 0, 0.6, 1));
}

.fa-beat-fade {
  animation-name: fa-beat-fade;
  animation-delay: var(--fa-animation-delay, 0s);
  animation-direction: var(--fa-animation-direction, normal);
  animation-duration: var(--fa-animation-duration, 1s);
  animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  animation-timing-function: var(--fa-animation-timing, cubic-bezier(0.4, 0, 0.6, 1));
}

.fa-flip {
  animation-name: fa-flip;
  animation-delay: var(--fa-animation-delay, 0s);
  animation-direction: var(--fa-animation-direction, normal);
  animation-duration: var(--fa-animation-duration, 1s);
  animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  animation-timing-function: var(--fa-animation-timing, ease-in-out);
}

.fa-shake {
  animation-name: fa-shake;
  animation-delay: var(--fa-animation-delay, 0s);
  animation-direction: var(--fa-animation-direction, normal);
  animation-duration: var(--fa-animation-duration, 1s);
  animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  animation-timing-function: var(--fa-animation-timing, linear);
}

.fa-spin {
  animation-name: fa-spin;
  animation-delay: var(--fa-animation-delay, 0s);
  animation-direction: var(--fa-animation-direction, normal);
  animation-duration: var(--fa-animation-duration, 2s);
  animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  animation-timing-function: var(--fa-animation-timing, linear);
}

.fa-spin-reverse {
  --fa-animation-direction: reverse;
}

.fa-pulse,
.fa-spin-pulse {
  animation-name: fa-spin;
  animation-direction: var(--fa-animation-direction, normal);
  animation-duration: var(--fa-animation-duration, 1s);
  animation-iteration-count: var(--fa-animation-iteration-count, infinite);
  animation-timing-function: var(--fa-animation-timing, steps(8));
}

@media (prefers-reduced-motion: reduce) {
  .fa-beat,
.fa-bounce,
.fa-fade,
.fa-beat-fade,
.fa-flip,
.fa-pulse,
.fa-shake,
.fa-spin,
.fa-spin-pulse {
    animation-delay: -1ms;
    animation-duration: 1ms;
    animation-iteration-count: 1;
    transition-delay: 0s;
    transition-duration: 0s;
  }
}
@keyframes fa-beat {
  0%, 90% {
    transform: scale(1);
  }
  45% {
    transform: scale(var(--fa-beat-scale, 1.25));
  }
}
@keyframes fa-bounce {
  0% {
    transform: scale(1, 1) translateY(0);
  }
  10% {
    transform: scale(var(--fa-bounce-start-scale-x, 1.1), var(--fa-bounce-start-scale-y, 0.9)) translateY(0);
  }
  30% {
    transform: scale(var(--fa-bounce-jump-scale-x, 0.9), var(--fa-bounce-jump-scale-y, 1.1)) translateY(var(--fa-bounce-height, -0.5em));
  }
  50% {
    transform: scale(var(--fa-bounce-land-scale-x, 1.05), var(--fa-bounce-land-scale-y, 0.95)) translateY(0);
  }
  57% {
    transform: scale(1, 1) translateY(var(--fa-bounce-rebound, -0.125em));
  }
  64% {
    transform: scale(1, 1) translateY(0);
  }
  100% {
    transform: scale(1, 1) translateY(0);
  }
}
@keyframes fa-fade {
  50% {
    opacity: var(--fa-fade-opacity, 0.4);
  }
}
@keyframes fa-beat-fade {
  0%, 100% {
    opacity: var(--fa-beat-fade-opacity, 0.4);
    transform: scale(1);
  }
  50% {
    opacity: 1;
    transform: scale(var(--fa-beat-fade-scale, 1.125));
  }
}
@keyframes fa-flip {
  50% {
    transform: rotate3d(var(--fa-flip-x, 0), var(--fa-flip-y, 1), var(--fa-flip-z, 0), var(--fa-flip-angle, -180deg));
  }
}
@keyframes fa-shake {
  0% {
    transform: rotate(-15deg);
  }
  4% {
    transform: rotate(15deg);
  }
  8%, 24% {
    transform: rotate(-18deg);
  }
  12%, 28% {
    transform: rotate(18deg);
  }
  16% {
    transform: rotate(-22deg);
  }
  20% {
    transform: rotate(22deg);
  }
  32% {
    transform: rotate(-12deg);
  }
  36% {
    transform: rotate(12deg);
  }
  40%, 100% {
    transform: rotate(0deg);
  }
}
@keyframes fa-spin {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
.fa-rotate-90 {
  transform: rotate(90deg);
}

.fa-rotate-180 {
  transform: rotate(180deg);
}

.fa-rotate-270 {
  transform: rotate(270deg);
}

.fa-flip-horizontal {
  transform: scale(-1, 1);
}

.fa-flip-vertical {
  transform: scale(1, -1);
}

.fa-flip-both,
.fa-flip-horizontal.fa-flip-vertical {
  transform: scale(-1, -1);
}

.fa-rotate-by {
  transform: rotate(var(--fa-rotate-angle, 0));
}

.fa-stack {
  display: inline-block;
  vertical-align: middle;
  height: 2em;
  position: relative;
  width: 2.5em;
}

.fa-stack-1x,
.fa-stack-2x {
  bottom: 0;
  left: 0;
  margin: auto;
  position: absolute;
  right: 0;
  top: 0;
  z-index: var(--fa-stack-z-index, auto);
}

.svg-inline--fa.fa-stack-1x {
  height: 1em;
  width: 1.25em;
}
.svg-inline--fa.fa-stack-2x {
  height: 2em;
  width: 2.5em;
}

.fa-inverse {
  color: var(--fa-inverse, #fff);
}

.sr-only,
.fa-sr-only {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.sr-only-focusable:not(:focus),
.fa-sr-only-focusable:not(:focus) {
  position: absolute;
  width: 1px;
  height: 1px;
  padding: 0;
  margin: -1px;
  overflow: hidden;
  clip: rect(0, 0, 0, 0);
  white-space: nowrap;
  border-width: 0;
}

.svg-inline--fa .fa-primary {
  fill: var(--fa-primary-color, currentColor);
  opacity: var(--fa-primary-opacity, 1);
}

.svg-inline--fa .fa-secondary {
  fill: var(--fa-secondary-color, currentColor);
  opacity: var(--fa-secondary-opacity, 0.4);
}

.svg-inline--fa.fa-swap-opacity .fa-primary {
  opacity: var(--fa-secondary-opacity, 0.4);
}

.svg-inline--fa.fa-swap-opacity .fa-secondary {
  opacity: var(--fa-primary-opacity, 1);
}

.svg-inline--fa mask .fa-primary,
.svg-inline--fa mask .fa-secondary {
  fill: black;
}</style><link href="./Orioye.E.project8.ipy_files/css2" rel="stylesheet"><link href="./Orioye.E.project8.ipy_files/css" rel="stylesheet"><link rel="search" type="application/opensearchdescription+xml" href="https://colab.research.google.com/opensearch.xml" title="Google Colab"><style>.gb_4d{font:13px/27px Roboto,Arial,sans-serif;z-index:986}@-webkit-keyframes gb__a{0%{opacity:0}50%{opacity:1}}@keyframes gb__a{0%{opacity:0}50%{opacity:1}}a.gb_Qa{border:none;color:#4285f4;cursor:default;font-weight:bold;outline:none;position:relative;text-align:center;text-decoration:none;text-transform:uppercase;white-space:nowrap;-webkit-user-select:none}a.gb_Qa:hover::after,a.gb_Qa:focus::after{background-color:rgba(0,0,0,.12);content:"";height:100%;left:0;position:absolute;top:0;width:100%}a.gb_Qa:hover,a.gb_Qa:focus{text-decoration:none}a.gb_Qa:active{background-color:rgba(153,153,153,.4);text-decoration:none}a.gb_Ra{background-color:#4285f4;color:#fff}a.gb_Ra:active{background-color:#0043b2}.gb_Sa{box-shadow:0 1px 1px rgba(0,0,0,.16)}.gb_Qa,.gb_Ra,.gb_Ta,.gb_Ua{display:inline-block;line-height:28px;padding:0 12px;border-radius:2px}.gb_Ta{background:#f8f8f8;border:1px solid #c6c6c6}.gb_Ua{background:#f8f8f8}.gb_Ta,#gb a.gb_Ta.gb_Ta,.gb_Ua{color:#666;cursor:default;text-decoration:none}#gb a.gb_Ua{cursor:default;text-decoration:none}.gb_Ua{border:1px solid #4285f4;font-weight:bold;outline:none;background:#4285f4;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#4387fd),to(#4683ea));background:-webkit-linear-gradient(top,#4387fd,#4683ea);background:linear-gradient(top,#4387fd,#4683ea);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#4387fd,endColorstr=#4683ea,GradientType=0)}#gb a.gb_Ua{color:#fff}.gb_Ua:hover{box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_Ua:active{box-shadow:inset 0 2px 0 rgba(0,0,0,.15);background:#3c78dc;background:-webkit-gradient(linear,left top,left bottom,from(top),color-stop(#3c7ae4),to(#3f76d3));background:-webkit-linear-gradient(top,#3c7ae4,#3f76d3);background:linear-gradient(top,#3c7ae4,#3f76d3);filter:progid:DXImageTransform.Microsoft.gradient(startColorstr=#3c7ae4,endColorstr=#3f76d3,GradientType=0)}#gb .gb_Va{background:#fff;border:1px solid #dadce0;color:#1a73e8;display:inline-block;text-decoration:none}#gb .gb_Va:hover{background:#f8fbff;border-color:#dadce0;color:#174ea6}#gb .gb_Va:focus{background:#f4f8ff;color:#174ea6;outline:1px solid #174ea6}#gb .gb_Va:active,#gb .gb_Va:focus:active{background:#ecf3fe;color:#174ea6}#gb .gb_Va.gb_H{background:transparent;border:1px solid #5f6368;color:#8ab4f8;text-decoration:none}#gb .gb_Va.gb_H:hover{background:rgba(255,255,255,.04);color:#e8eaed}#gb .gb_Va.gb_H:focus{background:rgba(232,234,237,.12);color:#e8eaed;outline:1px solid #e8eaed}#gb .gb_Va.gb_H:active,#gb .gb_Va.gb_H:focus:active{background:rgba(232,234,237,.1);color:#e8eaed}.gb_dd{display:inline-block;vertical-align:middle}.gb_Qe .gb_Q{bottom:-3px;right:-5px}.gb_D{position:relative}.gb_B{display:inline-block;outline:none;vertical-align:middle;border-radius:2px;box-sizing:border-box;height:40px;width:40px;cursor:pointer;text-decoration:none}#gb#gb a.gb_B{cursor:pointer;text-decoration:none}.gb_B,a.gb_B{color:#000}.gb_ed{border-color:transparent;border-bottom-color:#fff;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;top:33px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s}.gb_fd{border-color:transparent;border-style:dashed dashed solid;border-width:0 8.5px 8.5px;display:none;position:absolute;left:11.5px;z-index:1;height:0;width:0;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-bottom-color:rgba(0,0,0,.2);top:32px}x:-o-prefocus,div.gb_fd{border-bottom-color:#ccc}.gb_la{background:#fff;border:1px solid #ccc;border-color:rgba(0,0,0,.2);color:#000;-webkit-box-shadow:0 2px 10px rgba(0,0,0,.2);box-shadow:0 2px 10px rgba(0,0,0,.2);display:none;outline:none;overflow:hidden;position:absolute;right:8px;top:62px;-webkit-animation:gb__a .2s;animation:gb__a .2s;border-radius:2px;-webkit-user-select:text}.gb_dd.gb_Uc .gb_ed,.gb_dd.gb_Uc .gb_fd,.gb_dd.gb_Uc .gb_la,.gb_Uc.gb_la{display:block}.gb_dd.gb_Uc.gb_gd .gb_ed,.gb_dd.gb_Uc.gb_gd .gb_fd{display:none}.gb_Re{position:absolute;right:8px;top:62px;z-index:-1}.gb_hd .gb_ed,.gb_hd .gb_fd,.gb_hd .gb_la{margin-top:-10px}.gb_dd:first-child,#gbsfw:first-child+.gb_dd{padding-left:4px}.gb_Fa.gb_Se .gb_dd:first-child{padding-left:0}.gb_Te{position:relative}.gb_3c .gb_Te,.gb_Kd .gb_Te{float:right}.gb_B{padding:8px;cursor:pointer}.gb_B::after{content:"";position:absolute;top:-4px;bottom:-4px;left:-4px;right:-4px}.gb_Fa .gb_id:not(.gb_Qa):focus img{background-color:rgba(0,0,0,.2);outline:none;-webkit-border-radius:50%;border-radius:50%}.gb_jd button svg,.gb_B{-webkit-border-radius:50%;border-radius:50%}.gb_jd button:focus:not(:focus-visible) svg,.gb_jd button:hover svg,.gb_jd button:active svg,.gb_B:focus:not(:focus-visible),.gb_B:hover,.gb_B:active,.gb_B[aria-expanded=true]{outline:none}.gb_Mc .gb_jd.gb_kd button:focus-visible svg,.gb_jd button:focus-visible svg,.gb_B:focus-visible{outline:1px solid #202124}.gb_Mc .gb_jd button:focus-visible svg,.gb_Mc .gb_B:focus-visible{outline:1px solid #f1f3f4}@media (forced-colors:active){.gb_Mc .gb_jd.gb_kd button:focus-visible svg,.gb_jd button:focus-visible svg,.gb_Mc .gb_jd button:focus-visible svg{outline:1px solid currentcolor}}.gb_Mc .gb_jd.gb_kd button:focus svg,.gb_Mc .gb_jd.gb_kd button:focus:hover svg,.gb_jd button:focus svg,.gb_jd button:focus:hover svg,.gb_B:focus,.gb_B:focus:hover{background-color:rgba(60,64,67,.1)}.gb_Mc .gb_jd.gb_kd button:active svg,.gb_jd button:active svg,.gb_B:active{background-color:rgba(60,64,67,.12)}.gb_Mc .gb_jd.gb_kd button:hover svg,.gb_jd button:hover svg,.gb_B:hover{background-color:rgba(60,64,67,.08)}.gb_Wa .gb_B.gb_Za:hover{background-color:transparent}.gb_B[aria-expanded=true],.gb_B:hover[aria-expanded=true]{background-color:rgba(95,99,104,.24)}.gb_B[aria-expanded=true] .gb_F{fill:#5f6368;opacity:1}.gb_Mc .gb_jd button:hover svg,.gb_Mc .gb_B:hover{background-color:rgba(232,234,237,.08)}.gb_Mc .gb_jd button:focus svg,.gb_Mc .gb_jd button:focus:hover svg,.gb_Mc .gb_B:focus,.gb_Mc .gb_B:focus:hover{background-color:rgba(232,234,237,.1)}.gb_Mc .gb_jd button:active svg,.gb_Mc .gb_B:active{background-color:rgba(232,234,237,.12)}.gb_Mc .gb_B[aria-expanded=true],.gb_Mc .gb_B:hover[aria-expanded=true]{background-color:rgba(255,255,255,.12)}.gb_Mc .gb_B[aria-expanded=true] .gb_F{fill:#fff;opacity:1}.gb_dd{padding:4px}.gb_Fa.gb_Se .gb_dd{padding:4px 2px}.gb_Fa.gb_Se .gb_z.gb_dd{padding-left:6px}.gb_la{z-index:991;line-height:normal}.gb_la.gb_ld{left:0;right:auto}@media (max-width:350px){.gb_la.gb_ld{left:0}}.gb_Ue .gb_la{top:56px}.gb_R{display:none!important}.gb_od{visibility:hidden}.gb_J .gb_B,.gb_ka .gb_J .gb_B{background-position:-64px -29px}.gb_1 .gb_J .gb_B{background-position:-29px -29px;opacity:1}.gb_J .gb_B,.gb_J .gb_B:hover,.gb_J .gb_B:focus{opacity:1}.gb_L{display:none}@media screen and (max-width:319px){.gb_md:not(.gb_nd) .gb_J{display:none;visibility:hidden}}.gb_Q{display:none}.gb_ad{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-size:20px;font-weight:400;letter-spacing:0.25px;line-height:48px;margin-bottom:2px;opacity:1;overflow:hidden;padding-left:16px;position:relative;text-overflow:ellipsis;vertical-align:middle;top:2px;white-space:nowrap;-webkit-flex:1 1 auto;-webkit-box-flex:1;flex:1 1 auto}.gb_ad.gb_bd{color:#3c4043}.gb_Fa.gb_cc .gb_ad{margin-bottom:0}.gb_td.gb_vd .gb_ad{padding-left:4px}.gb_Fa.gb_cc .gb_wd{position:relative;top:-2px}.gb_cd{display:none}.gb_Fa{color:black;min-width:160px;position:relative;-webkit-transition:box-shadow 250ms;transition:box-shadow 250ms}.gb_Fa.gb_Tc{min-width:120px}.gb_Fa.gb_xd .gb_yd{display:none}.gb_Fa.gb_xd .gb_md{height:56px}header.gb_Fa{display:block}.gb_Fa svg{fill:currentColor}.gb_Ed{position:fixed;top:0;width:100%}.gb_zd{-webkit-box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2);box-shadow:0 4px 5px 0 rgba(0,0,0,.14),0 1px 10px 0 rgba(0,0,0,.12),0 2px 4px -1px rgba(0,0,0,.2)}.gb_Fd{height:64px}.gb_md{-webkit-box-sizing:border-box;box-sizing:border-box;position:relative;width:100%;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-box-pack:space-between;-webkit-justify-content:space-between;justify-content:space-between;min-width:-webkit-min-content;min-width:min-content}.gb_Fa:not(.gb_cc) .gb_md{padding:8px}.gb_Fa.gb_Hd .gb_md{-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Fa .gb_md.gb_nd.gb_Id{min-width:0}.gb_Fa.gb_cc .gb_md{padding:4px;padding-left:8px;min-width:0}.gb_yd{height:48px;vertical-align:middle;white-space:nowrap;-webkit-box-align:center;-webkit-align-items:center;align-items:center;display:-webkit-box;display:-webkit-flex;display:flex;-webkit-user-select:none}.gb_Bd>.gb_yd{display:table-cell;width:100%}.gb_td{padding-right:30px;box-sizing:border-box;-webkit-flex:1 0 auto;-webkit-box-flex:1;flex:1 0 auto}.gb_Fa.gb_cc .gb_td{padding-right:14px}.gb_Cd{-webkit-flex:1 1 100%;-webkit-box-flex:1;flex:1 1 100%}.gb_Cd>:only-child{display:inline-block}.gb_Dd.gb_4c{padding-left:4px}.gb_Dd.gb_Jd,.gb_Fa.gb_Hd .gb_Dd,.gb_Fa.gb_cc:not(.gb_Kd) .gb_Dd{padding-left:0}.gb_Fa.gb_cc .gb_Dd.gb_Jd{padding-right:0}.gb_Fa.gb_cc .gb_Dd.gb_Jd .gb_Wa{margin-left:10px}.gb_4c{display:inline}.gb_Fa.gb_Xc .gb_Dd.gb_Ld,.gb_Fa.gb_Kd .gb_Dd.gb_Ld{padding-left:2px}.gb_ad{display:inline-block}.gb_Dd{-webkit-box-sizing:border-box;box-sizing:border-box;height:48px;line-height:normal;padding:0 4px;padding-left:30px;-webkit-flex:0 0 auto;-webkit-box-flex:0;flex:0 0 auto;-webkit-box-pack:flex-end;-webkit-justify-content:flex-end;justify-content:flex-end}.gb_Kd{height:48px}.gb_Fa.gb_Kd{min-width:auto}.gb_Kd .gb_Dd{float:right;padding-left:32px}.gb_Kd .gb_Dd.gb_Md{padding-left:0}.gb_Nd{font-size:14px;max-width:200px;overflow:hidden;padding:0 12px;text-overflow:ellipsis;white-space:nowrap;-webkit-user-select:text}.gb_qd{-webkit-transition:background-color .4s;-webkit-transition:background-color .4s;transition:background-color .4s}.gb_Od{color:black}.gb_Mc{color:white}.gb_Fa a,.gb_Qc a{color:inherit}.gb_ba{color:rgba(0,0,0,.87)}.gb_Fa svg,.gb_Qc svg,.gb_td .gb_ud,.gb_3c .gb_ud{color:#5f6368;opacity:1}.gb_Mc svg,.gb_Qc.gb_Vc svg,.gb_Mc .gb_td .gb_ud,.gb_Mc .gb_td .gb_Lc,.gb_Mc .gb_td .gb_wd,.gb_Qc.gb_Vc .gb_ud{color:rgba(255,255,255,.87)}.gb_Mc .gb_td .gb_Pd:not(.gb_Qd){opacity:.87}.gb_bd{color:inherit;opacity:1;text-rendering:optimizeLegibility;-webkit-font-smoothing:antialiased}.gb_Mc .gb_bd,.gb_Od .gb_bd{opacity:1}.gb_Rd{position:relative}.gb_M{font-family:arial,sans-serif;line-height:normal;padding-right:15px}a.gb_X,span.gb_X{color:rgba(0,0,0,.87);text-decoration:none}.gb_Mc a.gb_X,.gb_Mc span.gb_X{color:white}a.gb_X:focus{outline-offset:2px}a.gb_X:hover{text-decoration:underline}.gb_Z{display:inline-block;padding-left:15px}.gb_Z .gb_X{display:inline-block;line-height:24px;vertical-align:middle}.gb_rd{font-family:Google Sans,Roboto,Helvetica,Arial,sans-serif;font-weight:500;font-size:14px;letter-spacing:.25px;line-height:16px;margin-left:10px;margin-right:8px;min-width:96px;padding:9px 23px;text-align:center;vertical-align:middle;border-radius:4px;box-sizing:border-box}.gb_Fa.gb_Kd .gb_rd{margin-left:8px}#gb a.gb_Ua.gb_rd{cursor:pointer}.gb_Ua.gb_rd:hover{background:#1b66c9;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ua.gb_rd:focus,.gb_Ua.gb_rd:hover:focus{background:#1c5fba;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_Ua.gb_rd:active{background:#1b63c1;-webkit-box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3);box-shadow:0 1px 3px 1px rgba(66,64,67,.15),0 1px 2px 0 rgba(60,64,67,.3)}.gb_rd{background:#1a73e8;border:1px solid transparent}.gb_Fa.gb_cc .gb_rd{padding:9px 15px;min-width:80px}.gb_Sd{text-align:left}#gb .gb_Mc a.gb_rd:not(.gb_H),#gb.gb_Mc a.gb_rd{background:#fff;border-color:#dadce0;-webkit-box-shadow:none;box-shadow:none;color:#1a73e8}#gb a.gb_Ua.gb_H.gb_rd{background:#8ab4f8;border:1px solid transparent;-webkit-box-shadow:none;box-shadow:none;color:#202124}#gb .gb_Mc a.gb_rd:hover:not(.gb_H),#gb.gb_Mc a.gb_rd:hover{background:#f8fbff;border-color:#cce0fc}#gb a.gb_Ua.gb_H.gb_rd:hover{background:#93baf9;border-color:transparent;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.3)}#gb .gb_Mc a.gb_rd:focus:not(.gb_H),#gb .gb_Mc a.gb_rd:focus:hover:not(.gb_H),#gb.gb_Mc a.gb_rd:focus:not(.gb_H),#gb.gb_Mc a.gb_rd:focus:hover:not(.gb_H){background:#f4f8ff;outline:1px solid #c9ddfc}#gb a.gb_Ua.gb_H.gb_rd:focus,#gb a.gb_Ua.gb_H.gb_rd:focus:hover{background:#a6c6fa;border-color:transparent;-webkit-box-shadow:none;box-shadow:none}#gb .gb_Mc a.gb_rd:active:not(.gb_H),#gb.gb_Mc a.gb_rd:active{background:#ecf3fe}#gb a.gb_Ua.gb_H.gb_rd:active{background:#a1c3f9;-webkit-box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15);box-shadow:0 1px 2px rgba(60,64,67,.3),0 2px 6px 2px rgba(60,64,67,.15)}.gb_K{display:none}@media screen and (max-width:319px){.gb_md .gb_J{display:none;visibility:hidden}}.gb_Wa{background-color:rgba(255,255,255,.88);border:1px solid #dadce0;-webkit-box-sizing:border-box;box-sizing:border-box;cursor:pointer;display:inline-block;max-height:48px;overflow:hidden;outline:none;padding:0;vertical-align:middle;width:134px;-webkit-border-radius:8px;border-radius:8px}.gb_Wa.gb_H{background-color:transparent;border:1px solid #5f6368}.gb_3a{display:inherit}.gb_Wa.gb_H .gb_3a{background:#fff;-webkit-border-radius:4px;border-radius:4px;display:inline-block;left:8px;margin-right:5px;position:relative;padding:3px;top:-1px}.gb_Wa:hover{border:1px solid #d2e3fc;background-color:rgba(248,250,255,.88)}.gb_Wa.gb_H:hover{background-color:rgba(241,243,244,.04);border:1px solid #5f6368}.gb_Wa:focus-visible,.gb_Wa:focus{background-color:#fff;outline:1px solid #202124;-webkit-box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15);box-shadow:0 1px 2px 0 rgba(60,64,67,.3),0 1px 3px 1px rgba(60,64,67,.15)}.gb_Wa.gb_H:focus-visible,.gb_Wa.gb_H:focus{background-color:rgba(241,243,244,.12);outline:1px solid #f1f3f4;-webkit-box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3);box-shadow:0 1px 3px 1px rgba(0,0,0,.15),0 1px 2px 0 rgba(0,0,0,.3)}.gb_Wa.gb_H:active,.gb_Wa.gb_Uc.gb_H:focus{background-color:rgba(241,243,244,.1);border:1px solid #5f6368}.gb_4a{display:inline-block;padding-bottom:2px;padding-left:7px;padding-top:2px;text-align:center;vertical-align:middle;line-height:32px;width:78px}.gb_Wa.gb_H .gb_4a{line-height:26px;margin-left:0;padding-bottom:0;padding-left:0;padding-top:0;width:72px}.gb_4a.gb_5a{background-color:#f1f3f4;-webkit-border-radius:4px;border-radius:4px;margin-left:8px;padding-left:0;line-height:30px}.gb_4a.gb_5a .gb_Jc{vertical-align:middle}.gb_Fa:not(.gb_cc) .gb_Wa{margin-left:10px;margin-right:4px}.gb_Td{max-height:32px;width:78px}.gb_Wa.gb_H .gb_Td{max-height:26px;width:72px}.gb_P{-webkit-background-size:32px 32px;background-size:32px 32px;border:0;-webkit-border-radius:50%;border-radius:50%;display:block;margin:0px;position:relative;height:32px;width:32px;z-index:0}.gb_eb{background-color:#e8f0fe;border:1px solid rgba(32,33,36,.08);position:relative}.gb_eb.gb_P{height:30px;width:30px}.gb_eb.gb_P:hover,.gb_eb.gb_P:active{-webkit-box-shadow:none;box-shadow:none}.gb_fb{background:#fff;border:none;-webkit-border-radius:50%;border-radius:50%;bottom:2px;-webkit-box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);box-shadow:0px 1px 2px 0px rgba(60,64,67,.30),0px 1px 3px 1px rgba(60,64,67,.15);height:14px;margin:2px;position:absolute;right:0;width:14px}.gb_wc{color:#1f71e7;font:400 22px/32px Google Sans,Roboto,Helvetica,Arial,sans-serif;text-align:center;text-transform:uppercase}@media (-webkit-min-device-pixel-ratio:1.25),(min-resolution:1.25dppx),(min-device-pixel-ratio:1.25){.gb_P::before,.gb_gb::before{display:inline-block;-webkit-transform:scale(0.5);-webkit-transform:scale(0.5);transform:scale(0.5);-webkit-transform-origin:left 0;-webkit-transform-origin:left 0;transform-origin:left 0}.gb_3 .gb_gb::before{-webkit-transform:scale(scale(0.416666667));-webkit-transform:scale(scale(0.416666667));transform:scale(scale(0.416666667))}}.gb_P:hover,.gb_P:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15);box-shadow:0 1px 0 rgba(0,0,0,.15)}.gb_P:active{-webkit-box-shadow:inset 0 2px 0 rgba(0,0,0,.15);box-shadow:inset 0 2px 0 rgba(0,0,0,.15)}.gb_P:active::after{background:rgba(0,0,0,.1);-webkit-border-radius:50%;border-radius:50%;content:"";display:block;height:100%}.gb_hb{cursor:pointer;line-height:40px;min-width:30px;opacity:.75;overflow:hidden;vertical-align:middle;text-overflow:ellipsis}.gb_B.gb_hb{width:auto}.gb_hb:hover,.gb_hb:focus{opacity:.85}.gb_hd .gb_hb,.gb_hd .gb_Wd{line-height:26px}#gb#gb.gb_hd a.gb_hb,.gb_hd .gb_Wd{font-size:11px;height:auto}.gb_ib{border-top:4px solid #000;border-left:4px dashed transparent;border-right:4px dashed transparent;display:inline-block;margin-left:6px;opacity:.75;vertical-align:middle}.gb_Za:hover .gb_ib{opacity:.85}.gb_Wa>.gb_z{padding:3px 3px 3px 4px}.gb_Xd.gb_od{color:#fff}.gb_1 .gb_hb,.gb_1 .gb_ib{opacity:1}#gb#gb.gb_1.gb_1 a.gb_hb,#gb#gb .gb_1.gb_1 a.gb_hb{color:#fff}.gb_1.gb_1 .gb_ib{border-top-color:#fff;opacity:1}.gb_ka .gb_P:hover,.gb_1 .gb_P:hover,.gb_ka .gb_P:focus,.gb_1 .gb_P:focus{-webkit-box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2);box-shadow:0 1px 0 rgba(0,0,0,.15),0 1px 2px rgba(0,0,0,.2)}.gb_Zd .gb_z,.gb_0d .gb_z{position:absolute;right:1px}.gb_z.gb_0,.gb_jb.gb_0,.gb_Za.gb_0{-webkit-flex:0 1 auto;-webkit-box-flex:0;flex:0 1 auto}.gb_1d.gb_2d .gb_hb{width:30px!important}.gb_3d{height:40px;position:absolute;right:-5px;top:-5px;width:40px}.gb_4d .gb_3d,.gb_5d .gb_3d{right:0;top:0}.gb_z .gb_B{padding:4px}.gb_S{display:none}sentinel{}</style><script nonce="">;this.gbar_={CONFIG:[[[0,"www.gstatic.com","og.qtm.en_US.v2pk7dVghog.2019.O","com.ng","en-GB","425",0,[4,2,"","","","793424555","0"],null,"dUugaLG-Idq-6-AP3JCo4QQ",null,0,"og.qtm.5bOMfS7uCn8.L.W.O","AA2YrTthfa-GW6nWNiVo32au3OStcP0_zg","AA2YrTs5z5IeveM3_8fj3UK_0H1gj7fqJg","",2,1,200,"NGA",null,null,"425","425",1,null,null,114591953,null,0,0],null,[1,0.1000000014901161,2,1],null,[1,0,0,null,"0","orioyeesther2019@gmail.com","","AIhRldK8w5FvKgj0RNEOPlJQwPKh6V26XJs0eeJjipqQ7nZdpFaLajeLQBs4u1DRvmQ1yOw2kC8D6f51kHERg1RWok5KOuU26w",0,0,0,""],[0,0,"",1,0,0,0,0,0,0,null,0,0,null,0,0,null,null,0,0,0,"","","","","","",null,0,0,0,0,0,null,null,null,"rgba(32,33,36,1)","rgba(255,255,255,1)",0,0,0,null,null,null,0],["%1$s (default)","Brand account",1,"%1$s (delegated)",1,null,83,"https://colab.research.google.com/drive/1GxAEOdWL568uMzUjdoXwNV13x4jAU5xu?authuser=$authuser",null,null,null,1,"https://accounts.google.com/ListAccounts?listPages=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en-GB\u0026ts=250",0,"dashboard",null,null,null,null,"Profile","",1,null,"Signed out","https://accounts.google.com/AccountChooser?source=ogb\u0026continue=$continue\u0026Email=$email\u0026ec=GAhAqQM","https://accounts.google.com/RemoveLocalAccount?source=ogb","Remove","Sign in",0,1,1,0,1,1,0,null,null,null,"Session expired",null,null,null,"Visitor",null,"Default","Delegated","Sign out of all accounts",0,null,null,0,null,null,"myaccount.google.com","https",0,1,0],null,["1","gci_91f30755d6a6b787dcc2a4062e6e9824.js","googleapis.client:gapi.iframes","0","en-GB"],null,null,null,null,["m;/_/scs/abc-static/_/js/k=gapi.gapi.en.GJa4oir6WlA.O/d=1/rs=AHpOoo-oT18V72om9ubISB9Na8GvbQT5cg/m=__features__","https://apis.google.com","","","1","",null,1,"es_plusone_gc_20250803.0_p0","en-GB",null,0],[0.009999999776482582,"com.ng","425",[null,"","0",null,1,5184000,null,null,"",null,null,null,null,null,0,null,0,null,1,0,0,0,null,null,0,0,null,0,0,0,0,0],null,null,null,0],[1,null,null,40400,425,"NGA","en-GB","793424555.0",8,null,1,0,null,null,null,null,"105071010,105071012",null,null,null,"dUugaLG-Idq-6-AP3JCo4QQ",0,0,0,null,2,5,"nn",7,0,0,null,null,1,114591953,0,0],[[null,null,null,"https://www.gstatic.com/og/_/js/k=og.qtm.en_US.v2pk7dVghog.2019.O/rt=j/m=qabr,qgl,q_dnp,qcwid,qbd,qapid,qads,qrcd,q_dg/exm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/rs=AA2YrTthfa-GW6nWNiVo32au3OStcP0_zg"],[null,null,null,"https://www.gstatic.com/og/_/ss/k=og.qtm.5bOMfS7uCn8.L.W.O/m=qcwid,qba/excm=qaaw,qadd,qaid,qein,qhaw,qhba,qhbr,qhch,qhga,qhid,qhin/d=1/ed=1/ct=zgms/rs=AA2YrTs5z5IeveM3_8fj3UK_0H1gj7fqJg"]],null,null,null,[[[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/account?amb=1"],0,414,436,57,4,1,0,0,65,66,8000,"https://accounts.google.com/SignOutOptions?hl=en-GB\u0026continue=https://colab.research.google.com/drive/1GxAEOdWL568uMzUjdoXwNV13x4jAU5xu\u0026ec=GBRAqQM",68,2,null,null,1,113,"Something went wrong.%1$s Refresh to try again or %2$schoose another account%3$s.",3,null,null,75,0,null,null,null,null,null,null,null,"/widget/account",["https","myaccount.google.com",0,32,83,0],0,0,1,["Critical security alert","Important account alert","Storage usage alert",null,1,0],0,1,null,1,1,null,null,null,null,0,0,0,null,0,0,null,null,null,null,null,null,null,null,null,0],[null,null,[null,null,null,"https://ogs.google.com/u/0/widget/callout/sid?dc=1"],null,280,420,70,25,0,null,0,null,null,8000,null,71,4,null,null,null,null,null,null,null,null,76,null,null,null,107,108,109,"",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,0]],null,null,"425","425",1,0,null,"en-GB",0,["https://colab.research.google.com/drive/1GxAEOdWL568uMzUjdoXwNV13x4jAU5xu?authuser=$authuser","https://accounts.google.com/AddSession?hl=en-GB\u0026continue=https://colab.research.google.com/drive/1GxAEOdWL568uMzUjdoXwNV13x4jAU5xu\u0026ec=GAlAqQM","https://accounts.google.com/Logout?hl=en-GB\u0026continue=https://colab.research.google.com/drive/1GxAEOdWL568uMzUjdoXwNV13x4jAU5xu\u0026timeStmp=1755335541\u0026secTok=.AG5fkS8-4VY2q6Xll_0WRR9dppCSbcWDZw\u0026ec=GAdAqQM","https://accounts.google.com/ListAccounts?listPages=0\u0026pid=425\u0026gpsia=1\u0026source=ogb\u0026atic=1\u0026mo=1\u0026mn=1\u0026hl=en-GB\u0026ts=250",0,0,"",0,0,null,0,0,"https://accounts.google.com/ServiceLogin?passive=true\u0026continue=https%3A%2F%2Fcolab.research.google.com%2Fdrive%2F1GxAEOdWL568uMzUjdoXwNV13x4jAU5xu\u0026ec=GAZAqQM",null,null,0,null,null,null,0],0,0,0,[null,"",null,null,null,1,null,0,0,"","","","https://ogads-pa.clients6.google.com",0,0,0,"","",0,0,null,86400,null,1,null,null,0,null,0,0,"8559284470",0,0,0],0,null,null,null,1,0,"orioyeesther2019@gmail.com",0],null,[["mousedown","touchstart","touchmove","wheel","keydown"],300000],[[null,null,null,"https://accounts.google.com/RotateCookiesPage"],3,null,null,null,0,1]]],};this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_._F_toggles_initialize=function(a){(typeof globalThis!=="undefined"?globalThis:typeof self!=="undefined"?self:this)._F_toggles_gbar_=a||[]};(0,_._F_toggles_initialize)([]);
/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var ja,pa,qa,ua,wa,xa,Fa,Ga,$a,cb,eb,jb,fb,lb,rb,Db,Eb,Fb,Gb;_.aa=function(a,b){if(Error.captureStackTrace)Error.captureStackTrace(this,_.aa);else{const c=Error().stack;c&&(this.stack=c)}a&&(this.message=String(a));b!==void 0&&(this.cause=b)};_.ba=function(a){a.zk=!0;return a};_.ia=function(a){var b=a;if(da(b)){if(!/^\s*(?:-?[1-9]\d*|0)?\s*$/.test(b))throw Error(String(b));}else if(ea(b)&&!Number.isSafeInteger(b))throw Error(String(b));return fa?BigInt(a):a=ha(a)?a?"1":"0":da(a)?a.trim()||"0":String(a)};
ja=function(a,b){if(a.length>b.length)return!1;if(a.length<b.length||a===b)return!0;for(let c=0;c<a.length;c++){const d=a[c],e=b[c];if(d>e)return!1;if(d<e)return!0}};_.ka=function(a){_.t.setTimeout(()=>{throw a;},0)};_.ma=function(){return _.la().toLowerCase().indexOf("webkit")!=-1};_.la=function(){var a=_.t.navigator;return a&&(a=a.userAgent)?a:""};pa=function(a){if(!na||!oa)return!1;for(let b=0;b<oa.brands.length;b++){const {brand:c}=oa.brands[b];if(c&&c.indexOf(a)!=-1)return!0}return!1};
_.u=function(a){return _.la().indexOf(a)!=-1};qa=function(){return na?!!oa&&oa.brands.length>0:!1};_.ra=function(){return qa()?!1:_.u("Opera")};_.sa=function(){return qa()?!1:_.u("Trident")||_.u("MSIE")};_.ta=function(){return _.u("Firefox")||_.u("FxiOS")};_.va=function(){return _.u("Safari")&&!(ua()||(qa()?0:_.u("Coast"))||_.ra()||(qa()?0:_.u("Edge"))||(qa()?pa("Microsoft Edge"):_.u("Edg/"))||(qa()?pa("Opera"):_.u("OPR"))||_.ta()||_.u("Silk")||_.u("Android"))};
ua=function(){return qa()?pa("Chromium"):(_.u("Chrome")||_.u("CriOS"))&&!(qa()?0:_.u("Edge"))||_.u("Silk")};wa=function(){return na?!!oa&&!!oa.platform:!1};xa=function(){return _.u("iPhone")&&!_.u("iPod")&&!_.u("iPad")};_.ya=function(){return xa()||_.u("iPad")||_.u("iPod")};_.za=function(){return wa()?oa.platform==="macOS":_.u("Macintosh")};_.Ba=function(a,b){return _.Aa(a,b)>=0};_.Ca=function(a,b=!1){return b&&Symbol.for&&a?Symbol.for(a):a!=null?Symbol(a):Symbol()};
_.Ea=function(a,b){return b===void 0?a.j!==Da&&!!(2&(a.fa[_.v]|0)):!!(2&b)&&a.j!==Da};Fa=function(a){return a};Ga=function(a,b){a.__closure__error__context__984382||(a.__closure__error__context__984382={});a.__closure__error__context__984382.severity=b};_.Ha=function(a){a=Error(a);Ga(a,"warning");return a};_.Ja=function(a,b){if(a!=null){var c;var d=(c=Ia)!=null?c:Ia={};c=d[a]||0;c>=b||(d[a]=c+1,a=Error(),Ga(a,"incident"),_.ka(a))}};
_.La=function(a){if(typeof a!=="boolean")throw Error("k`"+_.Ka(a)+"`"+a);return a};_.Ma=function(a){if(a==null||typeof a==="boolean")return a;if(typeof a==="number")return!!a};_.Oa=function(a){if(!(0,_.Na)(a))throw _.Ha("enum");return a|0};_.Pa=function(a){return a==null?a:(0,_.Na)(a)?a|0:void 0};_.Qa=function(a){if(typeof a!=="number")throw _.Ha("int32");if(!(0,_.Na)(a))throw _.Ha("int32");return a|0};_.Ra=function(a){if(a!=null&&typeof a!=="string")throw Error();return a};
_.Sa=function(a){return a==null||typeof a==="string"?a:void 0};_.Va=function(a,b,c){if(a!=null&&a[_.Ta]===_.Ua)return a;if(Array.isArray(a)){var d=a[_.v]|0;c=d|c&32|c&2;c!==d&&(a[_.v]=c);return new b(a)}};_.Ya=function(a){const b=_.Wa(_.Xa);return b?a[b]:void 0};$a=function(a,b){b<100||_.Ja(Za,1)};
cb=function(a,b,c,d){const e=d!==void 0;d=!!d;var f=_.Wa(_.Xa),g;!e&&f&&(g=a[f])&&g.xd($a);f=[];var h=a.length;let k;g=4294967295;let l=!1;const m=!!(b&64),p=m?b&128?0:-1:void 0;if(!(b&1||(k=h&&a[h-1],k!=null&&typeof k==="object"&&k.constructor===Object?(h--,g=h):k=void 0,!m||b&128||e))){l=!0;var r;g=((r=ab)!=null?r:Fa)(g-p,p,a,k,void 0)+p}b=void 0;for(r=0;r<h;r++){let w=a[r];if(w!=null&&(w=c(w,d))!=null)if(m&&r>=g){const D=r-p;var q=void 0;((q=b)!=null?q:b={})[D]=w}else f[r]=w}if(k)for(let w in k){q=
k[w];if(q==null||(q=c(q,d))==null)continue;h=+w;let D;if(m&&!Number.isNaN(h)&&(D=h+p)<g)f[D]=q;else{let Q;((Q=b)!=null?Q:b={})[w]=q}}b&&(l?f.push(b):f[g]=b);e&&_.Wa(_.Xa)&&(a=_.Ya(a))&&"function"==typeof _.bb&&a instanceof _.bb&&(f[_.Xa]=a.i());return f};
eb=function(a){switch(typeof a){case "number":return Number.isFinite(a)?a:""+a;case "bigint":return(0,_.db)(a)?Number(a):""+a;case "boolean":return a?1:0;case "object":if(Array.isArray(a)){const b=a[_.v]|0;return a.length===0&&b&1?void 0:cb(a,b,eb)}if(a!=null&&a[_.Ta]===_.Ua)return fb(a);if("function"==typeof _.gb&&a instanceof _.gb)return a.j();return}return a};jb=function(a,b){if(b){ab=b==null||b===Fa||b[hb]!==ib?Fa:b;try{return fb(a)}finally{ab=void 0}}return fb(a)};
fb=function(a){a=a.fa;return cb(a,a[_.v]|0,eb)};
_.mb=function(a,b,c,d=0){if(a==null){var e=32;c?(a=[c],e|=128):a=[];b&&(e=e&-8380417|(b&1023)<<13)}else{if(!Array.isArray(a))throw Error("l");e=a[_.v]|0;if(kb&&1&e)throw Error("m");2048&e&&!(2&e)&&lb();if(e&256)throw Error("n");if(e&64)return d!==0||e&2048||(a[_.v]=e|2048),a;if(c&&(e|=128,c!==a[0]))throw Error("o");a:{c=a;e|=64;var f=c.length;if(f){var g=f-1;const k=c[g];if(k!=null&&typeof k==="object"&&k.constructor===Object){b=e&128?0:-1;g-=b;if(g>=1024)throw Error("q");for(var h in k)if(f=+h,f<
g)c[f+b]=k[h],delete k[h];else break;e=e&-8380417|(g&1023)<<13;break a}}if(b){h=Math.max(b,f-(e&128?0:-1));if(h>1024)throw Error("r");e=e&-8380417|(h&1023)<<13}}}e|=64;d===0&&(e|=2048);a[_.v]=e;return a};lb=function(){if(kb)throw Error("p");_.Ja(nb,5)};
rb=function(a,b){if(typeof a!=="object")return a;if(Array.isArray(a)){var c=a[_.v]|0;a.length===0&&c&1?a=void 0:c&2||(!b||4096&c||16&c?a=_.ob(a,c,!1,b&&!(c&16)):(a[_.v]|=34,c&4&&Object.freeze(a)));return a}if(a!=null&&a[_.Ta]===_.Ua)return b=a.fa,c=b[_.v]|0,_.Ea(a,c)?a:_.pb(a,b,c)?_.qb(a,b):_.ob(b,c);if("function"==typeof _.gb&&a instanceof _.gb)return a};_.qb=function(a,b,c){a=new a.constructor(b);c&&(a.j=Da);a.o=Da;return a};
_.ob=function(a,b,c,d){d!=null||(d=!!(34&b));a=cb(a,b,rb,d);d=32;c&&(d|=2);b=b&8380609|d;a[_.v]=b;return a};_.tb=function(a){const b=a.fa,c=b[_.v]|0;return _.Ea(a,c)?_.pb(a,b,c)?_.qb(a,b,!0):new a.constructor(_.ob(b,c,!1)):a};_.ub=function(a){if(a.j!==Da)return!1;var b=a.fa;b=_.ob(b,b[_.v]|0);b[_.v]|=2048;a.fa=b;a.j=void 0;a.o=void 0;return!0};_.vb=function(a){if(!_.ub(a)&&_.Ea(a,a.fa[_.v]|0))throw Error();};_.wb=function(a,b){b===void 0&&(b=a[_.v]|0);b&32&&!(b&4096)&&(a[_.v]=b|4096)};
_.pb=function(a,b,c){return c&2?!0:c&32&&!(c&4096)?(b[_.v]=c|2,a.j=Da,!0):!1};_.xb=function(a,b,c,d,e){const f=c+(e?0:-1);var g=a.length-1;if(g>=1+(e?0:-1)&&f>=g){const h=a[g];if(h!=null&&typeof h==="object"&&h.constructor===Object)return h[c]=d,b}if(f<=g)return a[f]=d,b;if(d!==void 0){let h;g=((h=b)!=null?h:b=a[_.v]|0)>>13&1023||536870912;c>=g?d!=null&&(a[g+(e?0:-1)]={[c]:d}):a[f]=d}return b};
_.zb=function(a,b,c,d,e){let f=!1;d=_.yb(a,d,e,g=>{const h=_.Va(g,c,b);f=h!==g&&h!=null;return h});if(d!=null)return f&&!_.Ea(d)&&_.wb(a,b),d};_.Ab=function(){const a=class{constructor(){throw Error();}};Object.setPrototypeOf(a,a.prototype);return a};_.x=function(a,b){return a!=null?!!a:!!b};_.y=function(a,b){b==void 0&&(b="");return a!=null?a:b};_.Bb=function(a,b,c){for(const d in a)b.call(c,a[d],d,a)};_.Cb=function(a){for(const b in a)return!1;return!0};Db=Object.defineProperty;
Eb=function(a){a=["object"==typeof globalThis&&globalThis,a,"object"==typeof window&&window,"object"==typeof self&&self,"object"==typeof global&&global];for(var b=0;b<a.length;++b){var c=a[b];if(c&&c.Math==Math)return c}throw Error("a");};Fb=Eb(this);Gb=function(a,b){if(b)a:{var c=Fb;a=a.split(".");for(var d=0;d<a.length-1;d++){var e=a[d];if(!(e in c))break a;c=c[e]}a=a[a.length-1];d=c[a];b=b(d);b!=d&&b!=null&&Db(c,a,{configurable:!0,writable:!0,value:b})}};Gb("globalThis",function(a){return a||Fb});
Gb("Symbol.dispose",function(a){return a?a:Symbol("b")});Gb("Promise.prototype.finally",function(a){return a?a:function(b){return this.then(function(c){return Promise.resolve(b()).then(function(){return c})},function(c){return Promise.resolve(b()).then(function(){throw c;})})}});
Gb("Array.prototype.flat",function(a){return a?a:function(b){b=b===void 0?1:b;var c=[];Array.prototype.forEach.call(this,function(d){Array.isArray(d)&&b>0?(d=Array.prototype.flat.call(d,b-1),c.push.apply(c,d)):c.push(d)});return c}});var Jb,Kb,Nb;_.Hb=_.Hb||{};_.t=this||self;Jb=function(a,b){var c=_.Ib("WIZ_global_data.oxN3nb");a=c&&c[a];return a!=null?a:b};Kb=_.t._F_toggles_gbar_||[];_.Ib=function(a,b){a=a.split(".");b=b||_.t;for(var c=0;c<a.length;c++)if(b=b[a[c]],b==null)return null;return b};_.Ka=function(a){var b=typeof a;return b!="object"?b:a?Array.isArray(a)?"array":b:"null"};_.Lb=function(a){var b=typeof a;return b=="object"&&a!=null||b=="function"};_.Mb="closure_uid_"+(Math.random()*1E9>>>0);
Nb=function(a,b,c){return a.call.apply(a.bind,arguments)};_.z=function(a,b,c){_.z=Nb;return _.z.apply(null,arguments)};_.Ob=function(a,b){var c=Array.prototype.slice.call(arguments,1);return function(){var d=c.slice();d.push.apply(d,arguments);return a.apply(this,d)}};_.A=function(a,b){a=a.split(".");for(var c=_.t,d;a.length&&(d=a.shift());)a.length||b===void 0?c[d]&&c[d]!==Object.prototype[d]?c=c[d]:c=c[d]={}:c[d]=b};_.Wa=function(a){return a};
_.B=function(a,b){function c(){}c.prototype=b.prototype;a.X=b.prototype;a.prototype=new c;a.prototype.constructor=a;a.nk=function(d,e,f){for(var g=Array(arguments.length-2),h=2;h<arguments.length;h++)g[h-2]=arguments[h];return b.prototype[e].apply(d,g)}};_.B(_.aa,Error);_.aa.prototype.name="CustomError";var Pb=!!(Kb[0]>>15&1),Qb=!!(Kb[0]&1024),Rb=!!(Kb[0]>>16&1),Sb=!!(Kb[0]&128);var Tb=Jb(1,!0),na=Pb?Rb:Jb(610401301,!1),kb=Pb?Qb||!Sb:Jb(748402147,Tb);_.Ub=_.ba(a=>a!==null&&a!==void 0);var ea=_.ba(a=>typeof a==="number"),da=_.ba(a=>typeof a==="string"),ha=_.ba(a=>typeof a==="boolean");var fa=typeof _.t.BigInt==="function"&&typeof _.t.BigInt(0)==="bigint";var Xb,Vb,Yb,Wb;_.db=_.ba(a=>fa?a>=Vb&&a<=Wb:a[0]==="-"?ja(a,Xb):ja(a,Yb));Xb=Number.MIN_SAFE_INTEGER.toString();Vb=fa?BigInt(Number.MIN_SAFE_INTEGER):void 0;Yb=Number.MAX_SAFE_INTEGER.toString();Wb=fa?BigInt(Number.MAX_SAFE_INTEGER):void 0;_.Zb=typeof TextDecoder!=="undefined";_.$b=typeof TextEncoder!=="undefined";var oa,ac=_.t.navigator;oa=ac?ac.userAgentData||null:null;_.Aa=function(a,b){return Array.prototype.indexOf.call(a,b,void 0)};_.bc=function(a,b,c){Array.prototype.forEach.call(a,b,c)};_.cc=function(a,b){return Array.prototype.some.call(a,b,void 0)};_.dc=function(a){_.dc[" "](a);return a};_.dc[" "]=function(){};var rc;_.ec=_.ra();_.fc=_.sa();_.hc=_.u("Edge");_.ic=_.u("Gecko")&&!(_.ma()&&!_.u("Edge"))&&!(_.u("Trident")||_.u("MSIE"))&&!_.u("Edge");_.jc=_.ma()&&!_.u("Edge");_.kc=_.za();_.lc=wa()?oa.platform==="Windows":_.u("Windows");_.mc=wa()?oa.platform==="Android":_.u("Android");_.nc=xa();_.oc=_.u("iPad");_.pc=_.u("iPod");_.qc=_.ya();
a:{let a="";const b=function(){const c=_.la();if(_.ic)return/rv:([^\);]+)(\)|;)/.exec(c);if(_.hc)return/Edge\/([\d\.]+)/.exec(c);if(_.fc)return/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(c);if(_.jc)return/WebKit\/(\S+)/.exec(c);if(_.ec)return/(?:Version)[ \/]?(\S+)/.exec(c)}();b&&(a=b?b[1]:"");if(_.fc){var sc;const c=_.t.document;sc=c?c.documentMode:void 0;if(sc!=null&&sc>parseFloat(a)){rc=String(sc);break a}}rc=a}_.tc=rc;_.uc=_.ta();_.vc=xa()||_.u("iPod");_.wc=_.u("iPad");_.xc=_.u("Android")&&!(ua()||_.ta()||_.ra()||_.u("Silk"));_.yc=ua();_.zc=_.va()&&!_.ya();var Za,nb,hb;_.Xa=_.Ca();_.Ac=_.Ca();Za=_.Ca();_.Bc=_.Ca();nb=_.Ca();_.Ta=_.Ca("m_m",!0);hb=_.Ca();_.Cc=_.Ca();var Ec;_.v=_.Ca("jas",!0);Ec=[];Ec[_.v]=7;_.Dc=Object.freeze(Ec);var Da;_.Ua={};Da={};_.Fc=Object.freeze({});var ib={};var Ia=void 0;_.Gc=typeof BigInt==="function"?BigInt.asIntN:void 0;_.Hc=Number.isSafeInteger;_.Na=Number.isFinite;_.Ic=Math.trunc;var ab;_.Jc=_.ia(0);_.Kc={};_.Lc=function(a,b,c,d,e){b=_.yb(a.fa,b,c,e);if(b!==null||d&&a.o!==Da)return b};_.yb=function(a,b,c,d){if(b===-1)return null;const e=b+(c?0:-1),f=a.length-1;let g,h;if(!(f<1+(c?0:-1))){if(e>=f)if(g=a[f],g!=null&&typeof g==="object"&&g.constructor===Object)c=g[b],h=!0;else if(e===f)c=g;else return;else c=a[e];if(d&&c!=null){d=d(c);if(d==null)return d;if(!Object.is(d,c))return h?g[b]=d:a[e]=d,d}return c}};_.Mc=function(a,b,c,d){_.vb(a);const e=a.fa;_.xb(e,e[_.v]|0,b,c,d);return a};
_.C=function(a,b,c,d){let e=a.fa,f=e[_.v]|0;b=_.zb(e,f,b,c,d);if(b==null)return b;f=e[_.v]|0;if(!_.Ea(a,f)){const g=_.tb(b);g!==b&&(_.ub(a)&&(e=a.fa,f=e[_.v]|0),b=g,f=_.xb(e,f,c,b,d),_.wb(e,f))}return b};_.E=function(a,b,c){c==null&&(c=void 0);_.Mc(a,b,c);c&&!_.Ea(c)&&_.wb(a.fa);return a};_.Nc=function(a,b,c,d){return _.Pa(_.Lc(a,b,c,d))};_.F=function(a,b,c=!1,d){let e;return(e=_.Ma(_.Lc(a,b,d)))!=null?e:c};_.G=function(a,b,c="",d){let e;return(e=_.Sa(_.Lc(a,b,d)))!=null?e:c};
_.I=function(a,b,c){return _.Sa(_.Lc(a,b,c,_.Kc))};_.J=function(a,b,c,d){return _.Mc(a,b,c==null?c:_.La(c),d)};_.K=function(a,b,c){return _.Mc(a,b,c==null?c:_.Qa(c))};_.L=function(a,b,c,d){return _.Mc(a,b,_.Ra(c),d)};_.N=function(a,b,c,d){return _.Mc(a,b,c==null?c:_.Oa(c),d)};_.O=class{constructor(a,b,c){this.fa=_.mb(a,b,c)}toJSON(){return jb(this)}wa(a){return JSON.stringify(jb(this,a))}};_.O.prototype[_.Ta]=_.Ua;_.O.prototype.toString=function(){return this.fa.toString()};_.Oc=_.Ab();_.Pc=_.Ab();_.Rc=_.Ab();_.Sc=Symbol();var Tc=class extends _.O{constructor(a){super(a)}};_.Uc=class extends _.O{constructor(a){super(a)}D(a){return _.K(this,3,a)}};var Vc=class extends _.O{constructor(a){super(a)}Wb(a){return _.L(this,24,a)}};_.Wc=class extends _.O{constructor(a){super(a)}};_.P=function(){this.qa=this.qa;this.Y=this.Y};_.P.prototype.qa=!1;_.P.prototype.isDisposed=function(){return this.qa};_.P.prototype.dispose=function(){this.qa||(this.qa=!0,this.R())};_.P.prototype[Symbol.dispose]=function(){this.dispose()};_.P.prototype.R=function(){if(this.Y)for(;this.Y.length;)this.Y.shift()()};var Xc=class extends _.P{constructor(){var a=window;super();this.o=a;this.i=[];this.j={}}resolve(a){let b=this.o;a=a.split(".");const c=a.length;for(let d=0;d<c;++d)if(b[a[d]])b=b[a[d]];else return null;return b instanceof Function?b:null}tb(){const a=this.i.length,b=this.i,c=[];for(let d=0;d<a;++d){const e=b[d].i(),f=this.resolve(e);if(f&&f!=this.j[e])try{b[d].tb(f)}catch(g){}else c.push(b[d])}this.i=c.concat(b.slice(a))}};var Zc=class extends _.P{constructor(){var a=_.Yc;super();this.o=a;this.A=this.i=null;this.v=0;this.B={};this.j=!1;a=window.navigator.userAgent;a.indexOf("MSIE")>=0&&a.indexOf("Trident")>=0&&(a=/\b(?:MSIE|rv)[: ]([^\);]+)(\)|;)/.exec(a))&&a[1]&&parseFloat(a[1])<9&&(this.j=!0)}C(a,b){this.i=b;this.A=a;b.preventDefault?b.preventDefault():b.returnValue=!1}};_.$c=class extends _.O{constructor(a){super(a)}};var ad=class extends _.O{constructor(a){super(a)}};var dd;_.bd=function(a,b,c=98,d=new _.Uc){if(a.i){const e=new Tc;_.L(e,1,b.message);_.L(e,2,b.stack);_.K(e,3,b.lineNumber);_.N(e,5,1);_.E(d,40,e);a.i.log(c,d)}};dd=class{constructor(){var a=cd;this.i=null;_.F(a,4,!0)}log(a,b,c=new _.Uc){_.bd(this,a,98,c)}};var ed,fd;ed=function(a){if(a.o.length>0){var b=a.i!==void 0,c=a.j!==void 0;if(b||c){b=b?a.v:a.A;c=a.o;a.o=[];try{_.bc(c,b,a)}catch(d){console.error(d)}}}};_.gd=class{constructor(a){this.i=a;this.j=void 0;this.o=[]}then(a,b,c){this.o.push(new fd(a,b,c));ed(this)}resolve(a){if(this.i!==void 0||this.j!==void 0)throw Error("v");this.i=a;ed(this)}reject(a){if(this.i!==void 0||this.j!==void 0)throw Error("v");this.j=a;ed(this)}v(a){a.j&&a.j.call(a.i,this.i)}A(a){a.o&&a.o.call(a.i,this.j)}};
fd=class{constructor(a,b,c){this.j=a;this.o=b;this.i=c}};_.hd=a=>{var b="qc";if(a.qc&&a.hasOwnProperty(b))return a.qc;b=new a;return a.qc=b};_.R=class{constructor(){this.v=new _.gd;this.i=new _.gd;this.D=new _.gd;this.B=new _.gd;this.C=new _.gd;this.A=new _.gd;this.o=new _.gd;this.j=new _.gd;this.F=new _.gd;this.G=new _.gd}K(){return this.v}qa(){return this.i}O(){return this.D}M(){return this.B}P(){return this.C}L(){return this.A}Y(){return this.o}J(){return this.j}N(){return this.F}static i(){return _.hd(_.R)}};var ld;_.jd=function(){return _.C(_.id,Vc,1)};_.kd=function(){return _.C(_.id,_.Wc,5)};ld=class extends _.O{constructor(a){super(a)}};var md;window.gbar_&&window.gbar_.CONFIG?md=window.gbar_.CONFIG[0]||{}:md=[];_.id=new ld(md);var cd=_.C(_.id,ad,3)||new ad;_.jd()||new Vc;_.Yc=new dd;_.A("gbar_._DumpException",function(a){_.Yc?_.Yc.log(a):console.error(a)});_.nd=new Zc;var pd;_.qd=function(a,b){var c=_.od.i();if(a in c.i){if(c.i[a]!=b)throw new pd;}else{c.i[a]=b;const h=c.j[a];if(h)for(let k=0,l=h.length;k<l;k++){b=h[k];var d=c.i;delete b.i[a];if(_.Cb(b.i)){for(var e=b.j.length,f=Array(e),g=0;g<e;g++)f[g]=d[b.j[g]];b.o.apply(b.v,f)}}delete c.j[a]}};_.od=class{constructor(){this.i={};this.j={}}static i(){return _.hd(_.od)}};_.rd=class extends _.aa{constructor(){super()}};pd=class extends _.rd{};_.A("gbar.A",_.gd);_.gd.prototype.aa=_.gd.prototype.then;_.A("gbar.B",_.R);_.R.prototype.ba=_.R.prototype.qa;_.R.prototype.bb=_.R.prototype.O;_.R.prototype.bd=_.R.prototype.P;_.R.prototype.bf=_.R.prototype.K;_.R.prototype.bg=_.R.prototype.M;_.R.prototype.bh=_.R.prototype.L;_.R.prototype.bj=_.R.prototype.Y;_.R.prototype.bk=_.R.prototype.J;_.R.prototype.bl=_.R.prototype.N;_.A("gbar.a",_.R.i());window.gbar&&window.gbar.ap&&window.gbar.ap(window.gbar.a);var sd=new Xc;_.qd("api",sd);
var td=_.kd()||new _.Wc,ud=window,vd=_.y(_.I(td,8));ud.__PVT=vd;_.qd("eq",_.nd);
}catch(e){_._DumpException(e)}
try{
_.wd=class extends _.O{constructor(a){super(a)}};
}catch(e){_._DumpException(e)}
try{
var xd=class extends _.O{constructor(a){super(a)}};var yd=class extends _.P{constructor(){super();this.j=[];this.i=[]}o(a,b){this.j.push({features:a,options:b!=null?b:null})}init(a,b,c){window.gapi={};const d=window.___jsl={};d.h=_.y(_.I(a,1));_.Ma(_.Lc(a,12))!=null&&(d.dpo=_.x(_.F(a,12)));d.ms=_.y(_.I(a,2));d.m=_.y(_.I(a,3));d.l=[];_.G(b,1)&&(a=_.I(b,3))&&this.i.push(a);_.G(c,1)&&(c=_.I(c,2))&&this.i.push(c);_.A("gapi.load",(0,_.z)(this.o,this));return this}};var zd=_.C(_.id,_.$c,14);if(zd){var Bd=_.C(_.id,_.wd,9)||new _.wd,Cd=new xd,Dd=new yd;Dd.init(zd,Bd,Cd);_.qd("gs",Dd)};
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><script nonce="">try {const preferences = JSON.parse(window.localStorage.getItem("datalab_prefs_orioyeesther2019@gmail.com")); document.querySelector('html') .setAttribute('theme', preferences['siteTheme'] || 'default');} catch (e) {}</script><script nonce="">window.performance.mark('head_start');</script><link rel="stylesheet" href="./Orioye.E.project8.ipy_files/bundle.css"><script nonce="">var colabVersionTag = 'colab_20250814-060056_RC00_794972295'; var colabScsVersion = '5974b39383863f189d8033cb6eeaf562'; var hl = 'en-GB'; var colabExperiments = JSON.parse('\x7b\x22add_df_vars_in_ai_conversation_context\x22: false, \x22add_df_vars_in_ai_generate_context\x22: false, \x22add_notebook_diffs_to_chat_history\x22: true, \x22add_nvidia_cudf_facts_to_chat_context\x22: true, \x22add_prompt_cell\x22: false, \x22agent_client_update_task_max_request_size_bytes\x22: 10000000, \x22agent_scroll_delay_ms\x22: 200, \x22agent_update_task_max_request_size_bytes\x22: 10000000, \x22ai_banner\x22: false, \x22ai_characters_per_token\x22: 3.0, \x22ai_prompt_token_limit\x22: 32000, \x22ai_unsubscribed_warning\x22: false, \x22ai_user_input_char_limit\x22: 2000, \x22aida_complete_code_model_id\x22: \x22\x22, \x22aida_converse_max_facts\x22: 20, \x22aida_do_conversation_model_id\x22: \x22aida_v3p1s_streaming\x22, \x22aida_dsa_model_strategy\x22: -1, \x22aida_generate_code_model_id\x22: \x22aida_v3p1s\x22, \x22aida_generate_code_no_max_tokens\x22: true, \x22allow_dsa_page_interaction\x22: true, \x22allow_readonly_cells\x22: true, \x22allow_subpaths_in_kernel_url\x22: false, \x22allowed_public_url_domains\x22: \x5b\x22huggingface.co\x22, \x22dagshub.com\x22, \x22storage.googleapis.com\x22\x5d, \x22backend_url_allowlist\x22: \x5b\x22localhost\x22, \x22127.0.0.1\x22, \x22\x5b::1\x5d\x22, \x22kkb-production.jupyter-proxy.kaggle.net\x22, \x22kkb-staging.jupyter-proxy.kaggle.net\x22, \x22isolabs-kernels.corp.goog\x22\x5d, \x22backend_version\x22: \x22next\x22, \x22backtracking_strategy\x22: \x22non-literals\x22, \x22bigquery_sql_engine\x22: false, \x22bigquery_sql_engine_library\x22: \x22\x22, \x22ccu_info_abort_timeout_ms\x22: 3000, \x22cell_tags\x22: false, \x22cell_ui_refresh\x22: false, \x22chat_explain_error_temp\x22: \x221.0\x22, \x22chat_model_id_override\x22: \x22\x22, \x22classified_generate\x22: false, \x22classroom_iframe_parent_origin\x22: \x22\x22, \x22client_trim_completion_text\x22: 400, \x22clone_notebook_link\x22: true, \x22cloud_origin\x22: \x22\x22, \x22cloud_run\x22: false, \x22code_report_millis\x22: 600000, \x22colab_fetch_try_reauth\x22: false, \x22comment_poll_long\x22: 900000, \x22comment_poll_short\x22: 60000, \x22complete_code\x22: true, \x22compose_skip_suffix_check\x22: false, \x22composer\x22: true, \x22composer_auto_code\x22: true, \x22composer_autocomplete\x22: false, \x22composer_bigquery_context\x22: false, \x22composer_context_max_variable_length\x22: 500000, \x22composer_early_stopping_for_image_truncation\x22: false, \x22composer_focused_cell_context\x22: true, \x22composer_fp_context\x22: false, \x22composer_generate_code\x22: true, \x22composer_kernel_files_in_context\x22: true, \x22composer_model_strategy\x22: 0, \x22composer_show_debug_info\x22: false, \x22composer_survey\x22: true, \x22composer_transform_code\x22: true, \x22composer_visible_cells_context\x22: false, \x22converse_notebook_context_length\x22: 40000, \x22copy_cell_output\x22: false, \x22corp_third_party_widgets\x22: false, \x22crawler\x22: false, \x22create_gemini_api_key\x22: false, \x22critique_comments\x22: false, \x22data_inspector\x22: false, \x22dbu\x22: \x22\x22, \x22debug_adapter\x22: false, \x22debug_external\x22: \x22external\x22, \x22debug_prod\x22: \x22prod\x22, \x22debugger_server_side_globals\x22: true, \x22dep_cells_commands\x22: true, \x22dep_cells_enabled\x22: false, \x22dep_graph\x22: false, \x22deprecate_prompt\x22: true, \x22deprecate_unpin\x22: false, \x22development\x22: false, \x22dialog_ui_refresh\x22: false, \x22document_change_poll_interval\x22: 30000, \x22drive_anon_api_key\x22: \x22AIzaSyB10s2vWUTwP0pj20wZoxmpZIt3rRodYeg\x22, \x22drive_api_key\x22: \x22AIzaSyCN_sSPJMpYrAzC5AtTrltNC8oRmLtoqBk\x22, \x22drive_background_save_project_number\x22: \x22948411933973\x22, \x22drive_realtime_project_number\x22: \x22903414543955\x22, \x22drop_chat_links\x22: true, \x22dsa\x22: true, \x22dsa_file_not_sent_survey_timeout\x22: 60000, \x22dsa_markdown_cells\x22: false, \x22dsa_sample_datasets_toast\x22: true, \x22embedded_toolbar_customization\x22: true, \x22embedded_use_websockets\x22: false, \x22embedding_app\x22: \x22\x22, \x22enable_adhoc_backends\x22: false, \x22enable_agent_connect_to_new_vm\x22: true, \x22enable_cell_pair_slides\x22: false, \x22enable_composer_changeset_stacking\x22: false, \x22enable_composer_code_report\x22: false, \x22enable_composer_suggestion_chips\x22: false, \x22enable_dasher_subscription_ui\x22: true, \x22enable_edu_subscription_ui\x22: true, \x22enable_more_reprs\x22: true, \x22enable_mpp_orc_model_overrides\x22: true, \x22enable_rt_on_create\x22: false, \x22execution_status_propagation\x22: true, \x22explain_error_model_id_override\x22: \x22\x22, \x22explain_error_trim_traceback\x22: true, \x22explicit_ai_backend\x22: \x22\x22, \x22external_trusted_github_org_repos_quick_add\x22: \x22GoogleChrome\/CrUX,google\/generative-ai-docs,google-health\/cxr-foundation,google-health\/derm-foundation,google-health\/path-foundation\x22, \x22file_browser_poll_interval_millis\x22: 10000, \x22file_upload_rate_limit\x22: 5, \x22first_party_auth\x22: true, \x22fix_imports\x22: false, \x22fp_context\x22: false, \x22generate_code\x22: true, \x22generate_df\x22: true, \x22generate_prompt_reduce_blank_responses\x22: false, \x22generate_prompt_reduce_name_errors\x22: false, \x22get_started\x22: false, \x22gis_auth\x22: true, \x22github_client_id\x22: \x225036cf6d81e65aaa6340\x22, \x22gpu_utilization_check_interval_ms\x22: 600000, \x22hats_surveys\x22: true, \x22hrc\x22: false, \x22import_data\x22: false, \x22inline_completion_ai_campaign_max_views\x22: 3, \x22inline_completion_ai_campaign_throttle_ms\x22: 600000, \x22is_prober\x22: false, \x22jspb_analytics\x22: true, \x22jsraw\x22: \x22compiled\x22, \x22kaggle_backend_runtime_selector\x22: false, \x22kaggle_client_id\x22: \x22\x22, \x22kaggle_integrations\x22: false, \x22kaggle_resource_picker\x22: false, \x22kaggle_submit_to_competition\x22: false, \x22kernel_use_connected_endpoint_for_unassign\x22: true, \x22kernel_utils_fetch\x22: false, \x22key_promoter\x22: false, \x22kr\x22: false, \x22link_id_assignments\x22: true, \x22link_imports_to_installs\x22: true, \x22local_cloud_apis\x22: false, \x22local_service_worker\x22: false, \x22lsp_diagnostics_reporting\x22: false, \x22lsp_inlay_hint\x22: false, \x22makersuite_api_key\x22: \x22AIzaSyAmDcruecW4rCL1KdwcbIVHL4LkXxahIgw\x22, \x22makersuite_service_url\x22: \x22https:\/\/alkalimakersuite-pa.clients6.google.com\x22, \x22markdown_spellchecker\x22: false, \x22migrate_ccu_info\x22: false, \x22min_dep_cells_runtime_kernel_cl\x22: 694609395, \x22ml_enabled\x22: true, \x22mobile\x22: false, \x22moma_rag\x22: false, \x22moma_rag_composer\x22: false, \x22mpp_orc_temperature_override\x22: \x221.0\x22, \x22multi_modal_context_for_composer\x22: true, \x22multi_modal_context_for_transform\x22: false, \x22next_steps\x22: true, \x22nl2code_missing_imports\x22: false, \x22no_fun\x22: false, \x22oneplatform_api_key\x22: \x22AIzaSyA2BvntLwNwFthUB4w6_Bhn0cMlVHwyaHc\x22, \x22oneplatform_endpoint\x22: \x22https:\/\/colab.clients6.google.com\x22, \x22outage_notification\x22: \x22\x22, \x22outage_notification_link\x22: \x22\x22, \x22outputframe_version\x22: \x22\x22, \x22override_suf_params_for_test\x22: false, \x22parallel_prompting\x22: true, \x22pds_minting\x22: false, \x22prepare_runtime_for_notebook\x22: false, \x22prereq_cells_next_steps\x22: true, \x22presentation_mode\x22: true, \x22presentation_mode_start_from_beginning\x22: true, \x22prevent_ai_long_response_generate\x22: false, \x22prevent_ai_long_response_generate_with_df\x22: false, \x22prevent_ai_long_response_suggest_fix\x22: false, \x22prompt_for_dsa_trusted_tester_consent\x22: false, \x22recaptcha_polling_frequency_ms\x22: 300000, \x22recaptcha_v2_site_key\x22: \x226LfQttQUAAAAADuPanA_VZMaZgBAOnHZNuuqUewp\x22, \x22recaptcha_v3_site_key\x22: \x226LfQPtEUAAAAAHBpAdFng54jyuB1V5w5dofknpip\x22, \x22reconnect_max_delay_seconds\x22: 300, \x22reduced_gemini_sparks\x22: false, \x22refocus_focused_code_cell\x22: true, \x22remove_ai_explain_cell_fencing\x22: true, \x22remove_ai_explain_error_fencing\x22: true, \x22remove_ai_generate_fencing\x22: true, \x22require_ai_consent\x22: true, \x22resource_poll_interval_ms\x22: 10000, \x22rp_kxhr_skip_fallback\x22: false, \x22rp_serve_kernel_port\x22: true, \x22rp_socketio_fallback\x22: true, \x22rp_token_refresh_headroom_millis\x22: 300000, \x22rt_opt_in\x22: \x22OFF\x22, \x22run_mode\x22: false, \x22runtime_env_overrides\x22: \x22\\n          \x5b\\n            \x5b\\\x22ENABLE_DIRECTORYPREFETCHER\\\x22, \\\x221\\\x22\x5d\\n          \x5d\\n        \x22, \x22runtime_type_for_test\x22: \x22\x22, \x22runtime_version_names\x22: \x5b\x222025.07\x22\x5d, \x22runtime_version_selector\x22: false, \x22runtime_version_tags\x22: \x5b\x22release-colab_20250715-060042_RC00\x22\x5d, \x22server_execution_queue\x22: true, \x22server_side_generate_prompt_formatting_cloud\x22: false, \x22session_resume_coalesce\x22: true, \x22show_edu_signup_link\x22: true, \x22show_empty_notebook_actions\x22: true, \x22show_gemini_button_text_label\x22: true, \x22show_payments_interstitial\x22: false, \x22show_rel_notes_on_open\x22: true, \x22show_signup_survey\x22: true, \x22show_subscription_renewal_time\x22: false, \x22show_switch_to_prod_link\x22: false, \x22signup_ccu_increase\x22: true, \x22single_page_consent_form\x22: true, \x22smartpaste\x22: false, \x22smartpaste_chars_limit\x22: -1, \x22smartpaste_serving_config\x22: \x22freeform_servomatic_goose_v3_xs_smart_paste\x22, \x22sql_cell\x22: false, \x22sql_cell_buttons\x22: false, \x22sql_completion_lsp\x22: false, \x22storage_partition_trial\x22: true, \x22storage_partition_trial_token\x22: \x22Agk\/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe\/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9\x22, \x22suggest_plots\x22: true, \x22task_service_initial_poll_interval_ms\x22: 500, \x22task_service_max_poll_count\x22: 180, \x22task_service_max_poll_interval_ms\x22: 4000, \x22task_service_poll_interval_growth_factor\x22: 1.3, \x22task_service_poll_interval_ms\x22: 500, \x22task_service_poll_timeout_ms\x22: 90000, \x22task_service_wait_before_polling_ms\x22: 1000, \x22term4all\x22: true, \x22terminate_session_on_connect_to_new_vm\x22: true, \x22text_compose_report_changes_millis\x22: 10000, \x22text_span_comments\x22: false, \x22tpu_node_redirect\x22: true, \x22tpu_resource_stats\x22: false, \x22transform_code\x22: false, \x22transform_code_context_file_per_cell\x22: false, \x22trim_filename_extension\x22: false, \x22turn_off_agent_mode_when_safe\x22: true, \x22unmanaged_vm_min_label_block\x22: \x22\x22, \x22unmanaged_vm_min_label_warn\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_block\x22: \x22\x22, \x22unmanaged_vm_min_release_tag_warn\x22: \x22\x22, \x22unsupported_magics_check\x22: true, \x22use_ai_service\x22: false, \x22use_colab_adk_service\x22: false, \x22user_visible_accelerator_models\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22, \x22V28\x22, \x22V5E1\x22, \x22V6E1\x22\x5d, \x22user_visible_gpu_types\x22: \x5b\x22T4\x22, \x22A100\x22, \x22L4\x22\x5d, \x22v_100_redirect\x22: true, \x22verbose_warnings\x22: false, \x22vertex_ai_api_environment_override\x22: \x22\x22, \x22viz_cell\x22: false, \x22want_completions_ai_consent_campaign\x22: true, \x22workstations\x22: false, \x22ids\x22: \x5b20730265, 20730324, 20730460, 20730150, 20730454, 20730363, 20730369, 20730411, 20730470, 20730177, 20730182, 20730375\x5d, \x22flag_ids\x22: \x7b\x22add_df_vars_in_ai_conversation_context\x22: 45678289, \x22add_df_vars_in_ai_generate_context\x22: 45687604, \x22add_notebook_diffs_to_chat_history\x22: 45691117, \x22add_nvidia_cudf_facts_to_chat_context\x22: 45685179, \x22add_prompt_cell\x22: 45644995, \x22agent_client_update_task_max_request_size_bytes\x22: 45712580, \x22agent_scroll_delay_ms\x22: 45680776, \x22ai_banner\x22: 45670540, \x22ai_characters_per_token\x22: 45692654, \x22ai_prompt_token_limit\x22: 45692138, \x22ai_unsubscribed_warning\x22: 45504730, \x22ai_user_input_char_limit\x22: 45661098, \x22aida_complete_code_model_id\x22: 45427660, \x22aida_converse_max_facts\x22: 45680037, \x22aida_do_conversation_model_id\x22: 45427664, \x22aida_dsa_model_strategy\x22: 45693665, \x22aida_generate_code_model_id\x22: 45427663, \x22aida_generate_code_no_max_tokens\x22: 45694652, \x22allow_dsa_page_interaction\x22: 45675785, \x22allow_readonly_cells\x22: 45671718, \x22allow_subpaths_in_kernel_url\x22: 45699272, \x22allowed_public_url_domains\x22: 45425558, \x22backend_url_allowlist\x22: 45660303, \x22backend_version\x22: 45425541, \x22backtracking_strategy\x22: 45644832, \x22bigquery_sql_engine\x22: 45697421, \x22bigquery_sql_engine_library\x22: 45700104, \x22ccu_info_abort_timeout_ms\x22: 45691627, \x22cell_tags\x22: 45425779, \x22cell_ui_refresh\x22: 45673630, \x22chat_explain_error_temp\x22: 45655973, \x22chat_model_id_override\x22: 45631876, \x22classified_generate\x22: 45425499, \x22classroom_iframe_parent_origin\x22: 45425537, \x22client_trim_completion_text\x22: 45425628, \x22clone_notebook_link\x22: 45716348, \x22cloud_origin\x22: 45425538, \x22cloud_run\x22: 45697172, \x22code_report_millis\x22: 45658073, \x22colab_fetch_try_reauth\x22: 45713304, \x22comment_poll_long\x22: 45425588, \x22comment_poll_short\x22: 45425587, \x22complete_code\x22: 45686676, \x22compose_skip_suffix_check\x22: 45615470, \x22composer\x22: 45683351, \x22composer_auto_code\x22: 45693768, \x22composer_autocomplete\x22: 45718105, \x22composer_bigquery_context\x22: 45710683, \x22composer_context_max_variable_length\x22: 45688573, \x22composer_early_stopping_for_image_truncation\x22: 45719141, \x22composer_focused_cell_context\x22: 45697545, \x22composer_fp_context\x22: 45701859, \x22composer_generate_code\x22: 45702500, \x22composer_kernel_files_in_context\x22: 45701855, \x22composer_model_strategy\x22: 45711731, \x22composer_show_debug_info\x22: 45700003, \x22composer_survey\x22: 45707270, \x22composer_transform_code\x22: 45700458, \x22composer_visible_cells_context\x22: 45716167, \x22converse_notebook_context_length\x22: 45705427, \x22copy_cell_output\x22: 45712093, \x22corp_third_party_widgets\x22: 45678906, \x22crawler\x22: 45425491, \x22create_gemini_api_key\x22: 45654552, \x22critique_comments\x22: 45612076, \x22data_inspector\x22: 45697206, \x22dbu\x22: 45425545, \x22debug_adapter\x22: 45690097, \x22debug_external\x22: 45425470, \x22debug_prod\x22: 45425471, \x22debugger_server_side_globals\x22: 45687360, \x22dep_cells_commands\x22: 45622249, \x22dep_cells_enabled\x22: 45653551, \x22dep_graph\x22: 45629071, \x22deprecate_prompt\x22: 45679897, \x22deprecate_unpin\x22: 45701465, \x22development\x22: 45425544, \x22dialog_ui_refresh\x22: 45698577, \x22document_change_poll_interval\x22: 45425589, \x22drive_anon_api_key\x22: 45425478, \x22drive_api_key\x22: 45425473, \x22drive_background_save_project_number\x22: 45425479, \x22drive_realtime_project_number\x22: 45425629, \x22drop_chat_links\x22: 45646864, \x22dsa\x22: 45656258, \x22dsa_file_not_sent_survey_timeout\x22: 45688578, \x22dsa_markdown_cells\x22: 45707419, \x22dsa_sample_datasets_toast\x22: 45682045, \x22embedded_toolbar_customization\x22: 45692827, \x22embedded_use_websockets\x22: 45691694, \x22enable_adhoc_backends\x22: 45425506, \x22enable_agent_connect_to_new_vm\x22: 45670252, \x22enable_cell_pair_slides\x22: 45719587, \x22enable_composer_changeset_stacking\x22: 45717253, \x22enable_composer_code_report\x22: 45708595, \x22enable_composer_suggestion_chips\x22: 45710464, \x22enable_dasher_subscription_ui\x22: 45639531, \x22enable_edu_subscription_ui\x22: 45693272, \x22enable_more_reprs\x22: 45613354, \x22enable_mpp_orc_model_overrides\x22: 45649913, \x22enable_rt_on_create\x22: 45667583, \x22execution_status_propagation\x22: 45644828, \x22explain_error_model_id_override\x22: 45631875, \x22explain_error_trim_traceback\x22: 45618831, \x22explicit_ai_backend\x22: 45638548, \x22external_trusted_github_org_repos_quick_add\x22: 45425555, \x22file_browser_poll_interval_millis\x22: 45643722, \x22file_upload_rate_limit\x22: 45637799, \x22first_party_auth\x22: 45425560, \x22fix_imports\x22: 45624140, \x22fp_context\x22: 45684902, \x22generate_code\x22: 45425492, \x22generate_df\x22: 45425503, \x22generate_prompt_reduce_blank_responses\x22: 45643396, \x22generate_prompt_reduce_name_errors\x22: 45634392, \x22get_started\x22: 45430267, \x22gis_auth\x22: 45425625, \x22github_client_id\x22: 45425556, \x22gpu_utilization_check_interval_ms\x22: 45425561, \x22hats_surveys\x22: 45425559, \x22import_data\x22: 45430411, \x22inline_completion_ai_campaign_max_views\x22: 45676328, \x22inline_completion_ai_campaign_throttle_ms\x22: 45671534, \x22is_prober\x22: 45429104, \x22jspb_analytics\x22: 45704358, \x22jsraw\x22: 45425557, \x22kaggle_backend_runtime_selector\x22: 45704319, \x22kaggle_client_id\x22: 45690272, \x22kaggle_integrations\x22: 45690259, \x22kaggle_resource_picker\x22: 45697311, \x22kaggle_submit_to_competition\x22: 45693906, \x22kernel_use_connected_endpoint_for_unassign\x22: 45684913, \x22kernel_utils_fetch\x22: 45708200, \x22key_promoter\x22: 45425570, \x22link_id_assignments\x22: 45644831, \x22link_imports_to_installs\x22: 45644830, \x22local_cloud_apis\x22: 45425630, \x22local_service_worker\x22: 45425550, \x22lsp_diagnostics_reporting\x22: 45425604, \x22lsp_inlay_hint\x22: 45614695, \x22makersuite_api_key\x22: 45655361, \x22makersuite_service_url\x22: 45655362, \x22markdown_spellchecker\x22: 45671479, \x22migrate_ccu_info\x22: 45716751, \x22min_dep_cells_runtime_kernel_cl\x22: 45654240, \x22ml_enabled\x22: 45425493, \x22mobile\x22: 45425562, \x22moma_rag\x22: 45686203, \x22moma_rag_composer\x22: 45706746, \x22mpp_orc_temperature_override\x22: 45649914, \x22multi_modal_context_for_composer\x22: 45691122, \x22multi_modal_context_for_transform\x22: 45687634, \x22next_steps\x22: 45428239, \x22nl2code_missing_imports\x22: 45615676, \x22no_fun\x22: 45425540, \x22oneplatform_api_key\x22: 45717742, \x22oneplatform_endpoint\x22: 45717924, \x22outage_notification\x22: 45425584, \x22outage_notification_link\x22: 45425585, \x22outputframe_version\x22: 45425591, \x22override_suf_params_for_test\x22: 45425592, \x22parallel_prompting\x22: 45666384, \x22pds_minting\x22: 45648255, \x22prepare_runtime_for_notebook\x22: 45699118, \x22prereq_cells_next_steps\x22: 45640400, \x22presentation_mode\x22: 45699417, \x22presentation_mode_start_from_beginning\x22: 45714276, \x22prevent_ai_long_response_generate\x22: 45680972, \x22prevent_ai_long_response_generate_with_df\x22: 45681123, \x22prevent_ai_long_response_suggest_fix\x22: 45681124, \x22prompt_for_dsa_trusted_tester_consent\x22: 45670923, \x22recaptcha_polling_frequency_ms\x22: 45425582, \x22recaptcha_v2_site_key\x22: 45425581, \x22recaptcha_v3_site_key\x22: 45425580, \x22reconnect_max_delay_seconds\x22: 45425539, \x22reduced_gemini_sparks\x22: 45719726, \x22refocus_focused_code_cell\x22: 45714009, \x22remove_ai_explain_cell_fencing\x22: 45677303, \x22remove_ai_explain_error_fencing\x22: 45677302, \x22remove_ai_generate_fencing\x22: 45673079, \x22require_ai_consent\x22: 45425489, \x22resource_poll_interval_ms\x22: 45425590, \x22rp_kxhr_skip_fallback\x22: 45656329, \x22rp_serve_kernel_port\x22: 45572083, \x22rp_socketio_fallback\x22: 45658495, \x22rp_token_refresh_headroom_millis\x22: 45517773, \x22rt_opt_in\x22: 45667546, \x22run_mode\x22: 45642857, \x22runtime_env_overrides\x22: 45425583, \x22runtime_type_for_test\x22: 45425586, \x22runtime_version_names\x22: 45714997, \x22runtime_version_selector\x22: 45713197, \x22runtime_version_tags\x22: 45714998, \x22server_execution_queue\x22: 45425600, \x22server_side_generate_prompt_formatting_cloud\x22: 45655196, \x22session_resume_coalesce\x22: 45425603, \x22show_edu_signup_link\x22: 45692615, \x22show_empty_notebook_actions\x22: 45677304, \x22show_gemini_button_text_label\x22: 45681647, \x22show_payments_interstitial\x22: 45425543, \x22show_rel_notes_on_open\x22: 45644210, \x22show_signup_survey\x22: 45425620, \x22show_subscription_renewal_time\x22: 45425569, \x22show_switch_to_prod_link\x22: 45425483, \x22signup_ccu_increase\x22: 45689970, \x22single_page_consent_form\x22: 45656775, \x22smartpaste\x22: 45627425, \x22smartpaste_chars_limit\x22: 45714219, \x22smartpaste_serving_config\x22: 45630585, \x22sql_cell\x22: 45425497, \x22sql_cell_buttons\x22: 45425498, \x22sql_completion_lsp\x22: 45688254, \x22suggest_plots\x22: 45696393, \x22task_service_initial_poll_interval_ms\x22: 45696534, \x22task_service_max_poll_count\x22: 45669592, \x22task_service_max_poll_interval_ms\x22: 45696536, \x22task_service_poll_interval_growth_factor\x22: 45696535, \x22task_service_poll_interval_ms\x22: 45669591, \x22task_service_poll_timeout_ms\x22: 45696537, \x22task_service_wait_before_polling_ms\x22: 45669590, \x22term4all\x22: 45425542, \x22terminate_session_on_connect_to_new_vm\x22: 45683597, \x22text_compose_report_changes_millis\x22: 45425568, \x22text_span_comments\x22: 45545873, \x22tpu_node_redirect\x22: 45634372, \x22tpu_resource_stats\x22: 45655215, \x22transform_code\x22: 45667102, \x22transform_code_context_file_per_cell\x22: 45671260, \x22trim_filename_extension\x22: 45691676, \x22turn_off_agent_mode_when_safe\x22: 45679577, \x22unmanaged_vm_min_label_block\x22: 45425546, \x22unmanaged_vm_min_label_warn\x22: 45425547, \x22unmanaged_vm_min_release_tag_block\x22: 45425548, \x22unmanaged_vm_min_release_tag_warn\x22: 45425549, \x22unsupported_magics_check\x22: 45644829, \x22use_ai_service\x22: 45713338, \x22use_colab_adk_service\x22: 20730464, \x22user_visible_accelerator_models\x22: 45682571, \x22user_visible_gpu_types\x22: 45620529, \x22v_100_redirect\x22: 45644963, \x22verbose_warnings\x22: 45425551, \x22vertex_ai_api_environment_override\x22: 45612077, \x22viz_cell\x22: 45690754, \x22want_completions_ai_consent_campaign\x22: 45671138, \x22workstations\x22: 45425626\x7d\x7d'); var colabUserEmail = 'orioyeesther2019@gmail.com'; var colabRenderDataToken = 'AFWLbD11ouVsNmJcNHpMyQZw1lVl1SL881S4jzJTiNGFTuryhGXXFRZVdAeudqZFRsEZlpiBSd8kM8mBgfRmKxJT2atxMzcs8VDy3wNY'; var colabConfig = '\x5b\x5b\x22orioyeesther2019@gmail.com\x22,\x5b1,\x22AHXL0D34nqRq\/46cd9LIVTwavSgiheZw2zkfbAAESfldFLDUAd4JHNWzANNSqy0lmRwX4NHgalgLFgaM9cV4TQg1o4tfGrXBe0hGIjStgW\/pTXi1WR\/e+1V9Q2bt4xs1Wh4tqeEfq5UuMkFNyJ5w8jLjemebrHkfdLHH8\/A5z2DyZJjlyR1U4oGTqRXcP376+GGkLWTtICcYaGDDgMryy0uMeZI5SXwsKUDaDC\/VKw+mxGRzE2qJdXUAras2TK8T7G2QtEWtNfazzWJdrYVOPMlwslxTe3ZjYuHDN89AZpb2sDqnVm4qBW\/Z+hImWP10ioGLcggS4mcPrkT4Z8EEO4qkYec2QpESpGB7gBOsorZCAUUSDrda7HOXnwmtmIc+GmRkIBqG\/ni2rHU8x3gLYh1yNt3QFc6WukWqHKLM1bSrJb4oncL5CXv7ZawzQWs4YJ8JUa96k8osvL7pGLUr5KJjHAibxqiWFtaTi1hD6Fm5A4WSM36hA+J3gX4U3bZ7TT+kQhVIAfYLtG\/I1N3Dwweg4GEA2+80xLMNYa+0vrA6wKdkxeys0hNwyl4dCtIzol3DSAbevPYG2losjsnxiTtMBKHG9uf83KmEtLzAxZ0XWK8tpWXF01dMHGA4NL\/IeUx8EQd\/jPDMT4N5975pMDT0uioFG844VikrP\/L+JoeGTllzble6IKgs5Z2PGxDAbCJdXa7jFu1uK2D\/b5qZcqKA088iGWyncI5flEJ2AfKb43FxInwqjA5F2aYhwvxFd88qnw3oqvIHxwVIqb8y2TXCQ7FZTPSqXbzenTkD2sAaZlPADGXNP6nuwK4CQdiubN6wIpfsyJLqItUnzREuSsyf9f95STsC+p8kJ6MpTqZWaRS0bzwxbDOpsMOuFBW0jkgRXRjGthD7wgHNODNOuUkvd1HaNWvqt+cmYMkMm+Ur0CrInhpvnr0PHhU6VrYpHhkOIfKznf+JdLdXlPH1gd2o33OU2DtlHA+E3WioEfX7pzNXy76tqH8712zElSXLlLgFYD4trP180tKN3NmlllIgrBiFSklptiJe4C3d3fbSgSX+73mtCb7t1TxxANGtdcFjAcnsbYg0VG\/Vroq70jmNR7joqKqosxrGQXt6UgVqLvo\/YuCkW+e6MQc+sdwL+EEwaqOpoPbLG3dSGZedROMD+voJOgVkCBe1nWGA+1t5LV6KDvqmLVlKsM6Ooo07+Po3XH7hRjFoes1ZfKGUaJAYnslbPP3q+O8i0OzzY+dqx\/mt6bFuLE+nzuNqEFRT8xkTyY3+NPo3NuRrYhOVI6owZclHxGfqINEIEwbjpjdDpLnmCX\/FqSXEQFLqUl2PnNqU1\/\/AG7hotOif2u3TdihAC9jxF2RTJhd0tx\/KYkDz9uj2stG66q5O\/DDnsorNiLbbja4ohkKCTbm5dPP0FGBDuPzMUXqPd3v2FOQ9UBfp6NU3T8gfWN8K4MVRR+rbZsU9gk68qUgWdVEpUC5p9Jpbz+EFs1YYy91nFQhxGzO6Vfp72M3y2gwHKRRz\/OQXIq3ktplGY6ouImcN6mH7FflzG5DUhUIn9QzNx\/us2vZY6Q9+IbhJgv0JNWQStHQ27kk6wZs5UXnYDX7Hwwj4hlQh31plhcaOmN48X0WY4XJYp4FlezncTtF\/IHsvvu7e2hil0A4APNzTQwMDy0P4Y3hZrYvHYJFoD+IX1w6JurRlydnR02HBPRz6iqMrRFLe6kGRld3o+sRXsE+YG63iZb2p+FkRE+bohxUxCZqjkEm\/SGO4idn5dkOw\/TjPXTnHFuFqWJwAcGF2+wTcEVogNs3KU8ep5bMY0RBSCxmx6dNuBLGipW4ToWOPNWmhESlAwfj+58aDlo+tXJFVXtUkF8H7fw3cMS4ncprZGyeXEWdSqZgoBqnIYo8\x3d\x22,\x22AJ9oCCwrNLZW\/IPRsZqXu7HpMXe9TfiqgBI\/CQxXazOkTGSmmrHWsCeGwF6SMgZs0ICm3IrBHtzmob\/NHRY8lKNKRsMsHyycqPlmU9vars5EE1EPwUrQ5S+Mp2UuGlJy3O+2eVHewr4Q\x22,\x22https:\/\/payments.google.com\/payments\x22,0,0,null,null,null,\x22US$9.99\x22,\x22US$49.99\x22,\x22US$9.99\x22,\x22US$49.99\x22,0,0,0\x5d,\x5b1,4,5\x5d,\x22NG\x22,0\x5d\x5d';</script><link id="favicon-link" rel="shortcut icon" href="https://ssl.gstatic.com/colaboratory-static/common/5974b39383863f189d8033cb6eeaf562/img/favicon.ico"><meta name="google-site-verification" content="wRgpUU3mIRZPD1GORBPNonaotM72092B_DsqQFWNa4s"><meta name="google-site-verification" content="dsf7CRwnDkQv6Ot4gXTXx8_nVf8A9cb5o30hZ7cGAIo"><meta name="google-site-verification" content="K1UdZBHJXQYnJGXIK1KuutmVy6dn3vG2sEyV9D1C6dM"><meta name="google-site-verification" content="wdGthzzfu0IjM3qpFqTuQL9poAQZAvAaFKyuzetLpIM"><meta name="google-site-verification" content="qZJ77guHGO0TObHUBRYVdXQlIhXBBuz8dahJVmIlzCo"><meta name="google-site-verification" content="7ahoeOOKT2ZR781GZ5xK4L9t7yO1ZOHc-gaoUALEYgw"><meta name="google-site-verification" content="PHgaSKwdxZELS21aixtLhfpvaHtKen9pnVJ25EI35Zs"><meta name="google-site-verification" content="qylwTsZSLomIg1JrChne7cPcXmtC2Xh_5ZxlJWLlAH0"><meta name="google-site-verification" content="BQfukMqFy1nu2Q2gjGbNTDA8MJ_Y4L2brCYA1h6ewkY"><meta name="google-site-verification" content="pIZq7V_Vt54MAfdQe5afm8zeJrl3o4GkRW-etNvnlKI"><meta name="google-site-verification" content="Ozey1ptWUQW13_lCEhpPMOcmRBLqdyB3WEL-TJUjskU"><meta name="google-site-verification" content="z-WR3zzv8XZ5FFfBLLDbyTiN35UXm01nWUS2Uej5pwg"><meta name="google-site-verification" content="rF5iXzWe9KZXJes1dQNhOUkS4_z_e97IrsVoCx2trek"><meta name="google-site-verification" content="vsXaeD7OD0m3iK8Z54fG8TYGC5eT17KeL_xMHtdiyWI"><meta name="google-site-verification" content="cpB5oulaGwqSxsg4E-9q2MVbK87iE9NAUUVxdveucPw"><meta name="google-site-verification" content="b6bOMRzMVX2bJABYDGBPtpGcB_AUZ-o2SOTggQXErkg"><meta name="google-site-verification" content="88fgsZDoVRBuRnDPMIEjcHCxsEXzODOqEsJoqtvQsDc"><meta name="google-site-verification" content="hZkpVtQ8gdGznkTfUekRWeGY05QyeLXb6q946CFw2-c"><meta name="google-site-verification" content="sMarhZgb4va_L_7UTdMR43gDZ2gVqc_5GHN4REpQPGY"><meta name="google-site-verification" content="26aKGBCw3XblB5Ou01UhxY5WDtMqHjoTm6P-lvF6AqE"><meta name="google-site-verification" content="DGionF7db9g0dOgeBXwOAN2tmCzWBdo5yOdc_-5UcuE"><meta name="google-site-verification" content="Q9LlidR0toR7UtSyVO23xNeaqJmRp8I6r4ghBQTtntU"><meta name="google-site-verification" content="rQawcZaTEK_UrDG30cz_7nVKOVvBass61QEes0Tm04g"><meta name="google-site-verification" content="-N1hdkiHJQ6kwJALkHVh2ZzV2fFNER0schZl2AU6zvc"><meta name="google-site-verification" content="8L3ghjzKIj241AYAmEygniTe604tsXFkIrb1v-DBtGo"><meta name="google-site-verification" content="Gz6pcDgVFH_aS-aPTYW21rSHcWl0LAgKCWJtdXPVTNo"><meta name="google-site-verification" content="KiunYPvrY5x8umvAWcjhwPrB677xCar2LeT_8yaVrDg"><meta name="google-site-verification" content="LypEVvHhYiLSzDs9PabhmOmsfMfEjVGq2rLXJbtqdzY"><meta property="og:type" content="article"><meta property="og:image" content="https://colab.research.google.com/img/colab_favicon_256px.png"><meta property="og:title" content="Google Colab"><meta http-equiv="origin-trial" content="Agk/t4Bt05W7j6CHeqXH9+6ccDayrBsQPqCLDPSElphe/7cUobayuvN0A3huajTbJenIjp6qibLteh6e0IEWrgIAAAB4eyJvcmlnaW4iOiJodHRwczovL2NvbGFiLnJlc2VhcmNoLmdvb2dsZS5jb206NDQzIiwiZmVhdHVyZSI6IkRpc2FibGVUaGlyZFBhcnR5U3RvcmFnZVBhcnRpdGlvbmluZzIiLCJleHBpcnkiOjE3NDIzNDIzOTl9"><script nonce="">window.performance.mark('head_end'); window.performance.measure('head', 'head_start', 'head_end');</script><script async="" src="./Orioye.E.project8.ipy_files/lazy.min.js.download" nonce=""></script><style id="inert-style">
[inert] {
  pointer-events: none;
  cursor: default;
}

[inert], [inert] * {
  user-select: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
}
</style><script async="async" type="text/javascript" src="./Orioye.E.project8.ipy_files/editor.main.js.download"></script><script async="" type="text/javascript" charset="UTF-8" src="./Orioye.E.project8.ipy_files/rs=AA2YrTthfa-GW6nWNiVo32au3OStcP0_zg" nonce=""></script><link type="text/css" href="./Orioye.E.project8.ipy_files/rs=AA2YrTs5z5IeveM3_8fj3UK_0H1gj7fqJg" rel="stylesheet"><link rel="stylesheet" type="text/css" data-name="vs/editor/editor.main" href="./Orioye.E.project8.ipy_files/editor.main.css"><script async="async" type="text/javascript" src="./Orioye.E.project8.ipy_files/editor.main.nls.js.download"></script><style type="text/css">.MathJax_Hover_Frame {border-radius: .25em; -webkit-border-radius: .25em; -moz-border-radius: .25em; -khtml-border-radius: .25em; box-shadow: 0px 0px 15px #83A; -webkit-box-shadow: 0px 0px 15px #83A; -moz-box-shadow: 0px 0px 15px #83A; -khtml-box-shadow: 0px 0px 15px #83A; border: 1px solid #A6D ! important; display: inline-block; position: absolute}
.MathJax_Menu_Button .MathJax_Hover_Arrow {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 4px; -webkit-border-radius: 4px; -moz-border-radius: 4px; -khtml-border-radius: 4px; font-family: 'Courier New',Courier; font-size: 9px; color: #F0F0F0}
.MathJax_Menu_Button .MathJax_Hover_Arrow span {display: block; background-color: #AAA; border: 1px solid; border-radius: 3px; line-height: 0; padding: 4px}
.MathJax_Hover_Arrow:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_Hover_Arrow:hover span {background-color: #CCC!important}
</style><style type="text/css">#MathJax_About {position: fixed; left: 50%; width: auto; text-align: center; border: 3px outset; padding: 1em 2em; background-color: #DDDDDD; color: black; cursor: default; font-family: message-box; font-size: 120%; font-style: normal; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; border-radius: 15px; -webkit-border-radius: 15px; -moz-border-radius: 15px; -khtml-border-radius: 15px; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_About.MathJax_MousePost {outline: none}
.MathJax_Menu {position: absolute; background-color: white; color: black; width: auto; padding: 2px; border: 1px solid #CCCCCC; margin: 0; cursor: default; font: menu; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; z-index: 201; box-shadow: 0px 10px 20px #808080; -webkit-box-shadow: 0px 10px 20px #808080; -moz-box-shadow: 0px 10px 20px #808080; -khtml-box-shadow: 0px 10px 20px #808080; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
.MathJax_MenuItem {padding: 2px 2em; background: transparent}
.MathJax_MenuArrow {position: absolute; right: .5em; padding-top: .25em; color: #666666; font-size: .75em}
.MathJax_MenuActive .MathJax_MenuArrow {color: white}
.MathJax_MenuArrow.RTL {left: .5em; right: auto}
.MathJax_MenuCheck {position: absolute; left: .7em}
.MathJax_MenuCheck.RTL {right: .7em; left: auto}
.MathJax_MenuRadioCheck {position: absolute; left: 1em}
.MathJax_MenuRadioCheck.RTL {right: 1em; left: auto}
.MathJax_MenuLabel {padding: 2px 2em 4px 1.33em; font-style: italic}
.MathJax_MenuRule {border-top: 1px solid #CCCCCC; margin: 4px 1px 0px}
.MathJax_MenuDisabled {color: GrayText}
.MathJax_MenuActive {background-color: Highlight; color: HighlightText}
.MathJax_MenuDisabled:focus, .MathJax_MenuLabel:focus {background-color: #E8E8E8}
.MathJax_ContextMenu:focus {outline: none}
.MathJax_ContextMenu .MathJax_MenuItem:focus {outline: none}
#MathJax_AboutClose {top: .2em; right: .2em}
.MathJax_Menu .MathJax_MenuClose {top: -10px; left: -10px}
.MathJax_MenuClose {position: absolute; cursor: pointer; display: inline-block; border: 2px solid #AAA; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; font-family: 'Courier New',Courier; font-size: 24px; color: #F0F0F0}
.MathJax_MenuClose span {display: block; background-color: #AAA; border: 1.5px solid; border-radius: 18px; -webkit-border-radius: 18px; -moz-border-radius: 18px; -khtml-border-radius: 18px; line-height: 0; padding: 8px 0 6px}
.MathJax_MenuClose:hover {color: white!important; border: 2px solid #CCC!important}
.MathJax_MenuClose:hover span {background-color: #CCC!important}
.MathJax_MenuClose:hover:focus {outline: none}
</style><style type="text/css">.MJX_Assistive_MathML {position: absolute!important; top: 0; left: 0; clip: rect(1px, 1px, 1px, 1px); padding: 1px 0 0 0!important; border: 0!important; height: 1px!important; width: 1px!important; overflow: hidden!important; display: block!important; -webkit-touch-callout: none; -webkit-user-select: none; -khtml-user-select: none; -moz-user-select: none; -ms-user-select: none; user-select: none}
.MJX_Assistive_MathML.MJX_Assistive_MathML_Block {width: 100%!important}
</style><style type="text/css">#MathJax_Zoom {position: absolute; background-color: #F0F0F0; overflow: auto; display: block; z-index: 301; padding: .5em; border: 1px solid black; margin: 0; font-weight: normal; font-style: normal; text-align: left; text-indent: 0; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; -webkit-box-sizing: content-box; -moz-box-sizing: content-box; box-sizing: content-box; box-shadow: 5px 5px 15px #AAAAAA; -webkit-box-shadow: 5px 5px 15px #AAAAAA; -moz-box-shadow: 5px 5px 15px #AAAAAA; -khtml-box-shadow: 5px 5px 15px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true')}
#MathJax_ZoomOverlay {position: absolute; left: 0; top: 0; z-index: 300; display: inline-block; width: 100%; height: 100%; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
#MathJax_ZoomFrame {position: relative; display: inline-block; height: 0; width: 0}
#MathJax_ZoomEventTrap {position: absolute; left: 0; top: 0; z-index: 302; display: inline-block; border: 0; padding: 0; margin: 0; background-color: white; opacity: 0; filter: alpha(opacity=0)}
</style><style type="text/css">.MathJax_Preview {color: #888}
#MathJax_Message {position: fixed; left: 1em; bottom: 1.5em; background-color: #E6E6E6; border: 1px solid #959595; margin: 0px; padding: 2px 8px; z-index: 102; color: black; font-size: 80%; width: auto; white-space: nowrap}
#MathJax_MSIE_Frame {position: absolute; top: 0; left: 0; width: 0px; z-index: 101; border: 0px; margin: 0px; padding: 0px}
.MathJax_Error {color: #CC0000; font-style: italic}
</style><style type="text/css">.MJXp-script {font-size: .8em}
.MJXp-right {-webkit-transform-origin: right; -moz-transform-origin: right; -ms-transform-origin: right; -o-transform-origin: right; transform-origin: right}
.MJXp-bold {font-weight: bold}
.MJXp-italic {font-style: italic}
.MJXp-scr {font-family: MathJax_Script,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-frak {font-family: MathJax_Fraktur,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-sf {font-family: MathJax_SansSerif,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-cal {font-family: MathJax_Caligraphic,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-mono {font-family: MathJax_Typewriter,'Times New Roman',Times,STIXGeneral,serif}
.MJXp-largeop {font-size: 150%}
.MJXp-largeop.MJXp-int {vertical-align: -.2em}
.MJXp-math {display: inline-block; line-height: 1.2; text-indent: 0; font-family: 'Times New Roman',Times,STIXGeneral,serif; white-space: nowrap; border-collapse: collapse}
.MJXp-display {display: block; text-align: center; margin: 1em 0}
.MJXp-math span {display: inline-block}
.MJXp-box {display: block!important; text-align: center}
.MJXp-box:after {content: " "}
.MJXp-rule {display: block!important; margin-top: .1em}
.MJXp-char {display: block!important}
.MJXp-mo {margin: 0 .15em}
.MJXp-mfrac {margin: 0 .125em; vertical-align: .25em}
.MJXp-denom {display: inline-table!important; width: 100%}
.MJXp-denom > * {display: table-row!important}
.MJXp-surd {vertical-align: top}
.MJXp-surd > * {display: block!important}
.MJXp-script-box > *  {display: table!important; height: 50%}
.MJXp-script-box > * > * {display: table-cell!important; vertical-align: top}
.MJXp-script-box > *:last-child > * {vertical-align: bottom}
.MJXp-script-box > * > * > * {display: block!important}
.MJXp-mphantom {visibility: hidden}
.MJXp-munderover, .MJXp-munder {display: inline-table!important}
.MJXp-over {display: inline-block!important; text-align: center}
.MJXp-over > * {display: block!important}
.MJXp-munderover > *, .MJXp-munder > * {display: table-row!important}
.MJXp-mtable {vertical-align: .25em; margin: 0 .125em}
.MJXp-mtable > * {display: inline-table!important; vertical-align: middle}
.MJXp-mtr {display: table-row!important}
.MJXp-mtd {display: table-cell!important; text-align: center; padding: .5em 0 0 .5em}
.MJXp-mtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-mlabeledtr {display: table-row!important}
.MJXp-mlabeledtr > .MJXp-mtd:first-child {padding-left: 0}
.MJXp-mlabeledtr:first-child > .MJXp-mtd {padding-top: 0}
.MJXp-merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MJXp-scale0 {-webkit-transform: scaleX(.0); -moz-transform: scaleX(.0); -ms-transform: scaleX(.0); -o-transform: scaleX(.0); transform: scaleX(.0)}
.MJXp-scale1 {-webkit-transform: scaleX(.1); -moz-transform: scaleX(.1); -ms-transform: scaleX(.1); -o-transform: scaleX(.1); transform: scaleX(.1)}
.MJXp-scale2 {-webkit-transform: scaleX(.2); -moz-transform: scaleX(.2); -ms-transform: scaleX(.2); -o-transform: scaleX(.2); transform: scaleX(.2)}
.MJXp-scale3 {-webkit-transform: scaleX(.3); -moz-transform: scaleX(.3); -ms-transform: scaleX(.3); -o-transform: scaleX(.3); transform: scaleX(.3)}
.MJXp-scale4 {-webkit-transform: scaleX(.4); -moz-transform: scaleX(.4); -ms-transform: scaleX(.4); -o-transform: scaleX(.4); transform: scaleX(.4)}
.MJXp-scale5 {-webkit-transform: scaleX(.5); -moz-transform: scaleX(.5); -ms-transform: scaleX(.5); -o-transform: scaleX(.5); transform: scaleX(.5)}
.MJXp-scale6 {-webkit-transform: scaleX(.6); -moz-transform: scaleX(.6); -ms-transform: scaleX(.6); -o-transform: scaleX(.6); transform: scaleX(.6)}
.MJXp-scale7 {-webkit-transform: scaleX(.7); -moz-transform: scaleX(.7); -ms-transform: scaleX(.7); -o-transform: scaleX(.7); transform: scaleX(.7)}
.MJXp-scale8 {-webkit-transform: scaleX(.8); -moz-transform: scaleX(.8); -ms-transform: scaleX(.8); -o-transform: scaleX(.8); transform: scaleX(.8)}
.MJXp-scale9 {-webkit-transform: scaleX(.9); -moz-transform: scaleX(.9); -ms-transform: scaleX(.9); -o-transform: scaleX(.9); transform: scaleX(.9)}
.MathJax_PHTML .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><style type="text/css">.MathJax_Display {text-align: center; margin: 0; position: relative; display: block!important; text-indent: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; width: 100%}
.MathJax .merror {background-color: #FFFF88; color: #CC0000; border: 1px solid #CC0000; padding: 1px 3px; font-style: normal; font-size: 90%}
.MathJax .MJX-monospace {font-family: monospace}
.MathJax .MJX-sans-serif {font-family: sans-serif}
#MathJax_Tooltip {background-color: InfoBackground; color: InfoText; border: 1px solid black; box-shadow: 2px 2px 5px #AAAAAA; -webkit-box-shadow: 2px 2px 5px #AAAAAA; -moz-box-shadow: 2px 2px 5px #AAAAAA; -khtml-box-shadow: 2px 2px 5px #AAAAAA; filter: progid:DXImageTransform.Microsoft.dropshadow(OffX=2, OffY=2, Color='gray', Positive='true'); padding: 3px 4px; z-index: 401; position: absolute; left: 0; top: 0; width: auto; height: auto; display: none}
.MathJax {display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; word-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0; min-height: 0; border: 0; padding: 0; margin: 0}
.MathJax:focus, body :focus .MathJax {display: inline-table}
.MathJax.MathJax_FullWidth {text-align: center; display: table-cell!important; width: 10000em!important}
.MathJax img, .MathJax nobr, .MathJax a {border: 0; padding: 0; margin: 0; max-width: none; max-height: none; min-width: 0; min-height: 0; vertical-align: 0; line-height: normal; text-decoration: none}
img.MathJax_strut {border: 0!important; padding: 0!important; margin: 0!important; vertical-align: 0!important}
.MathJax span {display: inline; position: static; border: 0; padding: 0; margin: 0; vertical-align: 0; line-height: normal; text-decoration: none; box-sizing: content-box}
.MathJax nobr {white-space: nowrap!important}
.MathJax img {display: inline!important; float: none!important}
.MathJax * {transition: none; -webkit-transition: none; -moz-transition: none; -ms-transition: none; -o-transition: none}
.MathJax_Processing {visibility: hidden; position: fixed; width: 0; height: 0; overflow: hidden}
.MathJax_Processed {display: none!important}
.MathJax_test {font-style: normal; font-weight: normal; font-size: 100%; font-size-adjust: none; text-indent: 0; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow: hidden; height: 1px}
.MathJax_test.mjx-test-display {display: table!important}
.MathJax_test.mjx-test-inline {display: inline!important; margin-right: -1px}
.MathJax_test.mjx-test-default {display: block!important; clear: both}
.MathJax_ex_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60ex}
.MathJax_em_box {display: inline-block!important; position: absolute; overflow: hidden; min-height: 0; max-height: none; padding: 0; border: 0; margin: 0; width: 1px; height: 60em}
.mjx-test-inline .MathJax_left_box {display: inline-block; width: 0; float: left}
.mjx-test-inline .MathJax_right_box {display: inline-block; width: 0; float: right}
.mjx-test-display .MathJax_right_box {display: table-cell!important; width: 10000em!important; min-width: 0; max-width: none; padding: 0; border: 0; margin: 0}
.MathJax .MathJax_HitBox {cursor: text; background: white; opacity: 0; filter: alpha(opacity=0)}
.MathJax .MathJax_HitBox * {filter: none; opacity: 1; background: transparent}
#MathJax_Tooltip * {filter: none; opacity: 1; background: transparent}
@font-face {font-family: MathJax_Main; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-bold; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Bold.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Bold.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Main-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Main-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Main-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Math-italic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Math-Italic.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Math-Italic.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Caligraphic; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Caligraphic-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Caligraphic-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size1; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size1-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size1-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size2; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size2-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size2-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size3; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size3-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size3-Regular.otf?V=2.7.5') format('opentype')}
@font-face {font-family: MathJax_Size4; src: url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/woff/MathJax_Size4-Regular.woff?V=2.7.5') format('woff'), url('https://colab.research.google.com/static/mathjax/fonts/HTML-CSS/TeX/otf/MathJax_Size4-Regular.otf?V=2.7.5') format('opentype')}
.MathJax .noError {vertical-align: ; font-size: 90%; text-align: left; color: black; padding: 1px 3px; border: 1px solid}
</style><script src="./Orioye.E.project8.ipy_files/api.js.download" nonce=""></script><script src="./Orioye.E.project8.ipy_files/api(1).js.download" nonce=""></script><style type="text/css" media="screen" class="monaco-colors">.codicon-add:before { content: '\ea60'; }
.codicon-plus:before { content: '\ea60'; }
.codicon-gist-new:before { content: '\ea60'; }
.codicon-repo-create:before { content: '\ea60'; }
.codicon-lightbulb:before { content: '\ea61'; }
.codicon-light-bulb:before { content: '\ea61'; }
.codicon-repo:before { content: '\ea62'; }
.codicon-repo-delete:before { content: '\ea62'; }
.codicon-gist-fork:before { content: '\ea63'; }
.codicon-repo-forked:before { content: '\ea63'; }
.codicon-git-pull-request:before { content: '\ea64'; }
.codicon-git-pull-request-abandoned:before { content: '\ea64'; }
.codicon-record-keys:before { content: '\ea65'; }
.codicon-keyboard:before { content: '\ea65'; }
.codicon-tag:before { content: '\ea66'; }
.codicon-tag-add:before { content: '\ea66'; }
.codicon-tag-remove:before { content: '\ea66'; }
.codicon-person:before { content: '\ea67'; }
.codicon-person-follow:before { content: '\ea67'; }
.codicon-person-outline:before { content: '\ea67'; }
.codicon-person-filled:before { content: '\ea67'; }
.codicon-git-branch:before { content: '\ea68'; }
.codicon-git-branch-create:before { content: '\ea68'; }
.codicon-git-branch-delete:before { content: '\ea68'; }
.codicon-source-control:before { content: '\ea68'; }
.codicon-mirror:before { content: '\ea69'; }
.codicon-mirror-public:before { content: '\ea69'; }
.codicon-star:before { content: '\ea6a'; }
.codicon-star-add:before { content: '\ea6a'; }
.codicon-star-delete:before { content: '\ea6a'; }
.codicon-star-empty:before { content: '\ea6a'; }
.codicon-comment:before { content: '\ea6b'; }
.codicon-comment-add:before { content: '\ea6b'; }
.codicon-alert:before { content: '\ea6c'; }
.codicon-warning:before { content: '\ea6c'; }
.codicon-search:before { content: '\ea6d'; }
.codicon-search-save:before { content: '\ea6d'; }
.codicon-log-out:before { content: '\ea6e'; }
.codicon-sign-out:before { content: '\ea6e'; }
.codicon-log-in:before { content: '\ea6f'; }
.codicon-sign-in:before { content: '\ea6f'; }
.codicon-eye:before { content: '\ea70'; }
.codicon-eye-unwatch:before { content: '\ea70'; }
.codicon-eye-watch:before { content: '\ea70'; }
.codicon-circle-filled:before { content: '\ea71'; }
.codicon-primitive-dot:before { content: '\ea71'; }
.codicon-close-dirty:before { content: '\ea71'; }
.codicon-debug-breakpoint:before { content: '\ea71'; }
.codicon-debug-breakpoint-disabled:before { content: '\ea71'; }
.codicon-debug-hint:before { content: '\ea71'; }
.codicon-primitive-square:before { content: '\ea72'; }
.codicon-edit:before { content: '\ea73'; }
.codicon-pencil:before { content: '\ea73'; }
.codicon-info:before { content: '\ea74'; }
.codicon-issue-opened:before { content: '\ea74'; }
.codicon-gist-private:before { content: '\ea75'; }
.codicon-git-fork-private:before { content: '\ea75'; }
.codicon-lock:before { content: '\ea75'; }
.codicon-mirror-private:before { content: '\ea75'; }
.codicon-close:before { content: '\ea76'; }
.codicon-remove-close:before { content: '\ea76'; }
.codicon-x:before { content: '\ea76'; }
.codicon-repo-sync:before { content: '\ea77'; }
.codicon-sync:before { content: '\ea77'; }
.codicon-clone:before { content: '\ea78'; }
.codicon-desktop-download:before { content: '\ea78'; }
.codicon-beaker:before { content: '\ea79'; }
.codicon-microscope:before { content: '\ea79'; }
.codicon-vm:before { content: '\ea7a'; }
.codicon-device-desktop:before { content: '\ea7a'; }
.codicon-file:before { content: '\ea7b'; }
.codicon-file-text:before { content: '\ea7b'; }
.codicon-more:before { content: '\ea7c'; }
.codicon-ellipsis:before { content: '\ea7c'; }
.codicon-kebab-horizontal:before { content: '\ea7c'; }
.codicon-mail-reply:before { content: '\ea7d'; }
.codicon-reply:before { content: '\ea7d'; }
.codicon-organization:before { content: '\ea7e'; }
.codicon-organization-filled:before { content: '\ea7e'; }
.codicon-organization-outline:before { content: '\ea7e'; }
.codicon-new-file:before { content: '\ea7f'; }
.codicon-file-add:before { content: '\ea7f'; }
.codicon-new-folder:before { content: '\ea80'; }
.codicon-file-directory-create:before { content: '\ea80'; }
.codicon-trash:before { content: '\ea81'; }
.codicon-trashcan:before { content: '\ea81'; }
.codicon-history:before { content: '\ea82'; }
.codicon-clock:before { content: '\ea82'; }
.codicon-folder:before { content: '\ea83'; }
.codicon-file-directory:before { content: '\ea83'; }
.codicon-symbol-folder:before { content: '\ea83'; }
.codicon-logo-github:before { content: '\ea84'; }
.codicon-mark-github:before { content: '\ea84'; }
.codicon-github:before { content: '\ea84'; }
.codicon-terminal:before { content: '\ea85'; }
.codicon-console:before { content: '\ea85'; }
.codicon-repl:before { content: '\ea85'; }
.codicon-zap:before { content: '\ea86'; }
.codicon-symbol-event:before { content: '\ea86'; }
.codicon-error:before { content: '\ea87'; }
.codicon-stop:before { content: '\ea87'; }
.codicon-variable:before { content: '\ea88'; }
.codicon-symbol-variable:before { content: '\ea88'; }
.codicon-array:before { content: '\ea8a'; }
.codicon-symbol-array:before { content: '\ea8a'; }
.codicon-symbol-module:before { content: '\ea8b'; }
.codicon-symbol-package:before { content: '\ea8b'; }
.codicon-symbol-namespace:before { content: '\ea8b'; }
.codicon-symbol-object:before { content: '\ea8b'; }
.codicon-symbol-method:before { content: '\ea8c'; }
.codicon-symbol-function:before { content: '\ea8c'; }
.codicon-symbol-constructor:before { content: '\ea8c'; }
.codicon-symbol-boolean:before { content: '\ea8f'; }
.codicon-symbol-null:before { content: '\ea8f'; }
.codicon-symbol-numeric:before { content: '\ea90'; }
.codicon-symbol-number:before { content: '\ea90'; }
.codicon-symbol-structure:before { content: '\ea91'; }
.codicon-symbol-struct:before { content: '\ea91'; }
.codicon-symbol-parameter:before { content: '\ea92'; }
.codicon-symbol-type-parameter:before { content: '\ea92'; }
.codicon-symbol-key:before { content: '\ea93'; }
.codicon-symbol-text:before { content: '\ea93'; }
.codicon-symbol-reference:before { content: '\ea94'; }
.codicon-go-to-file:before { content: '\ea94'; }
.codicon-symbol-enum:before { content: '\ea95'; }
.codicon-symbol-value:before { content: '\ea95'; }
.codicon-symbol-ruler:before { content: '\ea96'; }
.codicon-symbol-unit:before { content: '\ea96'; }
.codicon-activate-breakpoints:before { content: '\ea97'; }
.codicon-archive:before { content: '\ea98'; }
.codicon-arrow-both:before { content: '\ea99'; }
.codicon-arrow-down:before { content: '\ea9a'; }
.codicon-arrow-left:before { content: '\ea9b'; }
.codicon-arrow-right:before { content: '\ea9c'; }
.codicon-arrow-small-down:before { content: '\ea9d'; }
.codicon-arrow-small-left:before { content: '\ea9e'; }
.codicon-arrow-small-right:before { content: '\ea9f'; }
.codicon-arrow-small-up:before { content: '\eaa0'; }
.codicon-arrow-up:before { content: '\eaa1'; }
.codicon-bell:before { content: '\eaa2'; }
.codicon-bold:before { content: '\eaa3'; }
.codicon-book:before { content: '\eaa4'; }
.codicon-bookmark:before { content: '\eaa5'; }
.codicon-debug-breakpoint-conditional-unverified:before { content: '\eaa6'; }
.codicon-debug-breakpoint-conditional:before { content: '\eaa7'; }
.codicon-debug-breakpoint-conditional-disabled:before { content: '\eaa7'; }
.codicon-debug-breakpoint-data-unverified:before { content: '\eaa8'; }
.codicon-debug-breakpoint-data:before { content: '\eaa9'; }
.codicon-debug-breakpoint-data-disabled:before { content: '\eaa9'; }
.codicon-debug-breakpoint-log-unverified:before { content: '\eaaa'; }
.codicon-debug-breakpoint-log:before { content: '\eaab'; }
.codicon-debug-breakpoint-log-disabled:before { content: '\eaab'; }
.codicon-briefcase:before { content: '\eaac'; }
.codicon-broadcast:before { content: '\eaad'; }
.codicon-browser:before { content: '\eaae'; }
.codicon-bug:before { content: '\eaaf'; }
.codicon-calendar:before { content: '\eab0'; }
.codicon-case-sensitive:before { content: '\eab1'; }
.codicon-check:before { content: '\eab2'; }
.codicon-checklist:before { content: '\eab3'; }
.codicon-chevron-down:before { content: '\eab4'; }
.codicon-drop-down-button:before { content: '\eab4'; }
.codicon-chevron-left:before { content: '\eab5'; }
.codicon-chevron-right:before { content: '\eab6'; }
.codicon-chevron-up:before { content: '\eab7'; }
.codicon-chrome-close:before { content: '\eab8'; }
.codicon-chrome-maximize:before { content: '\eab9'; }
.codicon-chrome-minimize:before { content: '\eaba'; }
.codicon-chrome-restore:before { content: '\eabb'; }
.codicon-circle:before { content: '\eabc'; }
.codicon-circle-outline:before { content: '\eabc'; }
.codicon-debug-breakpoint-unverified:before { content: '\eabc'; }
.codicon-circle-slash:before { content: '\eabd'; }
.codicon-circuit-board:before { content: '\eabe'; }
.codicon-clear-all:before { content: '\eabf'; }
.codicon-clippy:before { content: '\eac0'; }
.codicon-close-all:before { content: '\eac1'; }
.codicon-cloud-download:before { content: '\eac2'; }
.codicon-cloud-upload:before { content: '\eac3'; }
.codicon-code:before { content: '\eac4'; }
.codicon-collapse-all:before { content: '\eac5'; }
.codicon-color-mode:before { content: '\eac6'; }
.codicon-comment-discussion:before { content: '\eac7'; }
.codicon-compare-changes:before { content: '\eafd'; }
.codicon-credit-card:before { content: '\eac9'; }
.codicon-dash:before { content: '\eacc'; }
.codicon-dashboard:before { content: '\eacd'; }
.codicon-database:before { content: '\eace'; }
.codicon-debug-continue:before { content: '\eacf'; }
.codicon-debug-disconnect:before { content: '\ead0'; }
.codicon-debug-pause:before { content: '\ead1'; }
.codicon-debug-restart:before { content: '\ead2'; }
.codicon-debug-start:before { content: '\ead3'; }
.codicon-debug-step-into:before { content: '\ead4'; }
.codicon-debug-step-out:before { content: '\ead5'; }
.codicon-debug-step-over:before { content: '\ead6'; }
.codicon-debug-stop:before { content: '\ead7'; }
.codicon-debug:before { content: '\ead8'; }
.codicon-device-camera-video:before { content: '\ead9'; }
.codicon-device-camera:before { content: '\eada'; }
.codicon-device-mobile:before { content: '\eadb'; }
.codicon-diff-added:before { content: '\eadc'; }
.codicon-diff-ignored:before { content: '\eadd'; }
.codicon-diff-modified:before { content: '\eade'; }
.codicon-diff-removed:before { content: '\eadf'; }
.codicon-diff-renamed:before { content: '\eae0'; }
.codicon-diff:before { content: '\eae1'; }
.codicon-discard:before { content: '\eae2'; }
.codicon-editor-layout:before { content: '\eae3'; }
.codicon-empty-window:before { content: '\eae4'; }
.codicon-exclude:before { content: '\eae5'; }
.codicon-extensions:before { content: '\eae6'; }
.codicon-eye-closed:before { content: '\eae7'; }
.codicon-file-binary:before { content: '\eae8'; }
.codicon-file-code:before { content: '\eae9'; }
.codicon-file-media:before { content: '\eaea'; }
.codicon-file-pdf:before { content: '\eaeb'; }
.codicon-file-submodule:before { content: '\eaec'; }
.codicon-file-symlink-directory:before { content: '\eaed'; }
.codicon-file-symlink-file:before { content: '\eaee'; }
.codicon-file-zip:before { content: '\eaef'; }
.codicon-files:before { content: '\eaf0'; }
.codicon-filter:before { content: '\eaf1'; }
.codicon-flame:before { content: '\eaf2'; }
.codicon-fold-down:before { content: '\eaf3'; }
.codicon-fold-up:before { content: '\eaf4'; }
.codicon-fold:before { content: '\eaf5'; }
.codicon-folder-active:before { content: '\eaf6'; }
.codicon-folder-opened:before { content: '\eaf7'; }
.codicon-gear:before { content: '\eaf8'; }
.codicon-gift:before { content: '\eaf9'; }
.codicon-gist-secret:before { content: '\eafa'; }
.codicon-gist:before { content: '\eafb'; }
.codicon-git-commit:before { content: '\eafc'; }
.codicon-git-compare:before { content: '\eafd'; }
.codicon-git-merge:before { content: '\eafe'; }
.codicon-github-action:before { content: '\eaff'; }
.codicon-github-alt:before { content: '\eb00'; }
.codicon-globe:before { content: '\eb01'; }
.codicon-grabber:before { content: '\eb02'; }
.codicon-graph:before { content: '\eb03'; }
.codicon-gripper:before { content: '\eb04'; }
.codicon-heart:before { content: '\eb05'; }
.codicon-home:before { content: '\eb06'; }
.codicon-horizontal-rule:before { content: '\eb07'; }
.codicon-hubot:before { content: '\eb08'; }
.codicon-inbox:before { content: '\eb09'; }
.codicon-issue-closed:before { content: '\eba4'; }
.codicon-issue-reopened:before { content: '\eb0b'; }
.codicon-issues:before { content: '\eb0c'; }
.codicon-italic:before { content: '\eb0d'; }
.codicon-jersey:before { content: '\eb0e'; }
.codicon-json:before { content: '\eb0f'; }
.codicon-bracket:before { content: '\eb0f'; }
.codicon-kebab-vertical:before { content: '\eb10'; }
.codicon-key:before { content: '\eb11'; }
.codicon-law:before { content: '\eb12'; }
.codicon-lightbulb-autofix:before { content: '\eb13'; }
.codicon-link-external:before { content: '\eb14'; }
.codicon-link:before { content: '\eb15'; }
.codicon-list-ordered:before { content: '\eb16'; }
.codicon-list-unordered:before { content: '\eb17'; }
.codicon-live-share:before { content: '\eb18'; }
.codicon-loading:before { content: '\eb19'; }
.codicon-location:before { content: '\eb1a'; }
.codicon-mail-read:before { content: '\eb1b'; }
.codicon-mail:before { content: '\eb1c'; }
.codicon-markdown:before { content: '\eb1d'; }
.codicon-megaphone:before { content: '\eb1e'; }
.codicon-mention:before { content: '\eb1f'; }
.codicon-milestone:before { content: '\eb20'; }
.codicon-mortar-board:before { content: '\eb21'; }
.codicon-move:before { content: '\eb22'; }
.codicon-multiple-windows:before { content: '\eb23'; }
.codicon-mute:before { content: '\eb24'; }
.codicon-no-newline:before { content: '\eb25'; }
.codicon-note:before { content: '\eb26'; }
.codicon-octoface:before { content: '\eb27'; }
.codicon-open-preview:before { content: '\eb28'; }
.codicon-package:before { content: '\eb29'; }
.codicon-paintcan:before { content: '\eb2a'; }
.codicon-pin:before { content: '\eb2b'; }
.codicon-play:before { content: '\eb2c'; }
.codicon-run:before { content: '\eb2c'; }
.codicon-plug:before { content: '\eb2d'; }
.codicon-preserve-case:before { content: '\eb2e'; }
.codicon-preview:before { content: '\eb2f'; }
.codicon-project:before { content: '\eb30'; }
.codicon-pulse:before { content: '\eb31'; }
.codicon-question:before { content: '\eb32'; }
.codicon-quote:before { content: '\eb33'; }
.codicon-radio-tower:before { content: '\eb34'; }
.codicon-reactions:before { content: '\eb35'; }
.codicon-references:before { content: '\eb36'; }
.codicon-refresh:before { content: '\eb37'; }
.codicon-regex:before { content: '\eb38'; }
.codicon-remote-explorer:before { content: '\eb39'; }
.codicon-remote:before { content: '\eb3a'; }
.codicon-remove:before { content: '\eb3b'; }
.codicon-replace-all:before { content: '\eb3c'; }
.codicon-replace:before { content: '\eb3d'; }
.codicon-repo-clone:before { content: '\eb3e'; }
.codicon-repo-force-push:before { content: '\eb3f'; }
.codicon-repo-pull:before { content: '\eb40'; }
.codicon-repo-push:before { content: '\eb41'; }
.codicon-report:before { content: '\eb42'; }
.codicon-request-changes:before { content: '\eb43'; }
.codicon-rocket:before { content: '\eb44'; }
.codicon-root-folder-opened:before { content: '\eb45'; }
.codicon-root-folder:before { content: '\eb46'; }
.codicon-rss:before { content: '\eb47'; }
.codicon-ruby:before { content: '\eb48'; }
.codicon-save-all:before { content: '\eb49'; }
.codicon-save-as:before { content: '\eb4a'; }
.codicon-save:before { content: '\eb4b'; }
.codicon-screen-full:before { content: '\eb4c'; }
.codicon-screen-normal:before { content: '\eb4d'; }
.codicon-search-stop:before { content: '\eb4e'; }
.codicon-server:before { content: '\eb50'; }
.codicon-settings-gear:before { content: '\eb51'; }
.codicon-settings:before { content: '\eb52'; }
.codicon-shield:before { content: '\eb53'; }
.codicon-smiley:before { content: '\eb54'; }
.codicon-sort-precedence:before { content: '\eb55'; }
.codicon-split-horizontal:before { content: '\eb56'; }
.codicon-split-vertical:before { content: '\eb57'; }
.codicon-squirrel:before { content: '\eb58'; }
.codicon-star-full:before { content: '\eb59'; }
.codicon-star-half:before { content: '\eb5a'; }
.codicon-symbol-class:before { content: '\eb5b'; }
.codicon-symbol-color:before { content: '\eb5c'; }
.codicon-symbol-customcolor:before { content: '\eb5c'; }
.codicon-symbol-constant:before { content: '\eb5d'; }
.codicon-symbol-enum-member:before { content: '\eb5e'; }
.codicon-symbol-field:before { content: '\eb5f'; }
.codicon-symbol-file:before { content: '\eb60'; }
.codicon-symbol-interface:before { content: '\eb61'; }
.codicon-symbol-keyword:before { content: '\eb62'; }
.codicon-symbol-misc:before { content: '\eb63'; }
.codicon-symbol-operator:before { content: '\eb64'; }
.codicon-symbol-property:before { content: '\eb65'; }
.codicon-wrench:before { content: '\eb65'; }
.codicon-wrench-subaction:before { content: '\eb65'; }
.codicon-symbol-snippet:before { content: '\eb66'; }
.codicon-tasklist:before { content: '\eb67'; }
.codicon-telescope:before { content: '\eb68'; }
.codicon-text-size:before { content: '\eb69'; }
.codicon-three-bars:before { content: '\eb6a'; }
.codicon-thumbsdown:before { content: '\eb6b'; }
.codicon-thumbsup:before { content: '\eb6c'; }
.codicon-tools:before { content: '\eb6d'; }
.codicon-triangle-down:before { content: '\eb6e'; }
.codicon-triangle-left:before { content: '\eb6f'; }
.codicon-triangle-right:before { content: '\eb70'; }
.codicon-triangle-up:before { content: '\eb71'; }
.codicon-twitter:before { content: '\eb72'; }
.codicon-unfold:before { content: '\eb73'; }
.codicon-unlock:before { content: '\eb74'; }
.codicon-unmute:before { content: '\eb75'; }
.codicon-unverified:before { content: '\eb76'; }
.codicon-verified:before { content: '\eb77'; }
.codicon-versions:before { content: '\eb78'; }
.codicon-vm-active:before { content: '\eb79'; }
.codicon-vm-outline:before { content: '\eb7a'; }
.codicon-vm-running:before { content: '\eb7b'; }
.codicon-watch:before { content: '\eb7c'; }
.codicon-whitespace:before { content: '\eb7d'; }
.codicon-whole-word:before { content: '\eb7e'; }
.codicon-window:before { content: '\eb7f'; }
.codicon-word-wrap:before { content: '\eb80'; }
.codicon-zoom-in:before { content: '\eb81'; }
.codicon-zoom-out:before { content: '\eb82'; }
.codicon-list-filter:before { content: '\eb83'; }
.codicon-list-flat:before { content: '\eb84'; }
.codicon-list-selection:before { content: '\eb85'; }
.codicon-selection:before { content: '\eb85'; }
.codicon-list-tree:before { content: '\eb86'; }
.codicon-debug-breakpoint-function-unverified:before { content: '\eb87'; }
.codicon-debug-breakpoint-function:before { content: '\eb88'; }
.codicon-debug-breakpoint-function-disabled:before { content: '\eb88'; }
.codicon-debug-stackframe-active:before { content: '\eb89'; }
.codicon-circle-small-filled:before { content: '\eb8a'; }
.codicon-debug-stackframe-dot:before { content: '\eb8a'; }
.codicon-debug-stackframe:before { content: '\eb8b'; }
.codicon-debug-stackframe-focused:before { content: '\eb8b'; }
.codicon-debug-breakpoint-unsupported:before { content: '\eb8c'; }
.codicon-symbol-string:before { content: '\eb8d'; }
.codicon-debug-reverse-continue:before { content: '\eb8e'; }
.codicon-debug-step-back:before { content: '\eb8f'; }
.codicon-debug-restart-frame:before { content: '\eb90'; }
.codicon-call-incoming:before { content: '\eb92'; }
.codicon-call-outgoing:before { content: '\eb93'; }
.codicon-menu:before { content: '\eb94'; }
.codicon-expand-all:before { content: '\eb95'; }
.codicon-feedback:before { content: '\eb96'; }
.codicon-group-by-ref-type:before { content: '\eb97'; }
.codicon-ungroup-by-ref-type:before { content: '\eb98'; }
.codicon-account:before { content: '\eb99'; }
.codicon-bell-dot:before { content: '\eb9a'; }
.codicon-debug-console:before { content: '\eb9b'; }
.codicon-library:before { content: '\eb9c'; }
.codicon-output:before { content: '\eb9d'; }
.codicon-run-all:before { content: '\eb9e'; }
.codicon-sync-ignored:before { content: '\eb9f'; }
.codicon-pinned:before { content: '\eba0'; }
.codicon-github-inverted:before { content: '\eba1'; }
.codicon-debug-alt:before { content: '\eb91'; }
.codicon-server-process:before { content: '\eba2'; }
.codicon-server-environment:before { content: '\eba3'; }
.codicon-pass:before { content: '\eba4'; }
.codicon-stop-circle:before { content: '\eba5'; }
.codicon-play-circle:before { content: '\eba6'; }
.codicon-record:before { content: '\eba7'; }
.codicon-debug-alt-small:before { content: '\eba8'; }
.codicon-vm-connect:before { content: '\eba9'; }
.codicon-cloud:before { content: '\ebaa'; }
.codicon-merge:before { content: '\ebab'; }
.codicon-export:before { content: '\ebac'; }
.codicon-graph-left:before { content: '\ebad'; }
.codicon-magnet:before { content: '\ebae'; }
.codicon-notebook:before { content: '\ebaf'; }
.codicon-redo:before { content: '\ebb0'; }
.codicon-check-all:before { content: '\ebb1'; }
.codicon-pinned-dirty:before { content: '\ebb2'; }
.codicon-pass-filled:before { content: '\ebb3'; }
.codicon-circle-large-filled:before { content: '\ebb4'; }
.codicon-circle-large:before { content: '\ebb5'; }
.codicon-circle-large-outline:before { content: '\ebb5'; }
.codicon-combine:before { content: '\ebb6'; }
.codicon-gather:before { content: '\ebb6'; }
.codicon-table:before { content: '\ebb7'; }
.codicon-variable-group:before { content: '\ebb8'; }
.codicon-type-hierarchy:before { content: '\ebb9'; }
.codicon-type-hierarchy-sub:before { content: '\ebba'; }
.codicon-type-hierarchy-super:before { content: '\ebbb'; }
.codicon-git-pull-request-create:before { content: '\ebbc'; }
.codicon-run-above:before { content: '\ebbd'; }
.codicon-run-below:before { content: '\ebbe'; }
.codicon-notebook-template:before { content: '\ebbf'; }
.codicon-debug-rerun:before { content: '\ebc0'; }
.codicon-workspace-trusted:before { content: '\ebc1'; }
.codicon-workspace-untrusted:before { content: '\ebc2'; }
.codicon-workspace-unspecified:before { content: '\ebc3'; }
.codicon-terminal-cmd:before { content: '\ebc4'; }
.codicon-terminal-debian:before { content: '\ebc5'; }
.codicon-terminal-linux:before { content: '\ebc6'; }
.codicon-terminal-powershell:before { content: '\ebc7'; }
.codicon-terminal-tmux:before { content: '\ebc8'; }
.codicon-terminal-ubuntu:before { content: '\ebc9'; }
.codicon-terminal-bash:before { content: '\ebca'; }
.codicon-arrow-swap:before { content: '\ebcb'; }
.codicon-copy:before { content: '\ebcc'; }
.codicon-person-add:before { content: '\ebcd'; }
.codicon-filter-filled:before { content: '\ebce'; }
.codicon-wand:before { content: '\ebcf'; }
.codicon-debug-line-by-line:before { content: '\ebd0'; }
.codicon-inspect:before { content: '\ebd1'; }
.codicon-layers:before { content: '\ebd2'; }
.codicon-layers-dot:before { content: '\ebd3'; }
.codicon-layers-active:before { content: '\ebd4'; }
.codicon-compass:before { content: '\ebd5'; }
.codicon-compass-dot:before { content: '\ebd6'; }
.codicon-compass-active:before { content: '\ebd7'; }
.codicon-azure:before { content: '\ebd8'; }
.codicon-issue-draft:before { content: '\ebd9'; }
.codicon-git-pull-request-closed:before { content: '\ebda'; }
.codicon-git-pull-request-draft:before { content: '\ebdb'; }
.codicon-debug-all:before { content: '\ebdc'; }
.codicon-debug-coverage:before { content: '\ebdd'; }
.codicon-run-errors:before { content: '\ebde'; }
.codicon-folder-library:before { content: '\ebdf'; }
.codicon-debug-continue-small:before { content: '\ebe0'; }
.codicon-beaker-stop:before { content: '\ebe1'; }
.codicon-graph-line:before { content: '\ebe2'; }
.codicon-graph-scatter:before { content: '\ebe3'; }
.codicon-pie-chart:before { content: '\ebe4'; }
.codicon-bracket-dot:before { content: '\ebe5'; }
.codicon-bracket-error:before { content: '\ebe6'; }
.codicon-lock-small:before { content: '\ebe7'; }
.codicon-azure-devops:before { content: '\ebe8'; }
.codicon-verified-filled:before { content: '\ebe9'; }
.codicon-newline:before { content: '\ebea'; }
.codicon-layout:before { content: '\ebeb'; }
.codicon-layout-activitybar-left:before { content: '\ebec'; }
.codicon-layout-activitybar-right:before { content: '\ebed'; }
.codicon-layout-panel-left:before { content: '\ebee'; }
.codicon-layout-panel-center:before { content: '\ebef'; }
.codicon-layout-panel-justify:before { content: '\ebf0'; }
.codicon-layout-panel-right:before { content: '\ebf1'; }
.codicon-layout-panel:before { content: '\ebf2'; }
.codicon-layout-sidebar-left:before { content: '\ebf3'; }
.codicon-layout-sidebar-right:before { content: '\ebf4'; }
.codicon-layout-statusbar:before { content: '\ebf5'; }
.codicon-layout-menubar:before { content: '\ebf6'; }
.codicon-layout-centered:before { content: '\ebf7'; }
.codicon-layout-sidebar-right-off:before { content: '\ec00'; }
.codicon-layout-panel-off:before { content: '\ec01'; }
.codicon-layout-sidebar-left-off:before { content: '\ec02'; }
.codicon-target:before { content: '\ebf8'; }
.codicon-indent:before { content: '\ebf9'; }
.codicon-record-small:before { content: '\ebfa'; }
.codicon-error-small:before { content: '\ebfb'; }
.codicon-arrow-circle-down:before { content: '\ebfc'; }
.codicon-arrow-circle-left:before { content: '\ebfd'; }
.codicon-arrow-circle-right:before { content: '\ebfe'; }
.codicon-arrow-circle-up:before { content: '\ebff'; }
.codicon-heart-filled:before { content: '\ec04'; }
.codicon-map:before { content: '\ec05'; }
.codicon-map-filled:before { content: '\ec06'; }
.codicon-circle-small:before { content: '\ec07'; }
.codicon-bell-slash:before { content: '\ec08'; }
.codicon-bell-slash-dot:before { content: '\ec09'; }
.codicon-comment-unresolved:before { content: '\ec0a'; }
.codicon-git-pull-request-go-to-changes:before { content: '\ec0b'; }
.codicon-git-pull-request-new-changes:before { content: '\ec0c'; }
.codicon-search-fuzzy:before { content: '\ec0d'; }
.codicon-comment-draft:before { content: '\ec0e'; }
.codicon-send:before { content: '\ec0f'; }
.codicon-sparkle:before { content: '\ec10'; }
.codicon-insert:before { content: '\ec11'; }
.codicon-dialog-error:before { content: '\ea87'; }
.codicon-dialog-warning:before { content: '\ea6c'; }
.codicon-dialog-info:before { content: '\ea74'; }
.codicon-dialog-close:before { content: '\ea76'; }
.codicon-tree-item-expanded:before { content: '\eab4'; }
.codicon-tree-filter-on-type-on:before { content: '\eb83'; }
.codicon-tree-filter-on-type-off:before { content: '\eb85'; }
.codicon-tree-filter-clear:before { content: '\ea76'; }
.codicon-tree-item-loading:before { content: '\eb19'; }
.codicon-menu-selection:before { content: '\eab2'; }
.codicon-menu-submenu:before { content: '\eab6'; }
.codicon-menubar-more:before { content: '\ea7c'; }
.codicon-scrollbar-button-left:before { content: '\eb6f'; }
.codicon-scrollbar-button-right:before { content: '\eb70'; }
.codicon-scrollbar-button-up:before { content: '\eb71'; }
.codicon-scrollbar-button-down:before { content: '\eb6e'; }
.codicon-toolbar-more:before { content: '\ea7c'; }
.codicon-quick-input-back:before { content: '\ea9b'; }
.codicon-widget-close:before { content: '\ea76'; }
.codicon-goto-previous-location:before { content: '\eaa1'; }
.codicon-goto-next-location:before { content: '\ea9a'; }
.codicon-diff-review-insert:before { content: '\ea60'; }
.codicon-diff-review-remove:before { content: '\eb3b'; }
.codicon-diff-review-close:before { content: '\ea76'; }
.codicon-parameter-hints-next:before { content: '\eab4'; }
.codicon-parameter-hints-previous:before { content: '\eab7'; }
.codicon-suggest-more-info:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-next:before { content: '\eab6'; }
.codicon-inline-suggestion-hints-previous:before { content: '\eab5'; }
.codicon-diff-insert:before { content: '\ea60'; }
.codicon-diff-remove:before { content: '\eb3b'; }
.codicon-find-selection:before { content: '\eb85'; }
.codicon-find-collapsed:before { content: '\eab6'; }
.codicon-find-expanded:before { content: '\eab4'; }
.codicon-find-replace:before { content: '\eb3d'; }
.codicon-find-replace-all:before { content: '\eb3c'; }
.codicon-find-previous-match:before { content: '\eaa1'; }
.codicon-find-next-match:before { content: '\ea9a'; }
.codicon-folding-expanded:before { content: '\eab4'; }
.codicon-folding-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-collapsed:before { content: '\eab6'; }
.codicon-folding-manual-expanded:before { content: '\eab4'; }
.codicon-marker-navigation-next:before { content: '\ea9a'; }
.codicon-marker-navigation-previous:before { content: '\eaa1'; }
.codicon-extensions-warning-message:before { content: '\ea6c'; }
.monaco-editor .inputarea.ime-input { background-color: #1e1e1e; }
.monaco-editor .view-overlays .current-line { border: 2px solid #282828; }
.monaco-editor .margin-view-overlays .current-line-margin { border: 2px solid #282828; }
.monaco-editor .bracket-indent-guide.lvl-0 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-1 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-2 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-3 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-4 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-5 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-6 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-7 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-8 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-9 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-10 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-11 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-12 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-13 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-14 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-15 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-16 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-17 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-18 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-19 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-20 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-21 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-22 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-23 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-24 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-25 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-26 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .bracket-indent-guide.lvl-27 { --guide-color: rgba(255, 215, 0, 0.3); --guide-color-active: #ffd700; }
.monaco-editor .bracket-indent-guide.lvl-28 { --guide-color: rgba(218, 112, 214, 0.3); --guide-color-active: #da70d6; }
.monaco-editor .bracket-indent-guide.lvl-29 { --guide-color: rgba(23, 159, 255, 0.3); --guide-color-active: #179fff; }
.monaco-editor .vertical { box-shadow: 1px 0 0 0 var(--guide-color) inset; }
.monaco-editor .horizontal-top { border-top: 1px solid var(--guide-color); }
.monaco-editor .horizontal-bottom { border-bottom: 1px solid var(--guide-color); }
.monaco-editor .vertical.indent-active { box-shadow: 1px 0 0 0 var(--guide-color-active) inset; }
.monaco-editor .horizontal-top.indent-active { border-top: 1px solid var(--guide-color-active); }
.monaco-editor .horizontal-bottom.indent-active { border-bottom: 1px solid var(--guide-color-active); }
.monaco-editor .line-numbers.dimmed-line-number { color: rgba(133, 133, 133, 0.4); }
.monaco-editor .cursors-layer .cursor { background-color: #aeafad; border-color: #aeafad; color: #515052; }
.monaco-editor .unexpected-closing-bracket { color: rgba(255, 18, 18, 0.8); }
.monaco-editor .bracket-highlighting-0 { color: #ffd700; }
.monaco-editor .bracket-highlighting-1 { color: #da70d6; }
.monaco-editor .bracket-highlighting-2 { color: #179fff; }
.monaco-editor .bracket-highlighting-3 { color: #ffd700; }
.monaco-editor .bracket-highlighting-4 { color: #da70d6; }
.monaco-editor .bracket-highlighting-5 { color: #179fff; }
.monaco-editor .bracket-highlighting-6 { color: #ffd700; }
.monaco-editor .bracket-highlighting-7 { color: #da70d6; }
.monaco-editor .bracket-highlighting-8 { color: #179fff; }
.monaco-editor .bracket-highlighting-9 { color: #ffd700; }
.monaco-editor .bracket-highlighting-10 { color: #da70d6; }
.monaco-editor .bracket-highlighting-11 { color: #179fff; }
.monaco-editor .bracket-highlighting-12 { color: #ffd700; }
.monaco-editor .bracket-highlighting-13 { color: #da70d6; }
.monaco-editor .bracket-highlighting-14 { color: #179fff; }
.monaco-editor .bracket-highlighting-15 { color: #ffd700; }
.monaco-editor .bracket-highlighting-16 { color: #da70d6; }
.monaco-editor .bracket-highlighting-17 { color: #179fff; }
.monaco-editor .bracket-highlighting-18 { color: #ffd700; }
.monaco-editor .bracket-highlighting-19 { color: #da70d6; }
.monaco-editor .bracket-highlighting-20 { color: #179fff; }
.monaco-editor .bracket-highlighting-21 { color: #ffd700; }
.monaco-editor .bracket-highlighting-22 { color: #da70d6; }
.monaco-editor .bracket-highlighting-23 { color: #179fff; }
.monaco-editor .bracket-highlighting-24 { color: #ffd700; }
.monaco-editor .bracket-highlighting-25 { color: #da70d6; }
.monaco-editor .bracket-highlighting-26 { color: #179fff; }
.monaco-editor .bracket-highlighting-27 { color: #ffd700; }
.monaco-editor .bracket-highlighting-28 { color: #da70d6; }
.monaco-editor .bracket-highlighting-29 { color: #179fff; }
.monaco-editor .squiggly-error { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23f14c4c'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-warning { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%23cca700'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-info { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D'http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg'%20viewBox%3D'0%200%206%203'%20enable-background%3D'new%200%200%206%203'%20height%3D'3'%20width%3D'6'%3E%3Cg%20fill%3D'%233794ff'%3E%3Cpolygon%20points%3D'5.5%2C0%202.5%2C3%201.1%2C3%204.1%2C0'%2F%3E%3Cpolygon%20points%3D'4%2C0%206%2C2%206%2C0.6%205.4%2C0'%2F%3E%3Cpolygon%20points%3D'0%2C2%201%2C3%202.4%2C3%200%2C0.6'%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") repeat-x bottom left; }
.monaco-editor .squiggly-hint { background: url("data:image/svg+xml,%3Csvg%20xmlns%3D%22http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg%22%20height%3D%223%22%20width%3D%2212%22%3E%3Cg%20fill%3D%22rgba(238%2C%20238%2C%20238%2C%200.7)%22%3E%3Ccircle%20cx%3D%221%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%225%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3Ccircle%20cx%3D%229%22%20cy%3D%221%22%20r%3D%221%22%2F%3E%3C%2Fg%3E%3C%2Fsvg%3E") no-repeat bottom left; }
.monaco-editor.showUnused .squiggly-inline-unnecessary { opacity: 0.667; }
.monaco-editor .selectionHighlight { background-color: rgba(173, 214, 255, 0.07); }

	.monaco-editor .diagonal-fill {
		background-image: linear-gradient(
			-45deg,
			rgba(204, 204, 204, 0.2) 12.5%,
			#0000 12.5%, #0000 50%,
			rgba(204, 204, 204, 0.2) 50%, rgba(204, 204, 204, 0.2) 62.5%,
			#0000 62.5%, #0000 100%
		);
		background-size: 8px 8px;
	}
	
.monaco-editor .findMatch { background-color: rgba(234, 92, 0, 0.33); }
.monaco-editor .currentFindMatch { background-color: #515c6a; }
.monaco-editor .findScope { background-color: rgba(58, 61, 65, 0.4); }
.monaco-editor .find-widget { background-color: #252526; }
.monaco-editor .find-widget { box-shadow: 0 0 8px 2px rgba(0, 0, 0, 0.36); }
.monaco-editor .find-widget { color: #cccccc; }
.monaco-editor .find-widget.no-results .matchesCount { color: #f48771; }
.monaco-editor .find-widget .monaco-sash { background-color: #454545; }

		.monaco-editor .find-widget .button:not(.disabled):hover,
		.monaco-editor .find-widget .codicon-find-selection:hover {
			background-color: rgba(90, 93, 94, 0.31) !important;
		}
	
.monaco-editor .find-widget .monaco-inputbox.synthetic-focus { outline-color: #007fd4; }
.monaco-editor .monaco-hover .hover-row:not(:first-child):not(:empty) { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-top: 1px solid rgba(69, 69, 69, 0.5); }
.monaco-editor .monaco-hover hr { border-bottom: 0px solid rgba(69, 69, 69, 0.5); }
.monaco-editor { --vscode-foreground: #cccccc;
--vscode-disabledForeground: rgba(204, 204, 204, 0.5);
--vscode-errorForeground: #f48771;
--vscode-descriptionForeground: rgba(204, 204, 204, 0.7);
--vscode-icon-foreground: #c5c5c5;
--vscode-focusBorder: #007fd4;
--vscode-textSeparator-foreground: rgba(255, 255, 255, 0.18);
--vscode-textLink-foreground: #3794ff;
--vscode-textLink-activeForeground: #3794ff;
--vscode-textPreformat-foreground: #d7ba7d;
--vscode-textBlockQuote-background: rgba(127, 127, 127, 0.1);
--vscode-textBlockQuote-border: rgba(0, 122, 204, 0.5);
--vscode-textCodeBlock-background: rgba(10, 10, 10, 0.4);
--vscode-widget-shadow: rgba(0, 0, 0, 0.36);
--vscode-input-background: #3c3c3c;
--vscode-input-foreground: #cccccc;
--vscode-inputOption-activeBorder: #007acc;
--vscode-inputOption-hoverBackground: rgba(90, 93, 94, 0.5);
--vscode-inputOption-activeBackground: rgba(0, 127, 212, 0.4);
--vscode-inputOption-activeForeground: #ffffff;
--vscode-input-placeholderForeground: rgba(204, 204, 204, 0.5);
--vscode-inputValidation-infoBackground: #063b49;
--vscode-inputValidation-infoBorder: #007acc;
--vscode-inputValidation-warningBackground: #352a05;
--vscode-inputValidation-warningBorder: #b89500;
--vscode-inputValidation-errorBackground: #5a1d1d;
--vscode-inputValidation-errorBorder: #be1100;
--vscode-dropdown-background: #3c3c3c;
--vscode-dropdown-foreground: #f0f0f0;
--vscode-dropdown-border: #3c3c3c;
--vscode-button-foreground: #ffffff;
--vscode-button-separator: rgba(255, 255, 255, 0.4);
--vscode-button-background: #0e639c;
--vscode-button-hoverBackground: #1177bb;
--vscode-button-secondaryForeground: #ffffff;
--vscode-button-secondaryBackground: #3a3d41;
--vscode-button-secondaryHoverBackground: #45494e;
--vscode-badge-background: #4d4d4d;
--vscode-badge-foreground: #ffffff;
--vscode-scrollbar-shadow: #000000;
--vscode-scrollbarSlider-background: rgba(121, 121, 121, 0.4);
--vscode-scrollbarSlider-hoverBackground: rgba(100, 100, 100, 0.7);
--vscode-scrollbarSlider-activeBackground: rgba(191, 191, 191, 0.4);
--vscode-progressBar-background: #0e70c0;
--vscode-editorError-foreground: #f14c4c;
--vscode-editorWarning-foreground: #cca700;
--vscode-editorInfo-foreground: #3794ff;
--vscode-editorHint-foreground: rgba(238, 238, 238, 0.7);
--vscode-sash-hoverBorder: #007fd4;
--vscode-editor-background: #1e1e1e;
--vscode-editor-foreground: #d4d4d4;
--vscode-editorStickyScroll-background: #1e1e1e;
--vscode-editorStickyScrollHover-background: #2a2d2e;
--vscode-editorWidget-background: #252526;
--vscode-editorWidget-foreground: #cccccc;
--vscode-editorWidget-border: #454545;
--vscode-quickInput-background: #252526;
--vscode-quickInput-foreground: #cccccc;
--vscode-quickInputTitle-background: rgba(255, 255, 255, 0.1);
--vscode-pickerGroup-foreground: #3794ff;
--vscode-pickerGroup-border: #3f3f46;
--vscode-keybindingLabel-background: rgba(128, 128, 128, 0.17);
--vscode-keybindingLabel-foreground: #cccccc;
--vscode-keybindingLabel-border: rgba(51, 51, 51, 0.6);
--vscode-keybindingLabel-bottomBorder: rgba(68, 68, 68, 0.6);
--vscode-editor-selectionBackground: #264f78;
--vscode-editor-inactiveSelectionBackground: #3a3d41;
--vscode-editor-selectionHighlightBackground: rgba(173, 214, 255, 0.15);
--vscode-editor-findMatchBackground: #515c6a;
--vscode-editor-findMatchHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editor-findRangeHighlightBackground: rgba(58, 61, 65, 0.4);
--vscode-searchEditor-findMatchBackground: rgba(234, 92, 0, 0.22);
--vscode-search-resultsInfoForeground: rgba(204, 204, 204, 0.65);
--vscode-editor-hoverHighlightBackground: rgba(38, 79, 120, 0.25);
--vscode-editorHoverWidget-background: #252526;
--vscode-editorHoverWidget-foreground: #cccccc;
--vscode-editorHoverWidget-border: #454545;
--vscode-editorHoverWidget-statusBarBackground: #2c2c2d;
--vscode-editorLink-activeForeground: #4e94ce;
--vscode-editorInlayHint-foreground: #cccccc;
--vscode-editorInlayHint-background: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-typeForeground: #cccccc;
--vscode-editorInlayHint-typeBackground: rgba(77, 77, 77, 0.25);
--vscode-editorInlayHint-parameterForeground: #cccccc;
--vscode-editorInlayHint-parameterBackground: rgba(77, 77, 77, 0.25);
--vscode-editorLightBulb-foreground: #ffcc00;
--vscode-editorLightBulbAutoFix-foreground: #75beff;
--vscode-diffEditor-insertedTextBackground: #234521;
--vscode-diffEditor-removedTextBackground: #5b2022;
--vscode-diffEditor-insertedLineBackground: #22331f;
--vscode-diffEditor-removedLineBackground: #3c1a1a;
--vscode-diffEditor-diagonalFill: rgba(204, 204, 204, 0.2);
--vscode-diffEditor-unchangedRegionBackground: #3e3e3e;
--vscode-diffEditor-unchangedRegionForeground: #a3a2a2;
--vscode-diffEditor-unchangedCodeBackground: rgba(116, 116, 116, 0.16);
--vscode-list-focusOutline: #007fd4;
--vscode-list-activeSelectionBackground: #04395e;
--vscode-list-activeSelectionForeground: #ffffff;
--vscode-list-inactiveSelectionBackground: #37373d;
--vscode-list-hoverBackground: #2a2d2e;
--vscode-list-dropBackground: #062f4a;
--vscode-list-highlightForeground: #2aaaff;
--vscode-list-focusHighlightForeground: #2aaaff;
--vscode-list-invalidItemForeground: #b89500;
--vscode-list-errorForeground: #f88070;
--vscode-list-warningForeground: #cca700;
--vscode-listFilterWidget-background: #252526;
--vscode-listFilterWidget-outline: rgba(0, 0, 0, 0);
--vscode-listFilterWidget-noMatchesOutline: #be1100;
--vscode-listFilterWidget-shadow: rgba(0, 0, 0, 0.36);
--vscode-list-filterMatchBackground: rgba(234, 92, 0, 0.33);
--vscode-tree-indentGuidesStroke: #585858;
--vscode-tree-inactiveIndentGuidesStroke: rgba(88, 88, 88, 0.4);
--vscode-tree-tableColumnsBorder: rgba(204, 204, 204, 0.13);
--vscode-tree-tableOddRowsBackground: rgba(204, 204, 204, 0.04);
--vscode-list-deemphasizedForeground: #8c8c8c;
--vscode-checkbox-background: #3c3c3c;
--vscode-checkbox-selectBackground: #252526;
--vscode-checkbox-foreground: #f0f0f0;
--vscode-checkbox-border: #3c3c3c;
--vscode-checkbox-selectBorder: #c5c5c5;
--vscode-quickInputList-focusForeground: #ffffff;
--vscode-quickInputList-focusBackground: #04395e;
--vscode-menu-foreground: #f0f0f0;
--vscode-menu-background: #3c3c3c;
--vscode-menu-selectionForeground: #ffffff;
--vscode-menu-selectionBackground: #04395e;
--vscode-menu-separatorBackground: #606060;
--vscode-toolbar-hoverBackground: rgba(90, 93, 94, 0.31);
--vscode-toolbar-activeBackground: rgba(99, 102, 103, 0.31);
--vscode-editor-snippetTabstopHighlightBackground: rgba(124, 124, 124, 0.3);
--vscode-editor-snippetFinalTabstopHighlightBorder: #525252;
--vscode-breadcrumb-foreground: rgba(204, 204, 204, 0.8);
--vscode-breadcrumb-background: #1e1e1e;
--vscode-breadcrumb-focusForeground: #e0e0e0;
--vscode-breadcrumb-activeSelectionForeground: #e0e0e0;
--vscode-breadcrumbPicker-background: #252526;
--vscode-merge-currentHeaderBackground: rgba(64, 200, 174, 0.5);
--vscode-merge-currentContentBackground: rgba(64, 200, 174, 0.2);
--vscode-merge-incomingHeaderBackground: rgba(64, 166, 255, 0.5);
--vscode-merge-incomingContentBackground: rgba(64, 166, 255, 0.2);
--vscode-merge-commonHeaderBackground: rgba(96, 96, 96, 0.4);
--vscode-merge-commonContentBackground: rgba(96, 96, 96, 0.16);
--vscode-editorOverviewRuler-currentContentForeground: rgba(64, 200, 174, 0.5);
--vscode-editorOverviewRuler-incomingContentForeground: rgba(64, 166, 255, 0.5);
--vscode-editorOverviewRuler-commonContentForeground: rgba(96, 96, 96, 0.4);
--vscode-editorOverviewRuler-findMatchForeground: rgba(209, 134, 22, 0.49);
--vscode-editorOverviewRuler-selectionHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-minimap-findMatchHighlight: #d18616;
--vscode-minimap-selectionOccurrenceHighlight: #676767;
--vscode-minimap-selectionHighlight: #264f78;
--vscode-minimap-errorHighlight: rgba(255, 18, 18, 0.7);
--vscode-minimap-warningHighlight: #cca700;
--vscode-minimap-foregroundOpacity: #000000;
--vscode-minimapSlider-background: rgba(121, 121, 121, 0.2);
--vscode-minimapSlider-hoverBackground: rgba(100, 100, 100, 0.35);
--vscode-minimapSlider-activeBackground: rgba(191, 191, 191, 0.2);
--vscode-problemsErrorIcon-foreground: #f14c4c;
--vscode-problemsWarningIcon-foreground: #cca700;
--vscode-problemsInfoIcon-foreground: #3794ff;
--vscode-charts-foreground: #cccccc;
--vscode-charts-lines: rgba(204, 204, 204, 0.5);
--vscode-charts-red: #f14c4c;
--vscode-charts-blue: #3794ff;
--vscode-charts-yellow: #cca700;
--vscode-charts-orange: #d18616;
--vscode-charts-green: #89d185;
--vscode-charts-purple: #b180d7;
--vscode-symbolIcon-arrayForeground: #cccccc;
--vscode-symbolIcon-booleanForeground: #cccccc;
--vscode-symbolIcon-classForeground: #ee9d28;
--vscode-symbolIcon-colorForeground: #cccccc;
--vscode-symbolIcon-constantForeground: #cccccc;
--vscode-symbolIcon-constructorForeground: #b180d7;
--vscode-symbolIcon-enumeratorForeground: #ee9d28;
--vscode-symbolIcon-enumeratorMemberForeground: #75beff;
--vscode-symbolIcon-eventForeground: #ee9d28;
--vscode-symbolIcon-fieldForeground: #75beff;
--vscode-symbolIcon-fileForeground: #cccccc;
--vscode-symbolIcon-folderForeground: #cccccc;
--vscode-symbolIcon-functionForeground: #b180d7;
--vscode-symbolIcon-interfaceForeground: #75beff;
--vscode-symbolIcon-keyForeground: #cccccc;
--vscode-symbolIcon-keywordForeground: #cccccc;
--vscode-symbolIcon-methodForeground: #b180d7;
--vscode-symbolIcon-moduleForeground: #cccccc;
--vscode-symbolIcon-namespaceForeground: #cccccc;
--vscode-symbolIcon-nullForeground: #cccccc;
--vscode-symbolIcon-numberForeground: #cccccc;
--vscode-symbolIcon-objectForeground: #cccccc;
--vscode-symbolIcon-operatorForeground: #cccccc;
--vscode-symbolIcon-packageForeground: #cccccc;
--vscode-symbolIcon-propertyForeground: #cccccc;
--vscode-symbolIcon-referenceForeground: #cccccc;
--vscode-symbolIcon-snippetForeground: #cccccc;
--vscode-symbolIcon-stringForeground: #cccccc;
--vscode-symbolIcon-structForeground: #cccccc;
--vscode-symbolIcon-textForeground: #cccccc;
--vscode-symbolIcon-typeParameterForeground: #cccccc;
--vscode-symbolIcon-unitForeground: #cccccc;
--vscode-symbolIcon-variableForeground: #75beff;
--vscode-editor-lineHighlightBorder: #282828;
--vscode-editor-rangeHighlightBackground: rgba(255, 255, 255, 0.04);
--vscode-editor-symbolHighlightBackground: rgba(234, 92, 0, 0.33);
--vscode-editorCursor-foreground: #aeafad;
--vscode-editorWhitespace-foreground: rgba(227, 228, 226, 0.16);
--vscode-editorIndentGuide-background: #404040;
--vscode-editorIndentGuide-activeBackground: #707070;
--vscode-editorLineNumber-foreground: #858585;
--vscode-editorActiveLineNumber-foreground: #c6c6c6;
--vscode-editorLineNumber-activeForeground: #c6c6c6;
--vscode-editorRuler-foreground: #5a5a5a;
--vscode-editorCodeLens-foreground: #999999;
--vscode-editorBracketMatch-background: rgba(0, 100, 0, 0.1);
--vscode-editorBracketMatch-border: #888888;
--vscode-editorOverviewRuler-border: rgba(127, 127, 127, 0.3);
--vscode-editorGutter-background: #1e1e1e;
--vscode-editorUnnecessaryCode-opacity: rgba(0, 0, 0, 0.67);
--vscode-editorGhostText-foreground: rgba(255, 255, 255, 0.34);
--vscode-editorOverviewRuler-rangeHighlightForeground: rgba(0, 122, 204, 0.6);
--vscode-editorOverviewRuler-errorForeground: rgba(255, 18, 18, 0.7);
--vscode-editorOverviewRuler-warningForeground: #cca700;
--vscode-editorOverviewRuler-infoForeground: #3794ff;
--vscode-editorBracketHighlight-foreground1: #ffd700;
--vscode-editorBracketHighlight-foreground2: #da70d6;
--vscode-editorBracketHighlight-foreground3: #179fff;
--vscode-editorBracketHighlight-foreground4: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground5: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-foreground6: rgba(0, 0, 0, 0);
--vscode-editorBracketHighlight-unexpectedBracket-foreground: rgba(255, 18, 18, 0.8);
--vscode-editorBracketPairGuide-background1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-background6: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground1: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground2: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground3: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground4: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground5: rgba(0, 0, 0, 0);
--vscode-editorBracketPairGuide-activeBackground6: rgba(0, 0, 0, 0);
--vscode-editorUnicodeHighlight-border: #bd9b03;
--vscode-editorUnicodeHighlight-background: rgba(189, 155, 3, 0.15);
--vscode-editorOverviewRuler-bracketMatchForeground: #a0a0a0;
--vscode-editor-linkedEditingBackground: rgba(255, 0, 0, 0.3);
--vscode-editor-wordHighlightBackground: rgba(87, 87, 87, 0.72);
--vscode-editor-wordHighlightStrongBackground: rgba(0, 73, 114, 0.72);
--vscode-editor-wordHighlightTextBackground: rgba(87, 87, 87, 0.72);
--vscode-editorOverviewRuler-wordHighlightForeground: rgba(160, 160, 160, 0.8);
--vscode-editorOverviewRuler-wordHighlightStrongForeground: rgba(192, 160, 192, 0.8);
--vscode-editorOverviewRuler-wordHighlightTextForeground: rgba(160, 160, 160, 0.8);
--vscode-peekViewTitle-background: #252526;
--vscode-peekViewTitleLabel-foreground: #ffffff;
--vscode-peekViewTitleDescription-foreground: rgba(204, 204, 204, 0.7);
--vscode-peekView-border: #3794ff;
--vscode-peekViewResult-background: #252526;
--vscode-peekViewResult-lineForeground: #bbbbbb;
--vscode-peekViewResult-fileForeground: #ffffff;
--vscode-peekViewResult-selectionBackground: rgba(51, 153, 255, 0.2);
--vscode-peekViewResult-selectionForeground: #ffffff;
--vscode-peekViewEditor-background: #001f33;
--vscode-peekViewEditorGutter-background: #001f33;
--vscode-peekViewEditorStickyScroll-background: #001f33;
--vscode-peekViewResult-matchHighlightBackground: rgba(234, 92, 0, 0.3);
--vscode-peekViewEditor-matchHighlightBackground: rgba(255, 143, 0, 0.6);
--vscode-editorMarkerNavigationError-background: #f14c4c;
--vscode-editorMarkerNavigationError-headerBackground: rgba(241, 76, 76, 0.1);
--vscode-editorMarkerNavigationWarning-background: #cca700;
--vscode-editorMarkerNavigationWarning-headerBackground: rgba(204, 167, 0, 0.1);
--vscode-editorMarkerNavigationInfo-background: #3794ff;
--vscode-editorMarkerNavigationInfo-headerBackground: rgba(55, 148, 255, 0.1);
--vscode-editorMarkerNavigation-background: #1e1e1e;
--vscode-editorHoverWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-background: #252526;
--vscode-editorSuggestWidget-border: #454545;
--vscode-editorSuggestWidget-foreground: #d4d4d4;
--vscode-editorSuggestWidget-selectedForeground: #ffffff;
--vscode-editorSuggestWidget-selectedBackground: #04395e;
--vscode-editorSuggestWidget-highlightForeground: #2aaaff;
--vscode-editorSuggestWidget-focusHighlightForeground: #2aaaff;
--vscode-editorSuggestWidgetStatus-foreground: rgba(212, 212, 212, 0.5);
--vscode-editor-foldBackground: rgba(38, 79, 120, 0.3);
--vscode-editorGutter-foldingControlForeground: #c5c5c5; }

.mtk1 { color: #d4d4d4; }
.mtk2 { color: #1e1e1e; }
.mtk3 { color: #cc6666; }
.mtk4 { color: #9cdcfe; }
.mtk5 { color: #ce9178; }
.mtk6 { color: #b5cea8; }
.mtk7 { color: #608b4e; }
.mtk8 { color: #82b76c; }
.mtk9 { color: #569cd6; }
.mtk10 { color: #69a5d7; }
.mtk11 { color: #f28b82; }
.mtk12 { color: #d7ba7d; }
.mtk13 { color: #d49d87; }
.mtk14 { color: #dcdcdc; }
.mtk15 { color: #808080; }
.mtk16 { color: #4ec9b0; }
.mtk17 { color: #dcdcaa; }
.mtk18 { color: #f44747; }
.mtk19 { color: #82c6ff; }
.mtk20 { color: #c99cc6; }
.mtk21 { color: #c586c0; }
.mtk22 { color: #a79873; }
.mtk23 { color: #dd6a6f; }
.mtk24 { color: #5bb498; }
.mtk25 { color: #909090; }
.mtk26 { color: #778899; }
.mtk27 { color: #ff00ff; }
.mtk28 { color: #b46695; }
.mtk29 { color: #ff0000; }
.mtk30 { color: #4f76ac; }
.mtk31 { color: #3dc9b0; }
.mtk32 { color: #74b0df; }
.mtk33 { color: #4864aa; }
.mtki { font-style: italic; }
.mtkb { font-weight: bold; }
.mtku { text-decoration: underline; text-underline-position: under; }
.mtks { text-decoration: line-through; }
.mtks.mtku { text-decoration: underline line-through; text-underline-position: under; }</style></head><body class="" data-new-gr-c-s-check-loaded="14.1249.0" data-gr-ext-installed="" data-new-gr-c-s-loaded="14.1249.0" style="overscroll-behavior: contain;"><div style="visibility: hidden; overflow: hidden; position: absolute; top: 0px; height: 1px; width: auto; padding: 0px; border: 0px; margin: 0px; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal;"><div id="MathJax_Hidden"></div></div><div id="MathJax_Message" style="display: none;"></div><div class="scripts"><script nonce="">window.performance.mark('external_scripts_start');</script><script src="./Orioye.E.project8.ipy_files/gapi_loader.js.download" nonce=""></script><script src="./Orioye.E.project8.ipy_files/socketio_binary.js.download" nonce=""></script><script src="./Orioye.E.project8.ipy_files/analytics_binary.js.download" nonce=""></script><script src="./Orioye.E.project8.ipy_files/MathJax.js.download" nonce=""></script><script src="./Orioye.E.project8.ipy_files/js_monaco_editor_vs_loader.js.download" nonce=""></script><script nonce="">window.performance.mark('external_scripts_end'); window.performance.measure('external_scripts', 'external_scripts_start', 'external_scripts_end'); window.performance.mark('colab_load_start');</script><script src="./Orioye.E.project8.ipy_files/external_binary_l10n__en_gb.js.download" nonce=""></script><script nonce="">
          window.performance.mark('colab_load_end');
          window.performance.measure('colab_load', 'colab_load_start', 'colab_load_end');
        </script></div><colab-snackbar leading="" labeltext="" id="message-area" class="message-area"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar {
          z-index: var(--colab-above-dialog-z-index);
        }

        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$320062509$-->
      <div class="mdc-snackbar  mdc-snackbar--leading ">
        <div class="mdc-snackbar__surface">
          <!--?lit$320062509$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><colab-snackbar leading="" labeltext="" id="message-area-secondary" class="message-area startup"><template shadowrootmode="open"><!----><style>
        :host .mdc-snackbar {
          z-index: var(--colab-above-dialog-z-index);
        }

        :host .mdc-snackbar__surface {
          background-color: var(--colab-inverse-surface-color);
        }

        :host .mdc-snackbar__label {
          color: var(--colab-inverse-on-surface-color);
        }
      </style>
      <!--?lit$320062509$-->
      <div class="mdc-snackbar mdc-snackbar--leading">
        <div class="mdc-snackbar__surface">
          <!--?lit$320062509$-->
          <div class="mdc-snackbar__actions">
            <slot name="action"></slot>
            <slot name="dismiss"></slot>
          </div>
        </div>
      </div><!--?--></template>
      <md-icon-button class="close" slot="dismiss" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
      </md-icon-button>
    </colab-snackbar><div ng-non-bindable=""></div><div class="gb_S" ng-non-bindable=""><div class="gb_Bc"><div>Google Account</div><div class="gb_g">Esther Adenike</div><div>orioyeesther2019@gmail.com</div><div class="gb_Cc"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
var Id;Id=class extends _.rd{};_.Jd=function(a,b){if(b in a.i)return a.i[b];throw new Id;};_.Kd=function(a){return _.Jd(_.od.i(),a)};
}catch(e){_._DumpException(e)}
try{
/*

 Copyright Google LLC
 SPDX-License-Identifier: Apache-2.0
*/
var Nd;_.Ld=function(a){const b=a.length;if(b>0){const c=Array(b);for(let d=0;d<b;d++)c[d]=a[d];return c}return[]};Nd=function(a){return new _.Md(b=>b.substr(0,a.length+1).toLowerCase()===a+":")};_.Od=globalThis.trustedTypes;_.Pd=class{constructor(a){this.i=a}toString(){return this.i}};_.Qd=new _.Pd("about:invalid#zClosurez");_.Md=class{constructor(a){this.Th=a}};_.Rd=[Nd("data"),Nd("http"),Nd("https"),Nd("mailto"),Nd("ftp"),new _.Md(a=>/^[^:]*([/?#]|$)/.test(a))];_.Sd=class{constructor(a){this.i=a}toString(){return this.i+""}};_.Td=new _.Sd(_.Od?_.Od.emptyHTML:"");
}catch(e){_._DumpException(e)}
try{
var Xd,ie,Wd,Yd,ce;_.Ud=function(a){if(a==null)return a;if(typeof a==="string"&&a)a=+a;else if(typeof a!=="number")return;return(0,_.Na)(a)?a|0:void 0};_.Vd=function(a,b){return a.lastIndexOf(b,0)==0};Xd=function(){let a=null;if(!Wd)return a;try{const b=c=>c;a=Wd.createPolicy("ogb-qtm#html",{createHTML:b,createScript:b,createScriptURL:b})}catch(b){}return a};_.Zd=function(){Yd===void 0&&(Yd=Xd());return Yd};_.ae=function(a){const b=_.Zd();a=b?b.createScriptURL(a):a;return new _.$d(a)};
_.be=function(a){if(a instanceof _.$d)return a.i;throw Error("x");};_.de=function(a){if(ce.test(a))return a};_.ee=function(a){if(a instanceof _.Pd)if(a instanceof _.Pd)a=a.i;else throw Error("x");else a=_.de(a);return a};_.fe=function(a,b=document){let c;const d=(c=b.querySelector)==null?void 0:c.call(b,`${a}[nonce]`);return d==null?"":d.nonce||d.getAttribute("nonce")||""};_.S=function(a,b,c){return _.Ma(_.Lc(a,b,c,_.Kc))};_.ge=function(a,b){return _.Ud(_.Lc(a,b,void 0,_.Kc))};
_.he=function(a){var b=_.Ka(a);return b=="array"||b=="object"&&typeof a.length=="number"};Wd=_.Od;_.$d=class{constructor(a){this.i=a}toString(){return this.i+""}};ce=/^\s*(?!javascript:)(?:[\w+.-]+:|[^:/?#]*(?:[/?#]|$))/i;var oe,se,je;_.le=function(a){return a?new je(_.ke(a)):ie||(ie=new je)};_.me=function(a,b){return typeof b==="string"?a.getElementById(b):b};_.T=function(a,b){var c=b||document;c.getElementsByClassName?a=c.getElementsByClassName(a)[0]:(c=document,a=a?(b||c).querySelector(a?"."+a:""):_.ne(c,"*",a,b)[0]||null);return a||null};_.ne=function(a,b,c,d){a=d||a;return(b=b&&b!="*"?String(b).toUpperCase():"")||c?a.querySelectorAll(b+(c?"."+c:"")):a.getElementsByTagName("*")};
_.pe=function(a,b){_.Bb(b,function(c,d){d=="style"?a.style.cssText=c:d=="class"?a.className=c:d=="for"?a.htmlFor=c:oe.hasOwnProperty(d)?a.setAttribute(oe[d],c):_.Vd(d,"aria-")||_.Vd(d,"data-")?a.setAttribute(d,c):a[d]=c})};oe={cellpadding:"cellPadding",cellspacing:"cellSpacing",colspan:"colSpan",frameborder:"frameBorder",height:"height",maxlength:"maxLength",nonce:"nonce",role:"role",rowspan:"rowSpan",type:"type",usemap:"useMap",valign:"vAlign",width:"width"};
_.qe=function(a){return a?a.defaultView:window};_.te=function(a,b){const c=b[1],d=_.re(a,String(b[0]));c&&(typeof c==="string"?d.className=c:Array.isArray(c)?d.className=c.join(" "):_.pe(d,c));b.length>2&&se(a,d,b);return d};se=function(a,b,c){function d(e){e&&b.appendChild(typeof e==="string"?a.createTextNode(e):e)}for(let e=2;e<c.length;e++){const f=c[e];!_.he(f)||_.Lb(f)&&f.nodeType>0?d(f):_.bc(f&&typeof f.length=="number"&&typeof f.item=="function"?_.Ld(f):f,d)}};
_.ue=function(a){return _.re(document,a)};_.re=function(a,b){b=String(b);a.contentType==="application/xhtml+xml"&&(b=b.toLowerCase());return a.createElement(b)};_.ve=function(a){let b;for(;b=a.firstChild;)a.removeChild(b)};_.we=function(a){return a&&a.parentNode?a.parentNode.removeChild(a):null};_.xe=function(a,b){return a&&b?a==b||a.contains(b):!1};_.ke=function(a){return a.nodeType==9?a:a.ownerDocument||a.document};je=function(a){this.i=a||_.t.document||document};_.n=je.prototype;
_.n.H=function(a){return _.me(this.i,a)};_.n.Pa=function(a,b,c){return _.te(this.i,arguments)};_.n.appendChild=function(a,b){a.appendChild(b)};_.n.Je=_.ve;_.n.ng=_.we;_.n.mg=_.xe;
}catch(e){_._DumpException(e)}
try{
_.Mi=function(a){const b=_.fe("script",a.ownerDocument);b&&a.setAttribute("nonce",b)};_.Ni=function(a){if(!a)return null;a=_.I(a,4);var b;a===null||a===void 0?b=null:b=_.ae(a);return b};_.Oi=function(a,b,c){a=a.fa;return _.zb(a,a[_.v]|0,b,c)!==void 0};_.Pi=class extends _.O{constructor(a){super(a)}};_.Qi=function(a,b){return(b||document).getElementsByTagName(String(a))};
}catch(e){_._DumpException(e)}
try{
var Si=function(a,b,c){a<b?Ri(a+1,b):_.Yc.log(Error("W`"+a+"`"+b),{url:c})},Ri=function(a,b){if(Ti){const c=_.ue("SCRIPT");c.async=!0;c.type="text/javascript";c.charset="UTF-8";c.src=_.be(Ti);_.Mi(c);c.onerror=_.Ob(Si,a,b,c.src);_.Qi("HEAD")[0].appendChild(c)}},Ui=class extends _.O{constructor(a){super(a)}};var Vi=_.C(_.id,Ui,17)||new Ui,Wi,Ti=(Wi=_.C(Vi,_.Pi,1))?_.Ni(Wi):null,Xi,Yi=(Xi=_.C(Vi,_.Pi,2))?_.Ni(Xi):null,Zi=function(){Ri(1,2);if(Yi){const a=_.ue("LINK");a.setAttribute("type","text/css");a.href=_.be(Yi).toString();a.rel="stylesheet";let b=_.fe("style",document);b&&a.setAttribute("nonce",b);_.Qi("HEAD")[0].appendChild(a)}};(function(){const a=_.jd();if(_.S(a,18))Zi();else{const b=_.ge(a,19)||0;window.addEventListener("load",()=>{window.setTimeout(Zi,b)})}})();
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script><div style="position: absolute; width: 0px; height: 0px; overflow: hidden; padding: 0px; border: 0px; margin: 0px;"><div id="MathJax_Font_Test" style="position: absolute; visibility: hidden; top: 0px; left: 0px; width: auto; min-width: 0px; max-width: none; padding: 0px; border: 0px; margin: 0px; white-space: nowrap; text-align: left; text-indent: 0px; text-transform: none; line-height: normal; letter-spacing: normal; word-spacing: normal; font-size: 40px; font-weight: normal; font-style: normal; font-size-adjust: none; font-family: MathJax_Size1, monospace;"></div></div><iframe id="hfcr" src="./Orioye.E.project8.ipy_files/RotateCookiesPage.html" style="display: none;"></iframe><div class="notebook-vertical" style="position: relative;">
      <!--?lit$320062509$--><colab-skip-link><template shadowrootmode="open"><!----><md-elevated-button class="link" href="#notebook-main" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$320062509$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="link" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="link" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$320062509$--><a id="link" class="button" href="https://colab.research.google.com/drive/1GxAEOdWL568uMzUjdoXwNV13x4jAU5xu#notebook-main"><!--?lit$320062509$-->
      <span class="touch"></span>
      <!--?lit$320062509$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$320062509$-->
    
    </a>
    </template><!--?lit$320062509$-->Skip to main content</md-elevated-button></template></colab-skip-link>
      <div class="top-floater"><div role="banner">
    <!--?lit$320062509$-->
    <!--?lit$320062509$-->
          <div id="private-outputs-warning" class="header-warning private-outputs-warning" hidden=""><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>info</md-icon>
            <div class="message">
              <!--?lit$320062509$-->This notebook is open with private outputs. Outputs will not be saved. You can disable this in <a href="https://colab.research.google.com/drive/1GxAEOdWL568uMzUjdoXwNV13x4jAU5xu#" id="private-outputs-notebook-info-link" command="notebook-settings" aria-describedby="private-outputs-notebook-info-link-tooltip">Notebook settings</a><colab-tooltip-trigger aria-hidden="true" for="private-outputs-notebook-info-link" id="private-outputs-notebook-info-link-tooltip"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Open notebook settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>.
            </div>
          <div class="actions"><md-icon-button class="close" title="Close" data-aria-label="Close" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Close">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
          <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>close</md-icon>
        </md-icon-button></div></div>
        
    <!--?lit$320062509$--> <!--?lit$320062509$-->

    <div id="header" class="horizontal layout">
      <div id="header-background"><div></div></div>
      <div id="header-content">
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><div id="header-logo">
              <!--?lit$320062509$--> <!--?lit$320062509$--><a href="https://drive.google.com/drive/search?q=owner%3Ame%20(type%3Aapplication%2Fvnd.google.colaboratory%20%7C%7C%20type%3Aapplication%2Fvnd.google.colab)&amp;authuser=0" aria-label="View in Google Drive">
        <!--?lit$320062509$--><md-icon class="colab-large-icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$--><svg viewBox="0 0 24 24"><!--?lit$320062509$-->
      <g id="colab-logo">
        <path d="M4.54,9.46,2.19,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36A3.59,3.59,0,0,1,4.54,9.46Z" style="fill:var(--colab-logo-dark)"></path>
        <path d="M2.19,7.1,4.54,9.46a3.59,3.59,0,0,1,5.08,0l1.71-2.93h0l-.1-.08h0A6.93,6.93,0,0,0,2.19,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M11.34,17.46h0L9.62,14.54a3.59,3.59,0,0,1-5.08,0L2.19,16.9a6.93,6.93,0,0,0,9,.65l.11-.09" style="fill:var(--colab-logo-light)"></path>
        <path d="M12,7.1a6.93,6.93,0,0,0,0,9.79l2.36-2.36a3.59,3.59,0,1,1,5.08-5.08L21.81,7.1A6.93,6.93,0,0,0,12,7.1Z" style="fill:var(--colab-logo-light)"></path>
        <path d="M21.81,7.1,19.46,9.46a3.59,3.59,0,0,1-5.08,5.08L12,16.9A6.93,6.93,0,0,0,21.81,7.1Z" style="fill:var(--colab-logo-dark)"></path>
      </g></svg></md-icon>
      </a><!--?-->
            </div>
        <div id="header-doc-toolbar" class="flex">
          <div id="document-info">
            <!--?lit$320062509$--> <!--?lit$320062509$--><md-icon class="file-location-icon" id="file-type" aria-hidden="true" title="Notebook stored in Google Drive"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->
      <svg viewBox="0 0 192 192">
        <path d="M128.33,122l7.59,26.17l19.89,21.42c0,0,0,0,0,0v0c2.69-1.55,4.98-3.8,6.59-6.59l18.48-32 c1.61-2.78,2.41-5.89,2.41-9l-28.38-5.5L128.33,122z" fill="#EA4335"></path>
        <path d="M123.48,18.41c-2.69-1.55-5.78-2.41-9-2.41H77.53c-3.2,0-6.32,0.88-9,2.41l0,0l7.96,26.81l19.44,20.64 L96,66l0,0l19.58-20.89L123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41C123.48,18.41,123.48,18.41,123.48,18.41z" fill="#188038"></path>
        <path d="M63.67,122l-28.33-6.5L8.72,122c0,3.1,0.8,6.2,2.4,8.99L29.6,163c1.61,2.78,3.9,5.03,6.59,6.59 l19.59-20.18L63.67,122L63.67,122z" fill="#1967D2"></path>
        <path d="M155.47,69l-25.4-44c-1.61-2.79-3.9-5.04-6.59-6.59L96,66l32.33,56h54.95c0-3.11-0.8-6.21-2.41-9 L155.47,69z" fill="#FBBC04"></path><path d="M128.33,122H63.67l-27.48,47.59c2.69,1.55,5.78,2.41,9,2.41h101.61c3.22,0,6.31-0.86,9-2.41L128.33,122z" fill="#4285F4"></path>
        <path d="M96,66L68.53,18.41c-2.69,1.55-4.97,3.79-6.58,6.57l-50.83,88.05c-1.6,2.78-2.4,5.88-2.4,8.97h54.95L96,66 z" fill="#34A853"></path>
      </svg></md-icon>
    <input id="doc-name" class="doc-name" maxlength="259" autocomplete="off" aria-label="Notebook name" command="rename" aria-describedby="doc-name-tooltip" style="width: 176.359px;" data-has-listeners="true"><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events></input><colab-tooltip-trigger aria-hidden="true" for="doc-name" id="doc-name-tooltip"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Rename notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger><colab-input-sizer aria-hidden="true" style="left: -1000%; position: absolute; font-family: &quot;Google Sans&quot;, Roboto, Noto, sans-serif; font-size: 18px; font-weight: 400; letter-spacing: normal; padding-left: 3px; padding-right: 4px; white-space: pre;">Orioye.E.project8.ipy_</colab-input-sizer>
            <!--?lit$320062509$-->
                  <md-icon-button id="star-icon" command="toggle-star" aria-describedby="star-icon-tooltip" data-aria-label="Star" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Star">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface"></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
                    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>star</md-icon>
                  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="star-icon" id="star-icon-tooltip"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Star notebook in Google Drive</div><!----><!--?--></template>
        </colab-tooltip-trigger>
                
            <!--?lit$320062509$--><colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><!--?--></template></colab-last-saved-indicator>
          </div>
        <div class="menubar-wrapper"><div><!----><div id="top-menubar" class="goog-menubar format-lightborder" role="menubar" tabindex="0" style="user-select: none;"><!--?lit$320062509$--><div class="goog-menu-button goog-inline-block" id="file-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$320062509$-->File</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="edit-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$320062509$-->Edit</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="view-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$320062509$-->View</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="insert-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$320062509$-->Insert</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="runtime-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$320062509$-->Runtime</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="tools-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$320062509$-->Tools</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div><div class="goog-menu-button goog-inline-block" id="help-menu-button" role="button" aria-expanded="false" aria-haspopup="true" style="user-select: none;"><div class="goog-inline-block goog-menu-button-outer-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-inner-box" style="user-select: none;"><div class="goog-inline-block goog-menu-button-caption" style="user-select: none;"><!--?lit$320062509$-->Help</div><div class="goog-inline-block goog-menu-button-dropdown" style="user-select: none;">&nbsp;</div></div></div></div></div></div></div></div>
        <div id="header-right">
          <!--?lit$320062509$-->
    <colab-collaborator-bar id="collaborator-bar"><template shadowrootmode="open"><!----> <div class="collaborator-bar">
      <!--?lit$320062509$-->
      <!--?lit$320062509$-->
    </div></template></colab-collaborator-bar>
  
          <!--?lit$320062509$--> <md-icon-button id="comments" command="open-comments-thread" data-aria-label="Open comments pane" aria-describedby="comments-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open comments pane">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="comments" id="comments-tooltip"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Open comments pane</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$320062509$--> <md-icon-button id="settings-cog" command="preferences" data-aria-label="Open settings" aria-describedby="settings-cog-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
                <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
              </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-cog" id="settings-cog-tooltip"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$320062509$--> <md-filled-tonal-button id="share-toolbar-button" command="share" data-aria-label="Share notebook" aria-describedby="share-toolbar-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$320062509$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$320062509$--><button id="button" class="button" aria-label="Share notebook">
      <!--?lit$320062509$-->
      <span class="touch"></span>
      <!--?lit$320062509$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$320062509$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->people</md-icon>
                <!--?lit$320062509$-->Share
              </md-filled-tonal-button><colab-tooltip-trigger aria-hidden="true" for="share-toolbar-button" id="share-toolbar-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <!--?lit$320062509$--> <md-text-button class="show-chat-button" id="show-chat-button" command="toggle-composer" data-aria-label="Toggle Gemini" aria-describedby="show-chat-button-tooltip" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$320062509$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$320062509$--><button id="button" class="button" aria-label="Toggle Gemini">
      <!--?lit$320062509$-->
      <span class="touch"></span>
      <!--?lit$320062509$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$320062509$-->
    
    </button>
    </template>
                <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
                <!--?lit$320062509$-->Gemini
              </md-text-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button" id="show-chat-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Toggle Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
          <div class="header-onegoogle-container"><div class="onegoogle"><div class="gb_Fa gb_Kd gb_4d gb_Xc" id="gb"><div class="gb_Dd gb_1d gb_yd" ng-non-bindable="" data-ogsr-up="" style="padding:0;height:auto;display:block"><div class="gb_Te" style="display:block"><div class="gb_4c"></div><div class="gb_z gb_dd gb_Pf gb_0"><div class="gb_D gb_jb gb_Pf gb_0"><a class="gb_B gb_Za gb_0" aria-expanded="false" aria-label="Google Account: Esther Adenike  
(orioyeesther2019@gmail.com)" href="https://accounts.google.com/SignOutOptions?hl=en-GB&amp;continue=https://colab.research.google.com/drive/1GxAEOdWL568uMzUjdoXwNV13x4jAU5xu&amp;ec=GBRAqQM" tabindex="0" role="button"><span class="gb_Ud"><img class="gb_P gbii" src="./Orioye.E.project8.ipy_files/unnamed.png" srcset="https://lh3.googleusercontent.com/ogw/AF2bZyhVo1ClTsEpyUtsmo01xbPveoCeo-vzEwBuK4Zx-4KDIq4=s32-c-mo 1x, https://lh3.googleusercontent.com/ogw/AF2bZyhVo1ClTsEpyUtsmo01xbPveoCeo-vzEwBuK4Zx-4KDIq4=s64-c-mo 2x " alt="" aria-hidden="true" data-noaft=""></span><div class="gb_Q gb_R" aria-hidden="true"><svg class="gb_Ka" height="14" viewBox="0 0 14 14" width="14" xmlns="http://www.w3.org/2000/svg"><circle class="gb_La" cx="7" cy="7" r="7"></circle><path class="gb_Na" d="M6 10H8V12H6V10ZM6 2H8V8H6V2Z"></path></svg></div></a></div></div></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 436px; z-index: 991; height: 0px; margin-top: 57px; right: 0px; margin-right: 4px;"></div><div style="overflow: hidden; position: absolute; top: 0px; visibility: hidden; width: 420px; z-index: 991; height: 280px; margin-top: 70px; right: 0px; margin-right: 25px;"></div></div></div><script nonce="">this.gbar_=this.gbar_||{};(function(_){var window=this;
try{
_.Ed=function(a,b,c){if(!a.j)if(c instanceof Array)for(var d of c)_.Ed(a,b,d);else{d=(0,_.z)(a.C,a,b);const e=a.v+c;a.v++;b.dataset.eqid=e;a.B[e]=d;b&&b.addEventListener?b.addEventListener(c,d,!1):b&&b.attachEvent?b.attachEvent("on"+c,d):a.o.log(Error("t`"+b))}};
}catch(e){_._DumpException(e)}
try{
var Fd=document.querySelector(".gb_J .gb_B"),Gd=document.querySelector("#gb.gb_Tc");Fd&&!Gd&&_.Ed(_.nd,Fd,"click");
}catch(e){_._DumpException(e)}
try{
_.mh=function(a){if(a.v)return a.v;for(const b in a.i)if(a.i[b].ha()&&a.i[b].B())return a.i[b];return null};_.nh=function(a,b){a.i[b.J()]=b};var oh=new class extends _.P{constructor(){var a=_.Yc;super();this.B=a;this.v=null;this.o={};this.C={};this.i={};this.j=null}A(a){this.i[a]&&(_.mh(this)&&_.mh(this).J()==a||this.i[a].P(!0))}Ra(a){this.j=a;for(const b in this.i)this.i[b].ha()&&this.i[b].Ra(a)}kc(a){return a in this.i?this.i[a]:null}};_.qd("dd",oh);
}catch(e){_._DumpException(e)}
try{
_.Fi=function(a,b){return _.J(a,36,b)};
}catch(e){_._DumpException(e)}
try{
var Gi=document.querySelector(".gb_z .gb_B"),Hi=document.querySelector("#gb.gb_Tc");Gi&&!Hi&&_.Ed(_.nd,Gi,"click");
}catch(e){_._DumpException(e)}
})(this.gbar_);
// Google Inc.
</script></div></div>
        </div>
      </div>
    </div>
  </div></div><colab-notebook-toolbar id="top-toolbar" class="horizontal layout center noshrink"><!----> <!--?lit$320062509$-->
    <!--?lit$320062509$--> <colab-toolbar-button icon="search" id="toolbar-show-command-palette" command="show-command-palette"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$320062509$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$320062509$--><button id="button" class="button">
      <!--?lit$320062509$-->
      <span class="touch"></span>
      <!--?lit$320062509$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$320062509$-->
    
    </button>
    </template>
        <!--?lit$320062509$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->search</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$320062509$--><span class="screenreader-only"><!--?lit$320062509$-->Show command palette <!--?lit$320062509$-->Ctrl+Shift+P</span>
      </md-text-button>
      <!--?lit$320062509$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Show command palette" shortcut="Ctrl+Shift+P"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Show command palette (Ctrl+Shift+P)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$320062509$-->Commands
          </colab-toolbar-button>
          <span class="colab-separator"></span>
    <!--?lit$320062509$-->
          <colab-toolbar-button command="insert-cell-below" icon="add" id="toolbar-add-code"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$320062509$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$320062509$--><button id="button" class="button">
      <!--?lit$320062509$-->
      <span class="touch"></span>
      <!--?lit$320062509$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$320062509$-->
    
    </button>
    </template>
        <!--?lit$320062509$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$320062509$--><span class="screenreader-only"><!--?lit$320062509$-->Insert code cell below <!--?lit$320062509$-->Ctrl+M B</span>
      </md-text-button>
      <!--?lit$320062509$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Insert code cell below" shortcut="Ctrl+M B"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Insert code cell below (Ctrl+M B)</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$320062509$-->Code
          </colab-toolbar-button>
          <!--?lit$320062509$-->
          <colab-toolbar-button command="add-text" icon="add" id="toolbar-add-text"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$320062509$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$320062509$--><button id="button" class="button">
      <!--?lit$320062509$-->
      <span class="touch"></span>
      <!--?lit$320062509$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$320062509$-->
    
    </button>
    </template>
        <!--?lit$320062509$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->add</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$320062509$--><span class="screenreader-only"><!--?lit$320062509$-->Add text cell <!--?lit$320062509$--></span>
      </md-text-button>
      <!--?lit$320062509$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="tooltip" message="Add text cell" shortcut=""><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Add text cell</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
            <!--?lit$320062509$-->Text
          </colab-toolbar-button>
        
    <span class="colab-separator"></span>
    <colab-notebook-toolbar-run-button><template shadowrootmode="open"><!----><colab-toolbar-button icon="play_arrow" tooltipid="toolbar-run-button-tooltip" id="toolbar-run-button" tooltiptext="Run all cells in notebook"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$320062509$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$320062509$--><button id="button" class="button">
      <!--?lit$320062509$-->
      <span class="touch"></span>
      <!--?lit$320062509$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$320062509$-->
    
    </button>
    </template>
        <!--?lit$320062509$--><md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->play_arrow</md-icon>
        <span class="button-content"><slot></slot></span>
        <!--?lit$320062509$--><span class="screenreader-only"><!--?lit$320062509$-->Run all cells in notebook <!--?lit$320062509$--></span>
      </md-text-button>
      <!--?lit$320062509$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="toolbar-run-button-tooltip" message="Run all cells in notebook" shortcut=""><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Run all cells in notebook</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$320062509$-->Run all
      </colab-toolbar-button>
      <!--?lit$320062509$--><md-icon-button data-aria-haspopup="menu" data-aria-expanded="false" id="toolbar-run-button-more-actions" data-aria-label="More actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toolbar-run-button-more-actions" message="More actions"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->More actions</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$320062509$--><md-menu positioning="popover" quick="" aria-labelledby="toolbar-run-button-more-actions" anchor="toolbar-run-button-more-actions" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$320062509$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$320062509$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$320062509$--><!----><md-menu-item command="restart" disabled="" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="-1" role="menuitem" class="list-item  disabled "><!--?lit$320062509$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$320062509$--> <md-ripple part="ripple" for="item" disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$320062509$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$320062509$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$320062509$-->Restart session</span>
  </md-menu-item><!----><!----><md-menu-item command="restart-and-run-all" disabled="" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="-1" role="menuitem" class="list-item  disabled "><!--?lit$320062509$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$320062509$--> <md-ripple part="ripple" for="item" disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$320062509$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$320062509$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$320062509$-->Restart session and run all</span>
  </md-menu-item><!----><!----><md-divider><template shadowrootmode="open"><!----></template></md-divider><!----><!----><md-menu-item command="interrupt" disabled="" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="-1" role="menuitem" class="list-item  disabled "><!--?lit$320062509$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$320062509$--> <md-ripple part="ripple" for="item" disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$320062509$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$320062509$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$320062509$-->Interrupt execution</span>
  </md-menu-item><!----><!----><md-menu-item command="clear-outputs" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$320062509$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$320062509$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$320062509$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$320062509$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$320062509$-->Clear all outputs</span>
  </md-menu-item><!---->
  </md-menu><!--?--><!--?--></template>
    </colab-notebook-toolbar-run-button>
    <!--?lit$320062509$-->
    <!--?lit$320062509$-->
    <!--?lit$320062509$-->
    <!--?lit$320062509$-->
    <!--?lit$320062509$--> <span class="collapsed-options">
          <colab-last-saved-indicator aria-live="polite" aria-atomic="true"><template shadowrootmode="open"><!----><!--?--></template></colab-last-saved-indicator>
        </span>

    <span class="flex"></span>

    <!--?lit$320062509$--><colab-connect-warning-button><template shadowrootmode="open"><!----><!--?lit$320062509$--><!--?--><!--?--></template></colab-connect-warning-button>
    <!--?lit$320062509$--><!--?lit$320062509$--><colab-connect-button><template shadowrootmode="open"><!----> <!--?lit$320062509$--> <!--?lit$320062509$--><!--?-->
      <colab-toolbar-button id="connect" tooltipid="colab-connect-tooltip" tooltiptext="Connect to a new runtime"><template shadowrootmode="open"><!----><md-text-button id="button" data-aria-disabled="false" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$320062509$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$320062509$--><button id="button" class="button">
      <!--?lit$320062509$-->
      <span class="touch"></span>
      <!--?lit$320062509$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$320062509$-->
    
    </button>
    </template>
        <!--?lit$320062509$-->
        <span class="button-content"><slot></slot></span>
        <!--?lit$320062509$--><span class="screenreader-only"><!--?lit$320062509$-->Connect to a new runtime <!--?lit$320062509$--></span>
      </md-text-button>
      <!--?lit$320062509$--> <colab-tooltip-trigger for="button" aria-hidden="true" id="colab-connect-tooltip" message="Connect to a new runtime" shortcut=""><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Connect to a new runtime</div><!----><!--?--></template>
          </colab-tooltip-trigger><!--?--></template>
        <!--?lit$320062509$-->Connect
      </colab-toolbar-button>
      <!--?lit$320062509$--> <md-icon-button id="connect-dropdown" data-aria-expanded="false" data-aria-haspopup="menu" data-aria-label="Additional connection options" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Additional connection options" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>arrow_drop_down</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger for="connect-dropdown" id="connect-dropdown-tooltip" aria-hidden="true" message="Additional connection options"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Additional connection options</div><!----><!--?--></template>
      </colab-tooltip-trigger>
      <!--?lit$320062509$--><!--?--></template></colab-connect-button><!--?-->
    <!--?lit$320062509$-->
    <span class="collapsed-options">
      <!--?lit$320062509$--><span class="colab-separator"></span>
      <!--?lit$320062509$--> <md-icon-button id="share-button-toolbar" command="share" data-aria-label="Share notebook" aria-describedby="share-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Share notebook">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
            <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->people</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="share-button-toolbar" id="share-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Share notebook</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <md-icon-button id="settings-button-toolbar" command="preferences" data-aria-label="Open settings" aria-describedby="settings-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open settings">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>settings</md-icon>
      </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="settings-button-toolbar" id="settings-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Open settings</div><!----><!--?--></template>
        </colab-tooltip-trigger>
      <!--?lit$320062509$--> <md-icon-button class="show-chat-button" id="show-chat-button-toolbar" command="toggle-composer" data-aria-label="Toggle Gemini" aria-describedby="show-chat-button-toolbar-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle Gemini">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
            <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
          </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="show-chat-button-toolbar" id="show-chat-button-toolbar-tooltip"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Toggle Gemini</div><!----><!--?--></template>
        </colab-tooltip-trigger>
    </span>
    <span class="colab-separator"></span>
    <!--?lit$320062509$--><md-icon-button toggle="" command="toggle-header" id="toggle-header-button" data-aria-label="Toggle header visibility" aria-describedby="toggle-header-button-tooltip" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle header visibility" aria-pressed="false">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_less</md-icon>
    <md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>expand_more</md-icon>
  </md-icon-button><colab-tooltip-trigger aria-hidden="true" for="toggle-header-button" id="toggle-header-button-tooltip"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Toggle header visibility</div><!----><!--?--></template>
        </colab-tooltip-trigger><!--?--></colab-notebook-toolbar><div class="notebook-horizontal">
        <!--?lit$320062509$--><colab-left-pane role="complementary" aria-label="left pane"><!----><div class="colab-left-pane-nib layout vertical" role="toolbar" aria-orientation="vertical">
        <div class="left-pane-top"><!----><div class="left-pane-button">
        <!--?lit$320062509$--><md-icon-button toggle="" command="show-toc-pane" data-aria-label="Table of contents" title="Table of contents" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Table of contents" aria-pressed="false">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->format_list_bulleted</md-icon>
    </md-icon-button> <!--?lit$320062509$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$320062509$--><md-icon-button toggle="" command="find" data-aria-label="Find and replace" title="Find and replace" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Find and replace" aria-pressed="false">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->find_in_page</md-icon>
    </md-icon-button> <!--?lit$320062509$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$320062509$--><md-icon-button toggle="" command="snippets" data-aria-label="Code snippets" title="Code snippets" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code snippets" aria-pressed="false">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->code</md-icon>
    </md-icon-button> <!--?lit$320062509$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$320062509$--><md-icon-button toggle="" command="open-user-secrets" data-aria-label="Secrets" title="Secrets" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Secrets" aria-pressed="false">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->vpn_key</md-icon>
    </md-icon-button> <!--?lit$320062509$-->
      </div><!----><div class="left-pane-button">
        <!--?lit$320062509$--><md-icon-button toggle="" command="show-files" data-aria-label="Files" title="Files" tabindex="-1" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Files" aria-pressed="false">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->folder</md-icon>
    </md-icon-button> <!--?lit$320062509$-->
      </div></div>
      </div></colab-left-pane>
        <div class="layout vertical grow">
          <colab-tab-layout-container class="layout horizontal grow flexible-tabs"><!----> <div class="layout horizontal tab-pane-parent">
      <!--?lit$320062509$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$320062509$--><colab-tab-pane class="layout vertical grow no-header focused" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template><md-primary-tab noink="" title="" aria-labelledby="tab-title-Ev53ypMrJtLa" class="selected-tab" tabindex="0" md-tab="" active=""><template shadowrootmode="open"><!----><div class="button" role="presentation">
      <md-focus-ring part="focus-ring" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
      <md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <div role="presentation" class="content  has-label stacked ">
        <slot name="icon"></slot>
        <slot></slot>
        <!--?lit$320062509$--><div class="indicator"></div>
      </div>
      <!--?lit$320062509$-->
    </div></template>
          <div class="colab-tab-header">
            <span class="colab-tab-title" id="tab-title-Ev53ypMrJtLa"><!--?lit$320062509$--><!--?lit$320062509$-->Notebook<!--?--></span>
            <!--?lit$320062509$-->
          </div>
        </md-primary-tab></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$320062509$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> <colab-tab class="layout vertical grow notebook-tab-content selected-tab"><!----> <div class="overflow-flexbox-workaround">
      <colab-shaded-scroller ignore-dom-changes="" tabindex="-1" role="main" id="notebook-main" class="notebook-container" aria-label="Notebook">
        <div class="notebook-scrolling-horizontal-container">
          <div class="notebook-scrolling-horizontal">
            <div class="notebook-content-background">
              <!--?lit$320062509$-->
              <div class="notebook-content ">
                <!--?lit$320062509$--><div class="add-cell">
      <div class="add-cell-buttons">
        <md-outlined-button class="add-code add-button" data-aria-label="Add code cell
Ctrl+M B" title="Add code cell
Ctrl+M B" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$320062509$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$320062509$--><button id="button" class="button" aria-label="Add code cell
Ctrl+M B">
      <!--?lit$320062509$-->
      <span class="touch"></span>
      <!--?lit$320062509$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$320062509$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$320062509$-->Code
        </md-outlined-button>
        <md-outlined-button class="add-text add-button" data-aria-label="Add text cell" title="Add text cell" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$320062509$--><div class="outline"></div>
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$320062509$--><button id="button" class="button" aria-label="Add text cell">
      <!--?lit$320062509$-->
      <span class="touch"></span>
      <!--?lit$320062509$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$320062509$-->
    
    </button>
    </template>
          <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>add</md-icon>
          <!--?lit$320062509$-->Text
        </md-outlined-button>
        <!--?lit$320062509$-->
        <!--?lit$320062509$-->
      </div><hr>
    </div>
                <div class="notebook-cell-list"><div class="cell code code-has-output focused" id="cell-7NBggSsfbI_Q" tabindex="-1" role="region" aria-label="Cell 0: Code cell: " style=""><div class="cell-tag-editor sticky"></div><div class="agent-focus-label">
      <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      <!--?lit$320062509$-->Gemini
    </div><div class="cell-toolbar sticky"><colab-cell-toolbar><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-up-tooltip" data-aria-label="Move cell up
Ctrl+M K" command="move-cell-up" id="button-move-cell-up" soft-disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell up
Ctrl+M K" aria-disabled="true">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->arrow_upward</md-icon>
        <!--?lit$320062509$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-up" id="button-move-cell-up-tooltip" message="Move cell up
Ctrl+M K"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Move cell up</div><!----><!----><div><!--?lit$320062509$-->Ctrl+M K</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-move-cell-down-tooltip" data-aria-label="Move cell down
Ctrl+M J" command="move-cell-down" id="button-move-cell-down" soft-disabled="" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Move cell down
Ctrl+M J" aria-disabled="true">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple disabled="" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->arrow_downward</md-icon>
        <!--?lit$320062509$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-move-cell-down" id="button-move-cell-down-tooltip" message="Move cell down
Ctrl+M J"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Move cell down</div><!----><!----><div><!--?lit$320062509$-->Ctrl+M J</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----><!--?lit$320062509$--><md-menu positioning="popover" quick="" aria-labelledby="ai-menu-anchor-7NBggSsfbI_Q" anchor="ai-menu-anchor-7NBggSsfbI_Q" aria-hidden="true"><template shadowrootmode="open"><!---->
      <div class="menu   " popover="manual" style="display: none;">
        <!--?lit$320062509$--><md-elevation part="elevation" aria-hidden="true"><template shadowrootmode="open"><!----><span class="shadow"></span></template></md-elevation>
        <div class="items">
          <div class="item-padding"> <!--?lit$320062509$--><slot></slot> </div>
        </div>
      </div>
    </template>
    <!--?lit$320062509$--><!----><md-menu-item command="generate-code" md-menu-item="" tabindex="0"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$320062509$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$320062509$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$320062509$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$320062509$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$320062509$-->Generate code</span>
  </md-menu-item><!----><!----><md-menu-item command="explain-cell" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$320062509$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$320062509$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$320062509$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$320062509$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$320062509$-->Explain code</span>
  </md-menu-item><!----><!----><md-menu-item command="transform-code" md-menu-item="" tabindex="-1"><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <li id="item" tabindex="0" role="menuitem" class="list-item   "><!--?lit$320062509$-->
      <md-item><template shadowrootmode="open"><!---->
      <slot name="container"></slot>
      <slot class="non-text" name="start"></slot>
      <div class="text">
        <slot name="overline"></slot>
        <slot class="default-slot"></slot>
        <slot name="headline"></slot>
        <slot name="supporting-text"></slot>
      </div>
      <slot class="non-text" name="trailing-supporting-text"></slot>
      <slot class="non-text" name="end"></slot>
    </template>
        <div slot="container">
          <!--?lit$320062509$--> <md-ripple part="ripple" for="item" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple> <!--?lit$320062509$--> <md-focus-ring part="focus-ring" for="item" inward="" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        </div>
        <slot name="start" slot="start"></slot>
        <slot name="end" slot="end"></slot>
        <!--?lit$320062509$-->
      <slot></slot>
      <slot name="overline" slot="overline"></slot>
      <slot name="headline" slot="headline"></slot>
      <slot name="supporting-text" slot="supporting-text"></slot>
      <slot name="trailing-supporting-text" slot="trailing-supporting-text"></slot>
    
      </md-item>
    </li>
    </template>
    <span slot="headline"><!--?lit$320062509$-->Transform code</span>
  </md-menu-item><!---->
  </md-menu>
          <md-icon-button touch-target="none" data-aria-haspopup="menu" data-aria-expanded="false" aria-describedby="ai-menu-anchor-7NBggSsfbI_Q-tooltip" data-aria-label="Available AI features" id="ai-menu-anchor-7NBggSsfbI_Q" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Available AI features" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
          </md-icon-button>
          <colab-tooltip-trigger aria-hidden="true" for="ai-menu-anchor-7NBggSsfbI_Q" id="ai-menu-anchor-7NBggSsfbI_Q-tooltip" message="Available AI features"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Available AI features</div><!----><!--?--></template>
          </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-copy-link-to-cell-tooltip" data-aria-label="Copy link to cell" command="copy-link-to-cell" id="button-copy-link-to-cell" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Copy link to cell">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->link</md-icon>
        <!--?lit$320062509$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-copy-link-to-cell" id="button-copy-link-to-cell-tooltip" message="Copy link to cell"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Copy link to cell</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-add-comment-tooltip" data-aria-label="Add a comment
Ctrl+Alt+M" command="add-comment" id="button-add-comment" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Add a comment
Ctrl+Alt+M">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->comment</md-icon>
        <!--?lit$320062509$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-add-comment" id="button-add-comment-tooltip" message="Add a comment
Ctrl+Alt+M"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Add a comment</div><!----><!----><div><!--?lit$320062509$-->Ctrl+Alt+M</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-editor-preferences-tooltip" data-aria-label="Open editor settings" command="editor-preferences" id="button-editor-preferences" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Open editor settings">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
        <md-icon filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->settings</md-icon>
        <!--?lit$320062509$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-editor-preferences" id="button-editor-preferences-tooltip" message="Open editor settings"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Open editor settings</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-toggle-edit-markdown-tooltip" data-aria-label="Edit" command="toggle-edit-markdown" id="button-toggle-edit-markdown" toggle="" style="display: none;" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Edit" aria-pressed="false">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->edit</md-icon>
        <!--?lit$320062509$--><md-icon slot="selected" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->edit_off</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-toggle-edit-markdown" id="button-toggle-edit-markdown-tooltip" message="Edit"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Edit</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-mirror-cell-in-tab-tooltip" data-aria-label="Mirror cell in tab" command="mirror-cell-in-tab" id="button-mirror-cell-in-tab" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Mirror cell in tab">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$--><svg viewBox="0 0 24 24"><!--?lit$320062509$-->
      <g id="mirror-cell">
        <path d="M4,21V7H2V21a2,2,0,0,0,2,2H18V21Z"></path>
        <path d="M6,13v2H8.6L5,18.6,6.4,20,10,16.4V19h2V13Z"></path>
        <path d="M19,1H8A2,2,0,0,0,6,3v8H8V3H19V17H14v2h5a2,2,0,0,0,2-2V3A2,2,0,0,0,19,1Z"></path>
      </g></svg></md-icon>
        <!--?lit$320062509$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-mirror-cell-in-tab" id="button-mirror-cell-in-tab-tooltip" message="Mirror cell in tab"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Mirror cell in tab</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!----> <md-icon-button touch-target="none" aria-describedby="button-delete-cell-or-selection-tooltip" data-aria-label="Delete cell
Ctrl+M D" command="delete-cell-or-selection" id="button-delete-cell-or-selection" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Delete cell
Ctrl+M D">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->delete</md-icon>
        <!--?lit$320062509$-->
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-delete-cell-or-selection" id="button-delete-cell-or-selection-tooltip" message="Delete cell
Ctrl+M D"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Delete cell</div><!----><!----><div><!--?lit$320062509$-->Ctrl+M D</div><!----><!--?--></template>
      </colab-tooltip-trigger><!----><!--?lit$320062509$--><md-icon-button touch-target="none" data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-more-actions-tooltip" data-aria-label="More cell actions" class="cell-toolbar-more" id="button-more-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More cell actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_vert</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="button-more-actions" id="button-more-actions-tooltip" message="More cell actions"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->More cell actions</div><!----><!--?--></template>
      </colab-tooltip-trigger><!--?--></template></colab-cell-toolbar></div><div class="main-content" elevation="2"><div class="cell-contents"><div class="cell-mask"></div><span class="imported-info-area"></span><div class="codecell-input-output">
      <div class="inputarea horizontal layout code">
        <div class="cell-gutter">
          <!-- Bounding range for vertical scrolling of icons -->
          <div class="cell-execution-container">
            <colab-run-button><template shadowrootmode="open"><!----> <div class="cell-execution focused stale">
      <button id="run-button" aria-describedby="run-button-tooltip" aria-label="Run cell" aria-disabled="false">
        <!--?lit$320062509$--><span class="execution-count"><!--?lit$320062509$-->[ ]</span>
        <span aria-hidden="true" class="cell-execution-indicator"><!--?lit$320062509$-->
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24">
  <!--?lit$320062509$-->
  <mask id="playSymbolMask">
    <rect width="100%" height="100%" fill="white"></rect>
    <polygon points="10,8 17,12 10,16" fill="black"></polygon>
  </mask>
  <circle cx="12" cy="12" r="7.8" mask="url(#playSymbolMask)" id="filledCircle"></circle>
</svg></span>
      </button>
      <!--?lit$320062509$--><colab-tooltip-trigger for="run-button" id="run-button-tooltip" aria-hidden="true" message="Run cell (Ctrl+Enter)
cell has not been executed in this session

executed by Esther Adenike
Thursday, 19 June 2025
executed in 42.422 s"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Run cell (Ctrl+Enter)</div><!----><!----><div><!--?lit$320062509$-->cell has not been executed in this session</div><!----><!----><br><!----><!----><div><!--?lit$320062509$-->executed by Esther Adenike</div><!----><!----><div><!--?lit$320062509$-->Thursday, 19 June 2025</div><!----><!----><div><!--?lit$320062509$-->executed in 42.422 s</div><!----><!--?--></template>
    </colab-tooltip-trigger>
      <!--?lit$320062509$--><!--?-->
    </div></template></colab-run-button>
          </div>
        </div>
      <div class="editor flex lazy-editor" style=""><div class="editor flex monaco" data-keybinding-context="1" data-mode-id="notebook-python" style="height: 637px; --vscode-editorCodeLens-lineHeight: 16px; --vscode-editorCodeLens-fontSize: 12px; --vscode-editorCodeLens-fontFeatureSettings: &quot;liga&quot; off, &quot;calt&quot; off;"><div class="monaco-editor no-user-select  showUnused showDeprecated vs-dark" role="code" data-uri="inmemory://model/3" style="width: 1794px; height: 637px;"><div data-mprt="3" class="overflow-guard" style="width: 1794px; height: 637px; overflow: clip;"><div class="margin" role="presentation" aria-hidden="true" style="position: absolute; contain: strict; will-change: unset; top: 0px; height: 637px; width: 6px;"><div class="glyph-margin" style="left: 0px; width: 0px; height: 637px;"></div><div class="margin-view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="margin-view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 6px; height: 637px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line current-line-margin-both" style="width:6px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"></div><div style="position:absolute;top:418px;width:100%;height:19px;"></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div><div style="position:absolute;top:532px;width:100%;height:19px;"></div><div style="position:absolute;top:551px;width:100%;height:19px;"></div><div style="position:absolute;top:570px;width:100%;height:19px;"></div><div style="position:absolute;top:589px;width:100%;height:19px;"></div><div style="position:absolute;top:608px;width:100%;height:19px;"></div></div><div class="glyph-margin-widgets" style="position: absolute; top: 0px;"></div></div><div class="monaco-scrollable-element editor-scrollable vs-dark" role="presentation" data-mprt="5" style="position: absolute; overflow: hidden; left: 6px; width: 1788px; height: 637px;"><div class="lines-content monaco-editor-background" style="position: absolute; overflow: hidden; width: 1e+06px; height: 637px; contain: strict; will-change: unset; top: 0px; left: 0px;"><div class="view-overlays" role="presentation" aria-hidden="true" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; height: 0px; width: 1788px;"><div style="position:absolute;top:0px;width:100%;height:19px;"><div class="current-line" style="width:1788px; height:19px;"></div></div><div style="position:absolute;top:19px;width:100%;height:19px;"></div><div style="position:absolute;top:38px;width:100%;height:19px;"></div><div style="position:absolute;top:57px;width:100%;height:19px;"></div><div style="position:absolute;top:76px;width:100%;height:19px;"></div><div style="position:absolute;top:95px;width:100%;height:19px;"></div><div style="position:absolute;top:114px;width:100%;height:19px;"></div><div style="position:absolute;top:133px;width:100%;height:19px;"></div><div style="position:absolute;top:152px;width:100%;height:19px;"></div><div style="position:absolute;top:171px;width:100%;height:19px;"></div><div style="position:absolute;top:190px;width:100%;height:19px;"></div><div style="position:absolute;top:209px;width:100%;height:19px;"></div><div style="position:absolute;top:228px;width:100%;height:19px;"></div><div style="position:absolute;top:247px;width:100%;height:19px;"></div><div style="position:absolute;top:266px;width:100%;height:19px;"></div><div style="position:absolute;top:285px;width:100%;height:19px;"></div><div style="position:absolute;top:304px;width:100%;height:19px;"></div><div style="position:absolute;top:323px;width:100%;height:19px;"></div><div style="position:absolute;top:342px;width:100%;height:19px;"></div><div style="position:absolute;top:361px;width:100%;height:19px;"></div><div style="position:absolute;top:380px;width:100%;height:19px;"></div><div style="position:absolute;top:399px;width:100%;height:19px;"></div><div style="position:absolute;top:418px;width:100%;height:19px;"></div><div style="position:absolute;top:437px;width:100%;height:19px;"></div><div style="position:absolute;top:456px;width:100%;height:19px;"></div><div style="position:absolute;top:475px;width:100%;height:19px;"></div><div style="position:absolute;top:494px;width:100%;height:19px;"></div><div style="position:absolute;top:513px;width:100%;height:19px;"></div><div style="position:absolute;top:532px;width:100%;height:19px;"></div><div style="position:absolute;top:551px;width:100%;height:19px;"></div><div style="position:absolute;top:570px;width:100%;height:19px;"></div><div style="position:absolute;top:589px;width:100%;height:19px;"></div><div style="position:absolute;top:608px;width:100%;height:19px;"></div></div><div role="presentation" aria-hidden="true" class="view-rulers"><div class="view-ruler" style="width: 2px; height: 637px; left: 615.938px;"></div></div><div class="view-zones" role="presentation" aria-hidden="true" style="position: absolute;"></div><div class="view-lines monaco-mouse-cursor-text" role="presentation" aria-hidden="true" data-mprt="7" style="position: absolute; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; width: 1788px; height: 637px;"><div style="top:0px;height:19px;" class="view-line"><span><span class="mtk20">import</span><span class="mtk1">&nbsp;random</span></span></div><div style="top:19px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:38px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Options</span></span></div><div style="top:57px;height:19px;" class="view-line"><span><span class="mtk1">choices&nbsp;=&nbsp;</span><span class="mtk14 bracket-highlighting-0">[</span><span class="mtk5">"rock"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"paper"</span><span class="mtk14">,</span><span class="mtk1">&nbsp;</span><span class="mtk5">"scissors"</span><span class="mtk14 bracket-highlighting-0">]</span></span></div><div style="top:76px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:95px;height:19px;" class="view-line"><span><span class="mtk8">#&nbsp;Game&nbsp;loop</span></span></div><div style="top:114px;height:19px;" class="view-line"><span><span class="mtk20">while</span><span class="mtk1">&nbsp;</span><span class="mtk9">True</span><span class="mtk14">:</span></span></div><div style="top:133px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"\n---&nbsp;Rock,&nbsp;Paper,&nbsp;Scissors&nbsp;---"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:152px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;user_choice&nbsp;=&nbsp;</span><span class="mtk17">input</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Enter&nbsp;your&nbsp;choice&nbsp;(rock,&nbsp;paper,&nbsp;scissors)&nbsp;or&nbsp;'qui</span><span class="mtk5">t'&nbsp;to&nbsp;exit:&nbsp;"</span><span class="mtk14 bracket-highlighting-0">)</span><span class="mtk1">.lower</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:171px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:190px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">if</span><span class="mtk1">&nbsp;user_choice&nbsp;==&nbsp;</span><span class="mtk5">"quit"</span><span class="mtk14">:</span></span></div><div style="top:209px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Thanks&nbsp;for&nbsp;playing!"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:228px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">break</span></span></div><div style="top:247px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:266px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">if</span><span class="mtk1">&nbsp;user_choice&nbsp;</span><span class="mtk19">not</span><span class="mtk1">&nbsp;</span><span class="mtk19">in</span><span class="mtk1">&nbsp;choices</span><span class="mtk14">:</span></span></div><div style="top:285px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"Invalid&nbsp;choice.&nbsp;Please&nbsp;try&nbsp;again."</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:304px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">continue</span></span></div><div style="top:323px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:342px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;computer_choice&nbsp;=&nbsp;random.choice</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk1">choices</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:361px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk10">f</span><span class="mtk5">"Computer&nbsp;chose:&nbsp;</span><span class="mtk14 bracket-highlighting-1">{</span><span class="mtk1">computer_choice</span><span class="mtk14 bracket-highlighting-1">}</span><span class="mtk5">"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:380px;height:19px;" class="view-line"><span><span></span></span></div><div style="top:399px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk8">#&nbsp;Determine&nbsp;winner</span></span></div><div style="top:418px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">if</span><span class="mtk1">&nbsp;user_choice&nbsp;==&nbsp;computer_choice</span><span class="mtk14">:</span></span></div><div style="top:437px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"It's&nbsp;a&nbsp;tie!"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:456px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">elif</span><span class="mtk1">&nbsp;</span><span class="mtk14 bracket-highlighting-0">(</span></span></div><div style="top:475px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk1">user_choice&nbsp;==&nbsp;</span><span class="mtk5">"rock"</span><span class="mtk1">&nbsp;</span><span class="mtk19">and</span><span class="mtk1">&nbsp;computer_choice&nbsp;==&nbsp;</span><span class="mtk5">"scissors"</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk1">&nbsp;</span><span class="mtk19">or</span></span></div><div style="top:494px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk1">user_choice&nbsp;==&nbsp;</span><span class="mtk5">"paper"</span><span class="mtk1">&nbsp;</span><span class="mtk19">and</span><span class="mtk1">&nbsp;computer_choice&nbsp;==&nbsp;</span><span class="mtk5">"rock"</span><span class="mtk14 bracket-highlighting-1">)</span><span class="mtk1">&nbsp;</span><span class="mtk19">or</span></span></div><div style="top:513px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk14 bracket-highlighting-1">(</span><span class="mtk1">user_choice&nbsp;==&nbsp;</span><span class="mtk5">"scissors"</span><span class="mtk1">&nbsp;</span><span class="mtk19">and</span><span class="mtk1">&nbsp;computer_choice&nbsp;==&nbsp;</span><span class="mtk5">"paper"</span><span class="mtk14 bracket-highlighting-1">)</span></span></div><div style="top:532px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk14 bracket-highlighting-0">)</span><span class="mtk14">:</span></span></div><div style="top:551px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"You&nbsp;win!"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:570px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk20">else</span><span class="mtk14">:</span></span></div><div style="top:589px;height:19px;" class="view-line"><span><span class="mtk1">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span><span class="mtk17">print</span><span class="mtk14 bracket-highlighting-0">(</span><span class="mtk5">"You&nbsp;lose!"</span><span class="mtk14 bracket-highlighting-0">)</span></span></div><div style="top:608px;height:19px;" class="view-line"><span><span></span></span></div></div><div data-mprt="1" class="contentWidgets" style="position: absolute; top: 0px;"></div><div role="presentation" aria-hidden="true" class="cursors-layer cursor-line-style cursor-solid"><div class="cursor monaco-mouse-cursor-text " style="height: 19px; top: 0px; left: 0px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; display: block; visibility: hidden; padding-left: 0px; width: 2px;"></div></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute; width: 1774px; height: 10px; left: 0px; bottom: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; width: 1774px;"></div></div><canvas class="decorationsOverviewRuler" aria-hidden="true" width="14" height="637" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; top: 0px; right: 0px; width: 14px; height: 637px; will-change: unset; display: block;"></canvas><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute; width: 14px; height: 637px; right: 0px; top: 0px;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 14px; transform: translate3d(0px, 0px, 0px); contain: strict; will-change: unset; height: 637px;"></div></div></div><div role="presentation" aria-hidden="true" style="width: 1794px;"></div><textarea data-mprt="6" class="inputarea monaco-mouse-cursor-text" wrap="on" autocorrect="off" autocapitalize="off" autocomplete="off" spellcheck="false" aria-label="Editor content;Press Alt+F1 for Accessibility Options." tabindex="0" role="textbox" aria-roledescription="editor" aria-multiline="true" aria-haspopup="false" aria-autocomplete="both" style="tab-size: 15.3984px; font-family: monospace, Consolas, &quot;Courier New&quot;, monospace; font-weight: normal; font-size: 14px; font-feature-settings: &quot;liga&quot; 0, &quot;calt&quot; 0; font-variation-settings: normal; line-height: 19px; letter-spacing: 0px; top: 0px; left: 6px; width: 76992px; height: 1px;" data-has-listeners="true"></textarea><div class="monaco-editor-background textAreaCover" style="position: absolute; top: 0px; left: 0px; width: 0px; height: 0px;"></div><div data-mprt="4" class="overlayWidgets" style="width: 1794px;"></div><div data-mprt="8" class="minimap slider-mouseover" role="presentation" aria-hidden="true" style="position: absolute; left: 0px; width: 0px; height: 637px;"><div class="minimap-shadow-hidden" style="height: 637px;"></div><canvas width="0" height="637" style="position: absolute; left: 0px; width: 0px; height: 637px;"></canvas><canvas class="minimap-decorations-layer" width="0" height="637" style="position: absolute; left: 0px; width: 0px; height: 637px;"></canvas><div class="minimap-slider" style="position: absolute; transform: translate3d(0px, 0px, 0px); contain: strict; width: 0px; will-change: unset;"><div class="minimap-slider-horizontal" style="position: absolute; width: 0px; height: 0px;"></div></div></div><div role="presentation" aria-hidden="true" class="blockDecorations-container"></div></div><div data-mprt="2" class="overflowingContentWidgets" style="display: none;"><div widgetid="editor.contrib.resizableContentHoverWidget" style="position: fixed; height: 10px; width: 10px; z-index: 50; display: none; visibility: hidden; max-width: 1920px;"><div class="monaco-sash vertical" style="left: 8px;"></div><div class="monaco-sash vertical" style="left: -2px;"></div><div class="monaco-sash orthogonal-edge-north horizontal" style="top: -2px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-sash orthogonal-edge-south horizontal" style="top: 8px;"><div class="orthogonal-drag-handle start"></div><div class="orthogonal-drag-handle end"></div></div><div class="monaco-hover hidden" tabindex="0" role="tooltip"><div class="monaco-scrollable-element " role="presentation" style="position: relative; overflow: hidden;"><div class="monaco-hover-content" style="overflow: hidden; font-size: 14px; line-height: 1.35714; max-width: 1184.04px; max-height: 250px;"></div><div role="presentation" aria-hidden="true" class="invisible scrollbar horizontal" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; height: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div role="presentation" aria-hidden="true" class="invisible scrollbar vertical" style="position: absolute;"><div class="slider" style="position: absolute; top: 0px; left: 0px; width: 10px; transform: translate3d(0px, 0px, 0px); contain: strict;"></div></div><div class="shadow"></div><div class="shadow"></div><div class="shadow"></div></div></div></div></div><div class=".in-cell-overflowing"><div widgetid="editor.contrib.quickInputWidget" style="position: absolute; top: 0px; right: 50%;"></div></div></div></div></div><colab-form class="formview vertical layout flex"><div class="widget-area vertical layout"></div></colab-form></div>
    <div class="output" aria-label="Cell 0 output" role="region"><!----> <div class="output-header"> </div>
        <div class="output-content">
          <div class="output-info"><colab-output-info><template shadowrootmode="open"><!----><md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" aria-describedby="button-output-actions-tooltip" data-aria-label="Code cell output actions" id="button-output-actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Code cell output actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
        <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$--><svg viewBox="0 0 24 24"><!--?lit$320062509$--><path d="m15.9 3.07c-4.32 0.0742-8.64-0.0355-13 0.0568-1.37 0.307-1.74 2.1-1.41 3.26 0.469 0.606 1.86 0.384 1.66-0.525 0.0448-0.329-0.183-0.93 0.354-0.766h13.3v1.53h1.71c0.0709-1.13 0.141-2.62-0.968-3.3-0.511-0.264-1.11-0.252-1.67-0.259zm2.94 6.84v4.87c1.62-1.62 3.24-3.24 4.87-4.87h-4.87zm0 0h-1.71v3.43l1.57 1.57c0.32-1.65 0.0556-3.34 0.135-5zm-1.71 3.43v-3.43h-3.43c1.14 1.14 2.29 2.29 3.43 3.43zm1.4 4.27h-1.71v1.48h-13.6v-1.48h-1.71c-0.0473 1.15-0.16 2.72 1.09 3.29 1.47 0.506 3.02 0.0265 4.53 0.192 3.34-0.0051 6.68 0.0336 10-0.0245 1.49-0.366 1.56-2.22 1.42-3.45zm-10.1-1.12c-0.398-0.483-0.796-0.967-1.19-1.45 0.59-0.683 1.18-1.37 1.77-2.05h-8.67v-2h8.67c-0.59-0.683-1.18-1.37-1.77-2.05 0.398-0.483 0.796-0.967 1.19-1.45 1.28 1.5 2.56 3 3.84 4.5-1.28 1.5-2.56 3-3.84 4.5z"></path></svg></md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" id="button-output-actions-tooltip" for="button-output-actions" message="Code cell output actions"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Code cell output actions</div><!----><!--?--></template></colab-tooltip-trigger></template></colab-output-info></div>
          <div class="output-iframe-container">
            <div class="output-iframe-sizer"> <div><div><colab-static-output-renderer tabindex="0" role="group"><div><div class="stream output_text"><pre>
--- Rock, Paper, Scissors ---
Enter your choice (rock, paper, scissors) or 'quit' to exit: ROCK
Computer chose: paper
You lose!

--- Rock, Paper, Scissors ---
Enter your choice (rock, paper, scissors) or 'quit' to exit: PAPER
Computer chose: paper
It's a tie!

--- Rock, Paper, Scissors ---
Enter your choice (rock, paper, scissors) or 'quit' to exit: ROCK
Computer chose: scissors
You win!

--- Rock, Paper, Scissors ---
Enter your choice (rock, paper, scissors) or 'quit' to exit: quit
Thanks for playing!
</pre></div></div><div></div></colab-static-output-renderer></div></div><div><div></div></div></div>
          </div>
        </div></div></div><colab-cell-next-steps><template shadowrootmode="open"><!----></template></colab-cell-next-steps></div></div><div class="add-cell">
      <hr>
    </div></div></div>
              </div>
            </div>
          <section class="sidebar" aria-label="Comments" style="display: none;"></section></div>
          <!--?lit$320062509$--> <div class="footer-links">
      <a target="_blank" href="https://colab.research.google.com/signup?utm_source=footer&amp;utm_medium=link&amp;utm_campaign=footer_links">
        <!--?lit$320062509$-->Colab paid products
      </a>
      -
      <a href="https://colab.research.google.com/cancel-subscription" target="_blank">
        <!--?lit$320062509$-->Cancel contracts here
      </a>
    </div>
        </div>
      </colab-shaded-scroller>
      <div class="notebook-scroll-shadow"></div>
    </div><div class="right-pane-snap-hint"></div></colab-tab></div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 40%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$320062509$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$320062509$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      <colab-resizer style="width: 37%" class="we-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$320062509$--> <div class="layout vertical tab-pane-parent">
      <!--?lit$320062509$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$320062509$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      <colab-resizer style="height: 40%" class="sn-resize no-tabs"><div class="resizer-thumb"></div>
        <!--?lit$320062509$--><colab-tab-pane class="layout vertical grow no-tabs" align="horizontal"><!----> <div class="layout vertical grow">
    <div class="tab-pane-header layout horizontal noshrink">
      <md-tabs><template shadowrootmode="open"><!---->
      <div class="tabs">
        <slot></slot>
      </div>
      <md-divider part="divider"><template shadowrootmode="open"><!----></template></md-divider>
    </template></md-tabs>
      <div class="layout grow"></div>
      <!--?lit$320062509$--> <md-icon-button data-aria-expanded="false" data-aria-haspopup="menu" title="More tab actions" data-aria-label="More tab actions" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="More tab actions" aria-haspopup="menu" aria-expanded="false">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
    <md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>more_horiz</md-icon>
  </md-icon-button>
    </div>
    <div class="layout vertical grow tab-pane-container"> </div>
  </div></colab-tab-pane>
      </colab-resizer>
    </div>
      </colab-resizer>
    </div></colab-tab-layout-container>
        </div>
        <div class="proxies"><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation" src="./Orioye.E.project8.ipy_files/outputframe.html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div><div><colab-dom-lifecycle-events style="display: none;"></colab-dom-lifecycle-events><iframe allow="accelerometer; autoplay; gyroscope; magnetometer; xr-spatial-tracking; clipboard-write" sandbox="allow-downloads allow-forms allow-pointer-lock allow-popups allow-popups-to-escape-sandbox allow-same-origin allow-scripts allow-storage-access-by-user-activation allow-modals" src="./Orioye.E.project8.ipy_files/outputframe(1).html" style="width: 1px; height: 1px; position: absolute; top: -100px;"></iframe></div></div>
      <colab-file-viewer-manager></colab-file-viewer-manager></div>
    <colab-status-bar role="region" aria-label="Runtime status bar"><template shadowrootmode="open"><!----><span class="left">
        <slot name="bottom-pane-buttons"></slot>
      </span>
      <span class="middle"><!--?lit$320062509$-->
      <md-icon-button toggle="" id="toggle-composer" data-aria-label="Toggle Gemini" value=""><template shadowrootmode="open" shadowrootdelegatesfocus><!----><button id="button" class="icon-button  standard " aria-label="Toggle Gemini" aria-pressed="false">
        <!--?lit$320062509$--><md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
        <!--?lit$320062509$--><md-ripple aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
        <!--?lit$320062509$--><span class="icon"><slot></slot></span>
        <!--?lit$320062509$-->
        <!--?lit$320062509$--><span class="touch"></span>
  </button></template>
        <!--?lit$320062509$--><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>spark</md-icon>
      </md-icon-button>
      <colab-tooltip-trigger aria-hidden="true" for="toggle-composer" message="Toggle Gemini"><template shadowrootmode="open"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Toggle Gemini</div><!----><!--?--></template>
      </colab-tooltip-trigger>
    </span>
      <span class="right">
        <!--?lit$320062509$--><colab-execution-status><template shadowrootmode="open"><!----></template></colab-execution-status><!--?lit$320062509$--><!--?lit$320062509$--><!--?lit$320062509$--><colab-runtime-status><template shadowrootmode="open"><!----></template></colab-runtime-status>
      </span></template><md-text-button slot="bottom-pane-buttons" command="show-variables" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$320062509$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$320062509$--><button id="button" class="button">
      <!--?lit$320062509$-->
      <span class="touch"></span>
      <!--?lit$320062509$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$320062509$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->data_object</md-icon>
        <!--?lit$320062509$-->Variables</md-text-button><md-text-button slot="bottom-pane-buttons" command="show-terminal" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$320062509$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$320062509$--><button id="button" class="button">
      <!--?lit$320062509$-->
      <span class="touch"></span>
      <!--?lit$320062509$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$320062509$-->
    
    </button>
    </template>
        <md-icon slot="icon" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template><!--?lit$320062509$-->terminal</md-icon>
        <!--?lit$320062509$-->Terminal</md-text-button></colab-status-bar></div><div class="goog-menu" id="file-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$320062509$--><div command="locate-in-drive" class=" goog-menuitem " role="menuitem" id=":2" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Locate in Drive<!--?lit$320062509$--></div></div><div command="open-in-playground" class=" goog-menuitem " role="menuitem" id=":3" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Open in playground mode<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":4" style="user-select: none;"></div><div command="new" class=" goog-menuitem " role="menuitem" id=":5" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->New notebook in Drive<!--?lit$320062509$--></div></div><div command="open" class=" goog-menuitem " role="menuitem" id=":6" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Open notebook<!--?lit$320062509$--></div></div><div command="import-notebook" class=" goog-menuitem " role="menuitem" id=":7" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Upload notebook<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":8" style="user-select: none;"></div><div command="rename" class=" goog-menuitem " role="menuitem" id=":9" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Rename<!--?lit$320062509$--></div></div><div command="move-notebook" class=" goog-menuitem " role="menuitem" id=":a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Move<!--?lit$320062509$--></div></div><div command="trash" class=" goog-menuitem " role="menuitem" id=":b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Move to the bin<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":c" style="user-select: none;"></div><div command="clone" class=" goog-menuitem " role="menuitem" id=":d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Save a copy in Drive<!--?lit$320062509$--></div></div><div command="copy-to-gist" class=" goog-menuitem " role="menuitem" id=":e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Save a copy as a GitHub Gist<!--?lit$320062509$--></div></div><div command="copy-to-github" class=" goog-menuitem " role="menuitem" id=":f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Save a copy in GitHub<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":g" style="user-select: none;"></div><div command="save" class=" goog-menuitem " role="menuitem" id=":h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Save<!--?lit$320062509$--></div></div><div command="save-and-checkpoint" class=" goog-menuitem " role="menuitem" id=":i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Save and pin revision<!--?lit$320062509$--></div></div><div command="show-history" class=" goog-menuitem " role="menuitem" id=":j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Revision history<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":k" style="user-select: none;"></div><div class="goog-submenu goog-menuitem" id="download-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$320062509$-->Download
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div command="print" class=" goog-menuitem " role="menuitem" id=":o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Print<!--?lit$320062509$--></div></div></div><div class="goog-menu" id="download-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$320062509$--><div command="download-ipynb" class=" goog-menuitem " role="menuitem" id=":m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Download .ipynb<!--?lit$320062509$--></div></div><div command="download-python" class=" goog-menuitem " role="menuitem" id=":n" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Download .py<!--?lit$320062509$--></div></div></div><div class="goog-menu" id="edit-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$320062509$--><div command="undo" class=" goog-menuitem " role="menuitem" id=":q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Undo<!--?lit$320062509$--></div></div><div command="redo" class=" goog-menuitem " role="menuitem" id=":r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Redo<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":s" style="user-select: none;"></div><div command="select-all" class=" goog-menuitem " role="menuitem" id=":t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Select all cells<!--?lit$320062509$--></div></div><div command="cut" class=" goog-menuitem " role="menuitem" id=":u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Cut cell or selection<!--?lit$320062509$--></div></div><div command="copy" class=" goog-menuitem " role="menuitem" id=":v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Copy cell or selection<!--?lit$320062509$--></div></div><div command="paste" class=" goog-menuitem " role="menuitem" id=":w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Paste<!--?lit$320062509$--></div></div><div command="delete-cell-or-selection" class=" goog-menuitem " role="menuitem" id=":x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Delete selected cells<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":y" style="user-select: none;"></div><div command="find" class=" goog-menuitem " role="menuitem" id=":z" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Find and replace<!--?lit$320062509$--></div></div><div command="find-next" class=" goog-menuitem " role="menuitem" id=":10" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Find next<!--?lit$320062509$--></div></div><div command="find-previous" class=" goog-menuitem " role="menuitem" id=":11" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Find previous<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":12" style="user-select: none;"></div><div command="notebook-settings" class=" goog-menuitem " role="menuitem" id=":13" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Notebook settings<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":14" style="user-select: none;"></div><div command="clear-outputs" class=" goog-menuitem " role="menuitem" id=":15" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Clear all outputs<!--?lit$320062509$--></div></div></div><div class="goog-menu" id="view-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$320062509$--><div command="show-toc-pane" class="goog-menuitem goog-option" role="menuitemcheckbox" aria-checked="false" id=":17" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><div class="goog-menuitem-checkbox" style="user-select: none;"><!----><md-icon aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>check</md-icon> </div><!--?lit$320062509$-->Table of contents<!--?lit$320062509$--></div></div><div command="show-fileinfo" class=" goog-menuitem " role="menuitem" id=":18" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Notebook info<!--?lit$320062509$--></div></div><div command="show-executedcode" class=" goog-menuitem " role="menuitem" id=":19" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Executed code history<!--?lit$320062509$--></div></div><div command="start-presentation" class=" goog-menuitem " role="menuitem" id=":1a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Start slideshow<!--?lit$320062509$--></div></div><div command="start-presentation-beginning" class=" goog-menuitem " role="menuitem" id=":1b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Start slideshow from beginning<!--?lit$320062509$--></div></div><div class="goog-submenu goog-menuitem" id="comments-submenu-menu-button" role="menuitem" aria-haspopup="true" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;">
      <!--?lit$320062509$-->Comments
    <span class="goog-submenu-arrow" style="user-select: none;">►</span></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1g" style="user-select: none;"></div><div command="collapse-sections" class=" goog-menuitem " role="menuitem" id=":1h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Collapse sections<!--?lit$320062509$--></div></div><div command="expand-sections" class=" goog-menuitem " role="menuitem" id=":1i" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Expand sections<!--?lit$320062509$--></div></div><div command="save-section-layout" class=" goog-menuitem " role="menuitem" id=":1j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Save collapsed section layout<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1k" style="user-select: none;"></div><div command="hide-code" class=" goog-menuitem " role="menuitem" id=":1l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Show/hide code<!--?lit$320062509$--></div></div><div command="toggle-output" class=" goog-menuitem " role="menuitem" id=":1m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Show/hide output<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1n" style="user-select: none;"></div><div command="focus-next-tab" class=" goog-menuitem " role="menuitem" id=":1o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Focus next tab<!--?lit$320062509$--></div></div><div command="focus-previous-tab" class=" goog-menuitem " role="menuitem" id=":1p" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Focus previous tab<!--?lit$320062509$--></div></div><div command="move-tab-to-next" class=" goog-menuitem " role="menuitem" id=":1q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Move tab to next pane<!--?lit$320062509$--></div></div><div command="move-tab-to-prev" class=" goog-menuitem " role="menuitem" id=":1r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Move tab to previous pane<!--?lit$320062509$--></div></div></div><div class="goog-menu" id="comments-submenu-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$320062509$--><div command="hide-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Hide comments<!--?lit$320062509$--></div></div><div command="show-minimized-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1e" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Minimise comments<!--?lit$320062509$--></div></div><div command="show-expanded-sidebar-comments" class=" goog-menuitem goog-option-selectable " role="menuitem" id=":1f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Expand comments<!--?lit$320062509$--></div></div></div><div class="goog-menu" id="insert-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$320062509$--><div command="insert-cell-below" class=" goog-menuitem " role="menuitem" id=":1t" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Code cell<!--?lit$320062509$--></div></div><div command="add-text" class=" goog-menuitem " role="menuitem" id=":1u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Text cell<!--?lit$320062509$--></div></div><div command="add-section-header" class=" goog-menuitem " role="menuitem" id=":1v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Section header cell<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1w" style="user-select: none;"></div><div command="open-scratch-code-cell" class=" goog-menuitem " role="menuitem" id=":1x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Scratch code cell<!--?lit$320062509$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":1y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Code snippets<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":1z" style="user-select: none;"></div><div command="add-form-field" class=" goog-menuitem " role="menuitem" id=":20" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Add a form field<!--?lit$320062509$--></div></div></div><div class="goog-menu" id="runtime-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$320062509$--><div command="runall" class=" goog-menuitem " role="menuitem" id=":22" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Run all<!--?lit$320062509$--></div></div><div command="runbefore" class=" goog-menuitem " role="menuitem" id=":23" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Run before<!--?lit$320062509$--></div></div><div command="runfocused" class=" goog-menuitem " role="menuitem" id=":24" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Run the focused cell<!--?lit$320062509$--></div></div><div command="runselected" class=" goog-menuitem " role="menuitem" id=":25" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Run selection<!--?lit$320062509$--></div></div><div command="runafter" class=" goog-menuitem " role="menuitem" id=":26" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Run cell and below<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":27" style="user-select: none;"></div><div command="interrupt" class=" goog-menuitem " role="menuitem" id=":28" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Interrupt execution<!--?lit$320062509$--></div></div><div command="restart" class=" goog-menuitem " role="menuitem" id=":29" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Restart session<!--?lit$320062509$--></div></div><div command="restart-and-run-all" class=" goog-menuitem " role="menuitem" id=":2a" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Restart session and run all<!--?lit$320062509$--></div></div><div command="powerwash-current-vm" class=" goog-menuitem " role="menuitem" id=":2b" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Disconnect and delete runtime<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2c" style="user-select: none;"></div><div command="change-runtime-type" class=" goog-menuitem " role="menuitem" id=":2d" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Change runtime type<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2e" style="user-select: none;"></div><div command="manage-sessions" class=" goog-menuitem " role="menuitem" id=":2f" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Manage sessions<!--?lit$320062509$--></div></div><div command="open-resource-viewer" class=" goog-menuitem " role="menuitem" id=":2g" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->View resources<!--?lit$320062509$--></div></div><div command="view-runtime-logs" class=" goog-menuitem " role="menuitem" id=":2h" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->View runtime logs<!--?lit$320062509$--></div></div></div><div class="goog-menu" id="tools-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$320062509$--><div command="show-command-palette" class=" goog-menuitem " role="menuitem" id=":2j" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Command palette<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2k" style="user-select: none;"></div><div command="preferences" class=" goog-menuitem " role="menuitem" id=":2l" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Settings<!--?lit$320062509$--></div></div><div command="shortcuts" class=" goog-menuitem " role="menuitem" id=":2m" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Keyboard shortcuts<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2n" style="user-select: none;"></div><div command="open-differ" class=" goog-menuitem " role="menuitem" id=":2o" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Diff notebooks<!--?lit$320062509$--> <span class="screenreader-only" style="user-select: none;"><!--?lit$320062509$-->(opens in a new tab)</span></div></div></div><div class="goog-menu" id="help-menu" role="menu" aria-haspopup="true" style="display: none; user-select: none;"><!--?lit$320062509$--><div command="faq" class=" goog-menuitem " role="menuitem" id=":2q" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Frequently asked questions<!--?lit$320062509$--></div></div><div command="view-relnotes" class=" goog-menuitem " role="menuitem" id=":2r" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->View release notes<!--?lit$320062509$--></div></div><div command="snippets" class=" goog-menuitem " role="menuitem" id=":2s" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Search code snippets<!--?lit$320062509$--></div></div><div class="goog-menuseparator goog-menuitem-disabled" aria-disabled="true" role="separator" id=":2t" style="user-select: none;"></div><div command="report-bug" class=" goog-menuitem " role="menuitem" id=":2u" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Report a bug<!--?lit$320062509$--></div></div><div command="report-abuse" class=" goog-menuitem " role="menuitem" id=":2v" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Report Drive abuse<!--?lit$320062509$--></div></div><div command="send-feedback" class=" goog-menuitem " role="menuitem" id=":2w" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->Send feedback<!--?lit$320062509$--></div></div><div command="view-tos" class=" goog-menuitem " role="menuitem" id=":2x" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->View Terms of Service<!--?lit$320062509$--></div></div><div command="view-in-english" class=" goog-menuitem " role="menuitem" id=":2y" style="user-select: none;"><div class="goog-menuitem-content" style="user-select: none;"><!--?lit$320062509$-->View in English<!--?lit$320062509$--></div></div></div><dialog class="doc-comments-area" aria-label="Comments"><!----><div class="doc-comments-buttons">
        <md-text-button command="add-comment" value="" has-icon=""><template shadowrootmode="open" shadowrootdelegatesfocus><!---->
      <!--?lit$320062509$-->
      <div class="background"></div>
      <md-focus-ring part="focus-ring" for="button" aria-hidden="true"><template shadowrootmode="open"><!----></template></md-focus-ring>
      <md-ripple part="ripple" for="button" aria-hidden="true"><template shadowrootmode="open"><!----><div class="surface   "></div></template></md-ripple>
      <!--?lit$320062509$--><button id="button" class="button">
      <!--?lit$320062509$-->
      <span class="touch"></span>
      <!--?lit$320062509$--><slot name="icon"></slot>
      <span class="label"><slot></slot></span>
      <!--?lit$320062509$-->
    
    </button>
    </template>
          <md-icon slot="icon" filled="" aria-hidden="true"><template shadowrootmode="open"><!----><slot></slot></template>comment</md-icon>
          <!--?lit$320062509$-->Add a comment
        </md-text-button>
      </div></dialog><div class="thumbnail"></div><div class="monaco-aria-container"><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-alert" role="alert" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div><div class="monaco-status" role="complementary" aria-live="polite" aria-atomic="true"></div></div><iframe id="apiproxy788a7c9dc68e756eb2da844404158205b0e0c41a0.2448867047" name="apiproxy788a7c9dc68e756eb2da844404158205b0e0c41a0.2448867047" src="./Orioye.E.project8.ipy_files/proxy.html" tabindex="-1" aria-hidden="true" style="width: 1px; height: 1px; position: absolute; top: -100px; display: none;"></iframe><div><div class="grecaptcha-badge" data-style="bottomright" style="width: 256px; height: 60px; position: fixed; visibility: hidden; display: block; transition: right 0.3s; bottom: 14px; right: -186px; box-shadow: gray 0px 0px 5px; border-radius: 2px; overflow: hidden;"><div class="grecaptcha-logo"><iframe title="reCAPTCHA" width="256" height="60" role="presentation" name="a-i7gpepswxg9k" frameborder="0" scrolling="no" sandbox="allow-forms allow-popups allow-same-origin allow-scripts allow-top-navigation allow-modals allow-popups-to-escape-sandbox allow-storage-access-by-user-activation" src="./Orioye.E.project8.ipy_files/anchor.html"></iframe></div><div class="grecaptcha-error"></div><textarea id="g-recaptcha-response-100000" name="g-recaptcha-response" class="g-recaptcha-response" style="width: 250px; height: 40px; border: 1px solid rgb(193, 193, 193); margin: 10px 25px; padding: 0px; resize: none; display: none;" data-has-listeners="true"></textarea></div><iframe style="display: none;" src="./Orioye.E.project8.ipy_files/saved_resource.html"></iframe></div><iframe src="./Orioye.E.project8.ipy_files/bscframe.html" style="display: none;"></iframe><colab-callout dismisstext="" tooltipstyling="" aria-label="Rename notebook" opened="" role="tooltip" verticaldirection="below" horizontaldirection="right" style="visibility: visible; top: 38px; left: 127.398px;"><template shadowrootmode="open"><!----> <div id="content"><slot name="content"></slot></div>
      <!--?lit$320062509$--><!--?--></template>
      <!--?lit$320062509$--><div slot="content"><!----><!--?lit$320062509$--><!----><div><!--?lit$320062509$-->Rename notebook</div><!----><!--?--></div>
    </colab-callout></body><div id="aitopia" class="aitopia dark" data-v-app=""><!----><!----><div id="aitopia-container" class="close-sidebar"><div id="aitopia-sidebar"><div id="ai-sidebar" class="ait-flex ait-w-full ait-h-full ait-overflow-hidden"><div class="ait-flex ait-flex-col ait-w-[calc(100%_-_60px)]" id="ait-sidebar-chat"><div class="ait-header ait-flex-shrink"><nav class="ait-w-full ait-bg-[transparent]"><div class="ait-flex ait-items-center ait-w-full ait-p-0"><div class="ait-flex ait-items-center ait-justify-between ait-w-full"><div class="ait-flex ait-items-center ait-justify-between"><span><svg class="ait-w-8 ait-h-8  ait-logo" xmlns="http://www.w3.org/2000/svg" baseProfile="tiny" viewBox="0 0 125 121.7" overflow="visible"><circle fill="#01a77d" cx="63.4" cy="61.2" r="57.8"></circle><g fill="#fff"><path d="M46.9 60.5h-.4c-1.9-.2-3.3-1.9-3.1-3.8.6-6.3 4.5-38 17.3-41.2 8.2-2 14.4 7.5 16.5 10.6 1.1 1.6.6 3.8-1 4.9s-3.8.6-4.9-1c-3.5-5.3-6.9-8.2-9-7.7-4.2 1-10 14.8-12 35.1-.2 1.7-1.7 3.1-3.4 3.1zm51.9-4.9c-.5 0-1-.1-1.4-.3-1.8-.8-2.6-2.9-1.8-4.6 2.6-5.8 3.2-10.2 1.7-11.7-3.1-3-17.8-.6-36.1 8.6-1.7.9-3.8.2-4.7-1.6-.9-1.7-.2-3.8 1.6-4.7.3-.2 8.3-4.1 17.4-7.1 13.4-4.5 22.2-4.5 26.7-.2 6.1 5.8 1.4 16.2-.1 19.6-.7 1.3-2 2-3.3 2zM88.2 89.5c-1.8 0-3.3-1.3-3.5-3.1-.2-1.9 1.1-3.7 3.1-3.9 6.3-.7 10.4-2.5 10.9-4.6 1-4.2-8.7-15.6-25.9-26.6-1.6-1-2.1-3.2-1.1-4.8s3.2-2.1 4.8-1.1c.3.2 7.8 5 15.1 11.3 10.7 9.3 15.3 16.7 13.9 22.8-1.9 8.2-13.2 9.5-16.9 10h-.4zm-25.9 18.1c-7.2 0-12.4-8.3-14.2-11.2-1-1.6-.5-3.8 1.1-4.8s3.8-.5 4.8 1.1c3.4 5.4 6.7 8.3 8.8 7.9 4.2-.9 10.3-14.5 12.9-34.8.2-1.9 2-3.3 3.9-3 1.9.2 3.3 2 3 3.9-.8 6.3-5.4 37.9-18.4 40.7-.5.1-1.2.2-1.9.2zm-25-18.1c-5.5 0-9.4-1.3-11.8-4-5.6-6.3-.1-16.3 1.6-19.5.9-1.7 3.1-2.3 4.7-1.4 1.7.9 2.3 3.1 1.4 4.7-3.1 5.6-4 9.9-2.6 11.5 2.9 3.2 17.7 1.9 36.7-5.7a3.57 3.57 0 0 1 4.6 1.9 3.57 3.57 0 0 1-1.9 4.6c-.3.1-8.6 3.5-17.9 5.8-5.9 1.4-10.8 2.1-14.8 2.1zm16.5-12.6c-.6 0-1.2-.2-1.8-.5-.3-.2-7.9-4.8-15.4-10.8-11-8.9-15.8-16.2-14.6-22.3 1.6-8.2 12.9-9.9 16.6-10.5 1.9-.3 3.7 1 4 2.9s-1 3.7-2.9 4c-6.3.9-10.3 2.8-10.7 4.9-1 4.3 9 15.3 26.6 25.8 1.7 1 2.2 3.1 1.2 4.8-.7 1.1-1.8 1.7-3 1.7z"></path><circle cx="63.8" cy="60.5" r="8.4"></circle></g></svg></span><div class="ait-self-center ait-text-base ait-text-black ait-ml-2 dark:ait-text-gray-200 ait-whitespace-nowrap">Chat</div></div><div class="ait-flex ait-items-center ait-max-h-[50px]"><button class="ait-flex ait-items-center ait-space-x-2 ait-bg-transparent hover:ait-bg-[var(--ait-link-color)] ait-transition-all ait-rounded-full ait-p-1 ait-px-2"><svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" aria-hide="true" class="ait-w-4 ait-h-4 dark:ait-text-gray-200"><path stroke-linecap="round" stroke-linejoin="round" d="M12 4.5v15m7.5-7.5h-15"></path></svg><span class="ait-text-sm dark:ait-text-gray-200">New Conversation</span></button><button type="button" class="ait-ml-2 svg-logo"><span><svg class="ait-h-6 ait-w-6 ait-history_icon" width="1em" height="1em" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M20 12C20 16.4183 16.4183 20 12 20C7.58172 20 4 16.4183 4 12C4 7.58172 7.58172 4 12 4C16.4183 4 20 7.58172 20 12ZM22 12C22 17.5228 17.5228 22 12 22C6.47715 22 2 17.5228 2 12C2 6.47715 6.47715 2 12 2C17.5228 2 22 6.47715 22 12ZM13 8.99939C12.9997 8.4471 12.5517 7.99966 11.9994 8C11.4471 8.00034 10.9997 8.44833 11 9.00061L11.0024 13.0006C11.0026 13.3347 11.1697 13.6466 11.4477 13.832L14.4471 15.832C14.9066 16.1384 15.5275 16.0143 15.8339 15.5548C16.1403 15.0953 16.0161 14.4744 15.5566 14.168L13.0021 12.4647L13 8.99939Z" fill="currentColor"></path></svg></span></button></div></div></div></nav></div><div id="ait-upgrade-plan-modal" class="ait-hide"><div tabindex="-1" aria-hide="true" class="ait-fixed !ait-z-[999999] ait-modal ait-m-0 ait-bg-[rgba(0,0,0,.5)] ait-top-0 ait-left-0 ait-bottom-0 ait-right-0 ait-w-full ait-p-4 ait-overflow-x-hidden ait-overflow-y-auto lg:ait-inset-0 h-[calc(100%)] ait-max-h-full ait-justify-center ait-flex ait-w-full ait-items-center" data-modal-hide=""><div class="ait-relative ait-w-full lg:ait-max-w-screen-xl ait-max-h-full"><div class="ait-relative ait-bg-white ait-rounded-lg ait-shadow dark:ait-bg-neutral-800"><div class="ait-px-6 ait-py-4 ait-border-b ait-rounded-t dark:ait-border-neutral-600"><h3 class="ait-text-base ait-font-semibold ait-text-neutral-900 lg:ait-text-lg dark:ait-text-white ait-text-center">Search</h3><button type="button" class="ait-absolute ait-top-3 ait-right-2.5 ait-text-neutral-400 ait-bg-transparent hover:ait-bg-neutral-200 hover:ait-text-neutral-900 ait-rounded-lg ait-text-sm ait-w-8 ait-h-8 ait-ml-auto ait-inline-flex ait-justify-center ait-items-center dark:hover:ait-bg-neutral-600 dark:hover:ait-text-white" data-modal-hide=""><svg class="ait-w-3 ait-h-3" aria-hide="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"></path></svg><span class="ait-sr-only">Close modal</span></button></div><div class="ait-px-4 ait-py-12 ait-w-full ait-text-center ait-flex ait-flex-col ait-items-center ait-gap-8"><p class="ait-px-4 ait-text-sm ait-text-neutral-600 dark:ait-text-neutral-400">The data of AITOPIA isn't real-time. WebAccess Feature combines the intelligence of AITOPIA with realtime web information, allowing GPT to handle real-time information-related questions more effectively. Upgrade to gain this feature, and worry no more about outdated information!</p><button class="aitopia-pricing ait-cursor-pointer ait-w-full ait-font-semibold ait-text-white ait-text-sm ait-py-2 ait-rounded-md ait-flex ait-items-center ait-gap-2 ait-justify-center ait-bg-[var(--ait-link-color)] hover:ait-opacity-90 ait-transition-all">Upgrade Now</button></div><!----></div></div></div></div><button data-ait-dropdown-toggle="ait-upgrade-plan-modal" id="ait-toggle-upgrade-button" class="ait-hidden"></button><div id="ai-sidebar-content" class="false"><div class="ait-h-[calc(100vh_-_70px)] ait-flex ait-flex-col"><div id="ai-message-container" class="ait-flex ait-relative ait-flex-grow ait-w-full ait-overflow-x-hidden"><div class="ait-w-full"><div class="ait-flex ait-flex-col ait-h-full ait-space-y-3"><div id="aitopia-example"><div class="ait-p-2"><div class="ait-flex ait-items-center ait-justify-between ait-p-3 ait-space-x-3 ait-border ait-rounded-xl ait-bg-neutral-100 dark:ait-bg-neutral-900 dark:ait-text-neutral-200 ait-cursor-pointer"><div><p class="ait-font-bold"> 🤓 Explain a complex thing</p><p class="ait-opacity-60 ait-text-[11px] example_content">Explain Artificial Intelligence so
                        that I can explain it to my six-year-old child.</p></div><button><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="ait-w-5 ait-h-5 ait-cursor-pointer" fill="none"><path d="M20 12L14 6M20 12L14 18M20 12L9.5 12M4 12L6.5 12" stroke="#14746F" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg></button></div></div><div class="ait-p-2"><div class="ait-flex ait-items-center ait-justify-between ait-p-3 ait-space-x-3 ait-border ait-rounded-xl ait-bg-neutral-100 dark:ait-bg-neutral-900 dark:ait-text-neutral-200 ait-cursor-pointer"><div><p class="ait-font-bold"> 🧠 Get suggestions and create new ideas</p><p class="ait-opacity-60 ait-text-[11px] example_content">Please give me the best 10 travel
                        ideas around the world</p></div><button><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="ait-w-5 ait-h-5 ait-cursor-pointer" fill="none"><path d="M20 12L14 6M20 12L14 18M20 12L9.5 12M4 12L6.5 12" stroke="#14746F" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg></button></div></div><div class="ait-p-2"><div class="ait-flex ait-items-center ait-justify-between ait-p-3 ait-space-x-3 ait-border ait-rounded-xl ait-bg-neutral-100 dark:ait-bg-neutral-900 dark:ait-text-neutral-200 ait-cursor-pointer"><div><p class="ait-font-bold"> 💭 Translate, summarize, fix grammar and more…</p><p class="ait-opacity-60 ait-text-[11px] example_content">Translate "I love you" French</p></div><button><svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" class="ait-w-5 ait-h-5 ait-cursor-pointer" fill="none"><path d="M20 12L14 6M20 12L14 18M20 12L9.5 12M4 12L6.5 12" stroke="#14746F" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg></button></div></div></div><!----><div class="ait-h-full" id="aitopia-message"><div aria-details="chat-key-0" class="ait-bg-neutral-100 dark:ait-bg-neutral-900 dark:ait-text-gray-200 ait-mt-[2px] ait-mb-[2px]"><div class="ait-flex ait-p-2 ait-text-[10px] dark:ait-text-gray-200 ait-flex-col ait-items-start ait-justify-start ait-gap-2"><div class="ait-flex ait-items-center ait-space-x-2"><img class="ait-w-[16px] ait-h-[16px]" src="./Orioye.E.project8.ipy_files/logo.svg"><span>AITOPIA</span></div><!----></div><div class="dark:ait-bg-neutral-900 ait-px-6 ait-py-4 ai_result_container"><div class="ait-flex ait-flex-col"><!----><div class="ait-flex ait-flex-row ait-items-center"><div class="ai_result">Hello, how can I help you today?<br></div><!----></div><!----><div class="ait-mt-3 ait-flex ait-items-center ait-float-right ait-cursor-pointer ait-gap-2 ait-divide-x-[0.5px] ait-divide-neutral-300 dark:ait-divide-neutral-700"><div class="ait-bg-neutral-200 dark:ait-bg-neutral-950 ait-w-3 ait-h-3 ait-p-1 ait-rounded-md ait-justify-center ait-flex ait-items-center ait-float-right ait-cursor-pointer"><li data-v-123660cf="" class="ait-relative ait-block ait-popper-container"><svg class="svg-inline--fa fa-clipboard ait-w-3 ait-h-3" aria-hidden="true" focusable="false" data-prefix="far" data-icon="clipboard" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path class="" fill="currentColor" d="M280 64l40 0c35.3 0 64 28.7 64 64l0 320c0 35.3-28.7 64-64 64L64 512c-35.3 0-64-28.7-64-64L0 128C0 92.7 28.7 64 64 64l40 0 9.6 0C121 27.5 153.3 0 192 0s71 27.5 78.4 64l9.6 0zM64 112c-8.8 0-16 7.2-16 16l0 320c0 8.8 7.2 16 16 16l256 0c8.8 0 16-7.2 16-16l0-320c0-8.8-7.2-16-16-16l-16 0 0 24c0 13.3-10.7 24-24 24l-88 0-88 0c-13.3 0-24-10.7-24-24l0-24-16 0zm128-8a24 24 0 1 0 0-48 24 24 0 1 0 0 48z"></path></svg><div data-v-123660cf="" class="ait-absolute ait-z-[9999999] ait-top-0 ait-transform ait--translate-x-1/2 ait-py-1 ait-px-2 ait-rounded-md ait-shadow-lg dark:ait-bg-neutral-100 ait-bg-neutral-800 ait-text-gray-900 dark:ait-text-gray-200 ait-translate-y-[-120%] ait:border-[1px] dark:ait-border-neutral-200 ait-border-neutral-300 ait-left-1/2" style="display: none;"><div data-v-123660cf="" class="ait-text-xs ait-font-medium ait-text-gray-200 dark:ait-text-gray-800 ait-whitespace-nowrap sait-w-full">Copy</div></div><div data-v-123660cf="" class="ait-hide ait-left-0 ait-top-0 ait-bottom-0 ait-left-0 ait-top-1/2 ait-left-1/2 ait-right-1/2 ait-bottom-1/2 ait-translate-x-[-100%] ait-translate-y-[-100%] ait-translate-x-[-120%] ait-translate-y-[-120%]"></div></li></div><!----><!----></div><div class="ait-clear-both"></div></div></div><!----><!----></div><div id="ait-stop-chat-ai_chat" class="ait-stop-chat ait-items-center ait-justify-center ait-sticky ait-top-0 ait-w-full ait-py-2 ait-z-50 ait-bg-white/80 dark:ait-bg-neutral-900/80 ait-backdrop-blur-sm ait-hide"><button class="ait-text-white hover:ait-opacity-90 ait-font-medium ait-text-md ait-px-5 ait-py-2 ait-rounded-md dark:hover:ait-bg-[var(--ait-tab-menu-active-bg-color)]"><div class="ait-flex ait-w-full ait-gap-2 ait-items-center ait-justify-center"><svg stroke="currentColor" fill="none" stroke-width="2" viewBox="0 0 24 24" stroke-linecap="round" stroke-linejoin="round" class="icon-xs" height="1em" width="1em" xmlns="http://www.w3.org/2000/svg"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"></rect></svg> Stop generating</div></button></div></div></div></div></div><div class="ait-px-3 ait-pt-3"><div class="ait-flex ait-relative ait-w-full ait-items-center ait-justify-start ait-my-3 ait-grid ait-grid-cols-5 lg:ait-grid-none lg:grid-cols-2"><div class="ait-flex ait-w-full ait-gap-3 ait-items-center ait-col-span-5 lg:ait-col-span-none"> <div class="ait-flex ait-flex-wrap ait-gap-[6px] ait-max-w-full ait-place-self-end ait-self-center ait-min-w-[55px]"><div class="ait-text-xs ait-relative ait-min-w-[55px]" data-ait-modal-btn="show_model_sidebar"><div class="ait-flex ait-justify-center ait-min-h-full ait-max-h-full ait-items-center ait-leading-4 ait-gap-[2px] lg:ait-flex ait-space-x-1 ait-text-sm ait-relative dark:ait-text-neutral-200 ait-border ait-rounded-xl ait-cursor-pointer ait-pl-[6px] ait-pr-[5px] ait-py-[7px]"><div class="ait-ai-icon ait-flex ait-justify-center ait-items-center ait-rounded-full ait-ml-[1px] ait-mr-[2px]"><div class="ait-flex ait-items-center ait-justify-center ait-rounded-full"><img class="ait-w-[16px] ait-h-[16px]" src="./Orioye.E.project8.ipy_files/logo.svg"></div></div><span class="ait-inline-block ait-text-[13px] ait-text-ellipsis ait-whitespace-nowrap ait-overflow-hidden ait-max-w-full">AITOPIA</span><div class="ait-flex ait-items-end pl-[2px] pr-[2px]"><svg aria-hide="true" fill="currentColor" focusable="false" height="12" role="img" viewBox="0 0 12 12" width="12" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"><path d="M6 8.825c-.2 0-.4-.1-.5-.2l-3.3-3.3c-.3-.3-.3-.8 0-1.1.3-.3.8-.3 1.1 0l2.7 2.7 2.7-2.7c.3-.3.8-.3 1.1 0 .3.3.3.8 0 1.1l-3.2 3.2c-.2.2-.4.3-.6.3Z"></path></svg></div></div><!----></div></div><span class="ait-hide ait-my-2.5 ait-left-[-8px]"></span><!----><div class="ait-flex ait-items-center ait-relative ait-space-x-1 ait-grid-flow-row"><button data-ait-dropdown-toggle="ait-credit-dropdown" class="ait-flex ait-items-center ait-relative dark:ait-text-neutral-200 ait-border ait-rounded-full ait-w-[45px]"><img src="chrome-extension://becfinhbfclcgokjlobojlnldbfillpf/assets/images/coin.png" width="16px" height="16px" alt="coin image" class="ait-w-4 ait-h-4"><div class="ait-text-sm">10</div></button><button type="button" id="aitopia-pricing" class="ait-text-neutral-500 hover:ait-text-neutral-50 hover:ait-bg-green-700 ait-ml-1 ait-rounded-lg focus:ait-outline-none ait-text-[10px] ait-px-1 ait-py-1 ait-text-center aitopia-pricing">Upgrade</button></div><div id="ait-credit-dropdown" class="ait-z-20 ait-left-0 ait-bottom-[40px] ait-width-full ait-absolute ait-hide ait-w-full ait-max-w-[220px] ait-bg-white ait-divide-y ait-divide-neutral-100 ait-rounded-lg ait-shadow dark:ait-bg-neutral-900 dark:ait-divide-neutral-700"><div class="ait-block ait-px-3 ait-py-3 ait-font-medium ait-text-center ait-text-neutral-700 ait-rounded-t-lg ait-bg-neutral-50 dark:ait-bg-neutral-950 dark:ait-text-white"><span class="ait-font-bold">Free Plan</span><button type="button" class="ait-text-white ait-bg-green-700 hover:ait-opacity-90 focus:ait-outline-none focus:ait-ring-4 focus:ait-ring-green-300 ait-font-medium ait-rounded-full ait-text-sm ait-px-5 ait-py-1 ait-text-center ait-ml-5 ait-mr-2 dark:ait-bg-green-600 dark:hover:ait-bg-green-700 dark:focus:ait-ring-green-800 aitopia-pricing">Upgrade</button></div><div class="ait-divide-y ait-divide-neutral-100 dark:ait-divide-neutral-700"><div class="ait-flex ait-px-3 ait-py-3 hover:ait-bg-neutral-100 dark:hover:ait-bg-neutral-700"><div class="ait-w-full ait-px-1 ait-cursor-pointer"><div class="ait-grid ait-grid-cols-4 ait-gap-4 ait-text-neutral-900 dark:ait-text-white ait-text-sm ait-mb-1.5 dark:ait-text-neutral-400"><div class="ait-col-span-3">Fast Text <div class="ait-text-[10px] ait-text-neutral-500 ait-pt-2 dark:ait-text-neutral-400">AITOPIA, GPT-4o Mini, GPT-5 Mini, GPT-4.1 Mini, Claude 3.5 Haiku, Grok 3 Mini, Gemini 2.0 Flash, Gemini 2.5 Flash, Llama 3.3 70B, Llama 4 Maverick, Llama 4 Scout, Dall-e 3, SDXL v1.0, DeepSeek V3</div></div><div class="ait-text-right"><span class="ait-text-sm">10</span></div></div></div></div><div class="ait-flex ait-px-3 ait-py-3 hover:ait-bg-neutral-100 dark:hover:ait-bg-neutral-700"><div class="ait-w-full ait-px-1 ait-cursor-pointer"><div class="ait-grid ait-grid-cols-4 ait-gap-4 ait-text-neutral-900 dark:ait-text-white ait-text-sm ait-mb-1.5 dark:ait-text-neutral-400"><div class="ait-col-span-3">Advanced Text <div class="ait-text-[10px] ait-text-neutral-500 ait-pt-2 dark:ait-text-neutral-400">GPT-5, GPT-4o, GPT-4.1, o1 Mini, o3 Mini, o4 Mini, Grok 3, Claude 3.5 Sonnet, Claude 4 Sonnet, Claude 3.5 Opus, Claude 4 Opus, Gemini 1.5 Pro, Gemini 2.5 Pro, Llama 3.1 405B, SD3, SD3 Large Turbo, DeepSeek R1</div></div><div class="ait-text-right"><span class="ait-text-sm">0</span></div></div></div></div></div></div><div class="ait-capture-tab ait-flex ait-flex-row ait-items-center ait-gap-1 ait-ml-2"><li data-v-123660cf="" class="ait-relative ait-block ait-popper-container"><button class="ait-cursor-pointer ait-p-1.5 ait-rounded-full ait-flex ait-items-center ait-justify-center hover:ait-bg-neutral-300 dark:hover:ait-bg-neutral-900 ait-border ait-transition-all"><svg class="svg-inline--fa fa-scissors ait-w-4 ait-h-4" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="scissors" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M256 192l-39.5-39.5c4.9-12.6 7.5-26.2 7.5-40.5C224 50.1 173.9 0 112 0S0 50.1 0 112s50.1 112 112 112c14.3 0 27.9-2.7 40.5-7.5L192 256l-39.5 39.5c-12.6-4.9-26.2-7.5-40.5-7.5C50.1 288 0 338.1 0 400s50.1 112 112 112s112-50.1 112-112c0-14.3-2.7-27.9-7.5-40.5L499.2 76.8c7.1-7.1 7.1-18.5 0-25.6c-28.3-28.3-74.1-28.3-102.4 0L256 192zm22.6 150.6L396.8 460.8c28.3 28.3 74.1 28.3 102.4 0c7.1-7.1 7.1-18.5 0-25.6L342.6 278.6l-64 64zM64 112a48 48 0 1 1 96 0 48 48 0 1 1 -96 0zm48 240a48 48 0 1 1 0 96 48 48 0 1 1 0-96z"></path></svg></button><div data-v-123660cf="" class="ait-absolute ait-z-[9999999] ait-top-0 ait-transform ait--translate-x-1/2 ait-py-1 ait-px-2 ait-rounded-md ait-shadow-lg dark:ait-bg-neutral-100 ait-bg-neutral-800 ait-text-gray-900 dark:ait-text-gray-200 ait-translate-y-[-120%] ait:border-[1px] dark:ait-border-neutral-200 ait-border-neutral-300 ait-left-1/2" style="display: none;"><div data-v-123660cf="" class="ait-text-xs ait-font-medium ait-text-gray-200 dark:ait-text-gray-800 ait-whitespace-nowrap sait-w-full">Take a screenshot</div></div><div data-v-123660cf="" class="ait-hide ait-left-0 ait-top-0 ait-bottom-0 ait-left-0 ait-top-1/2 ait-left-1/2 ait-right-1/2 ait-bottom-1/2 ait-translate-x-[-100%] ait-translate-y-[-100%] ait-translate-x-[-120%] ait-translate-y-[-120%]"></div></li><li data-v-123660cf="" class="ait-relative ait-block ait-popper-container"><button class="ait-cursor-pointer ait-p-1.5 ait-rounded-full ait-flex ait-items-center ait-justify-center hover:ait-bg-neutral-300 dark:hover:ait-bg-neutral-900 ait-border ait-transition-all"><svg class="svg-inline--fa fa-image ait-w-4 ait-h-4" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="image" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M0 96C0 60.7 28.7 32 64 32l384 0c35.3 0 64 28.7 64 64l0 320c0 35.3-28.7 64-64 64L64 480c-35.3 0-64-28.7-64-64L0 96zM323.8 202.5c-4.5-6.6-11.9-10.5-19.8-10.5s-15.4 3.9-19.8 10.5l-87 127.6L170.7 297c-4.6-5.7-11.5-9-18.7-9s-14.2 3.3-18.7 9l-64 80c-5.8 7.2-6.9 17.1-2.9 25.4s12.4 13.6 21.6 13.6l96 0 32 0 208 0c8.9 0 17.1-4.9 21.2-12.8s3.6-17.4-1.4-24.7l-120-176zM112 192a48 48 0 1 0 0-96 48 48 0 1 0 0 96z"></path></svg></button><div data-v-123660cf="" class="ait-absolute ait-z-[9999999] ait-top-0 ait-transform ait--translate-x-1/2 ait-py-1 ait-px-2 ait-rounded-md ait-shadow-lg dark:ait-bg-neutral-100 ait-bg-neutral-800 ait-text-gray-900 dark:ait-text-gray-200 ait-translate-y-[-120%] ait:border-[1px] dark:ait-border-neutral-200 ait-border-neutral-300 ait-left-1/2" style="display: none;"><div data-v-123660cf="" class="ait-text-xs ait-font-medium ait-text-gray-200 dark:ait-text-gray-800 ait-whitespace-nowrap sait-w-full">Upload an image</div></div><div data-v-123660cf="" class="ait-hide ait-left-0 ait-top-0 ait-bottom-0 ait-left-0 ait-top-1/2 ait-left-1/2 ait-right-1/2 ait-bottom-1/2 ait-translate-x-[-100%] ait-translate-y-[-100%] ait-translate-x-[-120%] ait-translate-y-[-120%]"></div></li><li data-v-123660cf="" class="ait-relative ait-block ait-popper-container"><button data-ait-dropdown-toggle="ait-pdf-upload-modal" class="ait-cursor-pointer ait-p-1.5 ait-rounded-full ait-flex ait-items-center ait-justify-center hover:ait-bg-neutral-300 dark:hover:ait-bg-neutral-900 ait-border ait-transition-all"><span><svg class="ait-w-4 ait-h-4 lg:ait-w-4 lg:ait-h-4 ait-chat_with_file_icon" style="width: 1em; height: 1em;vertical-align: middle;fill: currentColor;overflow: hidden;" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"><path d="M486.4 1024A230.656 230.656 0 0 1 256 793.6v-614.4C256 80.384 336.384 0 435.2 0S614.4 80.384 614.4 179.2v563.2c0 70.5536-57.4464 128-128 128S358.4 812.9536 358.4 742.4v-307.2a25.6 25.6 0 0 1 51.2 0v307.2c0 42.3424 34.4576 76.8 76.8 76.8s76.8-34.4576 76.8-76.8v-563.2C563.2 108.6464 505.7536 51.2 435.2 51.2S307.2 108.6464 307.2 179.2v614.4C307.2 892.416 387.584 972.8 486.4 972.8s179.2-80.384 179.2-179.2v-358.4a25.6 25.6 0 0 1 51.2 0v358.4c0 127.0272-103.3728 230.4-230.4 230.4z" fill=""></path></svg></span></button><div data-v-123660cf="" class="ait-absolute ait-z-[9999999] ait-top-0 ait-transform ait--translate-x-1/2 ait-py-1 ait-px-2 ait-rounded-md ait-shadow-lg dark:ait-bg-neutral-100 ait-bg-neutral-800 ait-text-gray-900 dark:ait-text-gray-200 ait-translate-y-[-120%] ait:border-[1px] dark:ait-border-neutral-200 ait-border-neutral-300 ait-left-1/2" style="display: none;"><div data-v-123660cf="" class="ait-text-xs ait-font-medium ait-text-gray-200 dark:ait-text-gray-800 ait-whitespace-nowrap sait-w-full">Upload File</div></div><div data-v-123660cf="" class="ait-hide ait-left-0 ait-top-0 ait-bottom-0 ait-left-0 ait-top-1/2 ait-left-1/2 ait-right-1/2 ait-bottom-1/2 ait-translate-x-[-100%] ait-translate-y-[-100%] ait-translate-x-[-120%] ait-translate-y-[-120%]"></div></li><li data-v-123660cf="" class="ait-relative ait-block ait-popper-container"><button class="ait-cursor-pointer ait-p-1.5 ait-rounded-full ait-flex ait-items-center ait-justify-center hover:ait-bg-neutral-300 dark:hover:ait-bg-neutral-900 ait-border ait-transition-all"><svg class="svg-inline--fa fa-book ait-w-3.5 ait-h-3.5" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="book" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path class="" fill="currentColor" d="M96 0C43 0 0 43 0 96L0 416c0 53 43 96 96 96l288 0 32 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l0-64c17.7 0 32-14.3 32-32l0-320c0-17.7-14.3-32-32-32L384 0 96 0zm0 384l256 0 0 64L96 448c-17.7 0-32-14.3-32-32s14.3-32 32-32zm32-240c0-8.8 7.2-16 16-16l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16zm16 48l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16s7.2-16 16-16z"></path></svg></button><div data-v-123660cf="" class="ait-absolute ait-z-[9999999] ait-top-0 ait-transform ait--translate-x-1/2 ait-py-1 ait-px-2 ait-rounded-md ait-shadow-lg dark:ait-bg-neutral-100 ait-bg-neutral-800 ait-text-gray-900 dark:ait-text-gray-200 ait-translate-y-[-120%] ait:border-[1px] dark:ait-border-neutral-200 ait-border-neutral-300 ait-left-1/2" style="display: none;"><div data-v-123660cf="" class="ait-text-xs ait-font-medium ait-text-gray-200 dark:ait-text-gray-800 ait-whitespace-nowrap sait-w-full">Read Page</div></div><div data-v-123660cf="" class="ait-hide ait-left-0 ait-top-0 ait-bottom-0 ait-left-0 ait-top-1/2 ait-left-1/2 ait-right-1/2 ait-bottom-1/2 ait-translate-x-[-100%] ait-translate-y-[-100%] ait-translate-x-[-120%] ait-translate-y-[-120%]"></div></li><input type="file" id="imageFileInput" accept="image/jpeg,image/png" style="display: none;"></div><div id="ait-image-vision-modal" class="ait-hide"><div tabindex="-1" aria-hide="true" class="ait-fixed !ait-z-[999999] ait-modal ait-m-0 ait-bg-[rgba(0,0,0,.5)] ait-top-0 ait-left-0 ait-bottom-0 ait-right-0 ait-w-full ait-p-4 ait-overflow-x-hidden ait-overflow-y-auto lg:ait-inset-0 h-[calc(100%)] ait-max-h-full ait-justify-center ait-flex ait-w-full ait-items-center" data-modal-hide=""><div class="ait-relative ait-w-full lg:ait-max-w-screen-xl ait-max-h-full"><div class="ait-relative ait-bg-white ait-rounded-lg ait-shadow dark:ait-bg-neutral-800"><div class="ait-px-6 ait-py-4 ait-border-b ait-rounded-t dark:ait-border-neutral-600"><h3 class="ait-text-base ait-font-semibold ait-text-neutral-900 lg:ait-text-lg dark:ait-text-white ait-text-center">Vision</h3><button type="button" class="ait-absolute ait-top-3 ait-right-2.5 ait-text-neutral-400 ait-bg-transparent hover:ait-bg-neutral-200 hover:ait-text-neutral-900 ait-rounded-lg ait-text-sm ait-w-8 ait-h-8 ait-ml-auto ait-inline-flex ait-justify-center ait-items-center dark:hover:ait-bg-neutral-600 dark:hover:ait-text-white" data-modal-hide=""><svg class="ait-w-3 ait-h-3" aria-hide="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"></path></svg><span class="ait-sr-only">Close modal</span></button></div><div class="ait-p-4 ait-w-full ait-text-center ait-flex ait-flex-col ait-items-center ait-gap-3"><p class="ait-px-4 ait-text-sm ait-text-neutral-600 dark:ait-text-neutral-400">Upload an image to easily get intelligent explanations and extract text from your images.</p><input type="file" id="imageFileInput" accept="image/jpeg,image/png" style="display: none;"><label for="imageFileInput" class="ait-w-full ait-h-full ait-relative ait-z-[9999]"><div class="ait-flex ait-flex-col ait-w-full ait-p-6 ait-items-center ait-justify-center ait-mt-4 ait-border-2 ait-border-dotted ait-border-neutral-300 dark:ait-border-neutral-700 ait-rounded-lg ait-text-neutral-600 dark:ait-text-neutral-400 ait-text-center ait-cursor-pointer ait-transition-all hover:ait-opacity-70"><svg class="svg-inline--fa fa-image ait-w-24 ait-h-24 ait-opacity-60" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="image" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M0 96C0 60.7 28.7 32 64 32l384 0c35.3 0 64 28.7 64 64l0 320c0 35.3-28.7 64-64 64L64 480c-35.3 0-64-28.7-64-64L0 96zM323.8 202.5c-4.5-6.6-11.9-10.5-19.8-10.5s-15.4 3.9-19.8 10.5l-87 127.6L170.7 297c-4.6-5.7-11.5-9-18.7-9s-14.2 3.3-18.7 9l-64 80c-5.8 7.2-6.9 17.1-2.9 25.4s12.4 13.6 21.6 13.6l96 0 32 0 208 0c8.9 0 17.1-4.9 21.2-12.8s3.6-17.4-1.4-24.7l-120-176zM112 192a48 48 0 1 0 0-96 48 48 0 1 0 0 96z"></path></svg><div class="ait-flex ait-flex-col ait-items-center ait-gap-1 ait-mt-2"><span class="ait-block ait-text-xs">Supported image types are JPEG and PNG</span></div><span class="ait-block ait-mt-2 ait-opacity-60">Drag your Image here or click to upload</span></div></label></div><div class="ait-flex ait-flex-row ait-justify-center ait-items-center ait-gap-2 ait-px-4"><div class="ait-h-[1px] ait-w-1/2 ait-bg-neutral-200 dark:ait-bg-neutral-600"></div><p class="ait-text-center ait-text-neutral-600 dark:ait-text-neutral-400 ait-text-lg ait-my-4">Or</p><div class="ait-h-[1px] ait-w-1/2 ait-bg-neutral-200 dark:ait-bg-neutral-600"></div></div><div class="ait-capture-tab ait-flex ait-flex-col ait-px-4 ait-mt-2"><button class="ait-cursor-pointer ait-w-full ait-font-semibold ait-text-white ait-text-sm ait-py-2 ait-rounded-md ait-flex ait-items-center ait-gap-2 ait-justify-center ait-bg-[var(--ait-link-color)] hover:ait-opacity-90 ait-transition-all"><svg class="svg-inline--fa fa-scissors ait-w-3 ait-h-3" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="scissors" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M256 192l-39.5-39.5c4.9-12.6 7.5-26.2 7.5-40.5C224 50.1 173.9 0 112 0S0 50.1 0 112s50.1 112 112 112c14.3 0 27.9-2.7 40.5-7.5L192 256l-39.5 39.5c-12.6-4.9-26.2-7.5-40.5-7.5C50.1 288 0 338.1 0 400s50.1 112 112 112s112-50.1 112-112c0-14.3-2.7-27.9-7.5-40.5L499.2 76.8c7.1-7.1 7.1-18.5 0-25.6c-28.3-28.3-74.1-28.3-102.4 0L256 192zm22.6 150.6L396.8 460.8c28.3 28.3 74.1 28.3 102.4 0c7.1-7.1 7.1-18.5 0-25.6L342.6 278.6l-64 64zM64 112a48 48 0 1 1 96 0 48 48 0 1 1 -96 0zm48 240a48 48 0 1 1 0 96 48 48 0 1 1 0-96z"></path></svg> Take a screenshot</button></div><div class="ait-h-6 ait-mt-4"><!----></div><!----></div></div></div></div><div id="ait-pdf-upload-modal" class="ait-hide"><div tabindex="-1" aria-hide="true" class="ait-fixed !ait-z-[999999] ait-modal ait-m-0 ait-bg-[rgba(0,0,0,.5)] ait-top-0 ait-left-0 ait-bottom-0 ait-right-0 ait-w-full ait-p-4 ait-overflow-x-hidden ait-overflow-y-auto lg:ait-inset-0 h-[calc(100%)] ait-max-h-full ait-justify-center ait-flex ait-items-center" data-modal-hide=""><div class="ait-relative ait-w-full lg:ait-max-w-screen-xl ait-max-h-full"><div class="ait-relative ait-bg-white ait-rounded-lg ait-shadow dark:ait-bg-neutral-800"><div class="ait-px-6 ait-py-4 ait-border-b ait-rounded-t dark:ait-border-neutral-600"><h3 class="ait-text-base ait-font-semibold ait-text-neutral-900 lg:ait-text-lg dark:ait-text-white ait-text-center">Upload File</h3><button type="button" class="ait-absolute ait-top-3 ait-right-2.5 ait-text-neutral-400 ait-bg-transparent hover:ait-bg-neutral-200 hover:ait-text-neutral-900 ait-rounded-lg ait-text-sm ait-w-8 ait-h-8 ait-ml-auto ait-inline-flex ait-justify-center ait-items-center dark:hover:ait-bg-neutral-600 dark:hover:ait-text-white" data-modal-hide=""><svg class="ait-w-3 ait-h-3" aria-hide="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"></path></svg><span class="ait-sr-only">Close modal</span></button></div><div class="ait-p-4 ait-w-full ait-text-center ait-flex ait-flex-col ait-items-center ait-gap-3"><p class="ait-px-4 ait-text-sm ait-text-neutral-600 dark:ait-text-neutral-400">Upload a PDF, Word, Excel, or PowerPoint file to easily get intelligent summaries and answers for your documents.</p><input type="file" id="fileInputPDF" accept=".pdf,.doc,.docx,.xlsx,.xls,.ppt,.pptx" style="display: none;"><label for="fileInputPDF" class="ait-w-full ait-h-full ait-relative ait-z-[9999]"><div class="ait-flex ait-flex-col ait-w-full ait-p-6 ait-items-center ait-justify-center ait-mt-4 ait-border-2 ait-border-dotted ait-border-neutral-300 dark:ait-border-neutral-700 ait-rounded-lg ait-text-neutral-600 dark:ait-text-neutral-400 ait-text-center ait-cursor-pointer ait-transition-all hover:ait-opacity-70"><span><svg class="ait-w-16 ait-h-16 ait-opacity-60 ait-file_icon" style="width: 1em;height: 1em;vertical-align: middle;fill: currentColor;overflow: hidden;" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"><path d="M960 512c0 247.4-200.6 448-448 448-34.1 0-67.2-3.8-99.1-11l-2.7-0.6C211.8 902.3 64 724.4 64 512 64 264.6 264.6 64 512 64c209.9 0 386.2 144.4 434.7 339.3 8.7 34.8 13.3 71.2 13.3 108.7z" fill="#885AEF"></path><path d="M960 512c0 247.4-200.6 448-448 448-34.1 0-67.2-3.8-99.1-11l-2.7-0.6-180.5-180.8 570.2-511.1 146.8 146.8c8.7 34.8 13.3 71.2 13.3 108.7z" fill="#3F2867"></path><path d="M754.4 783.3H270.1c-33 0-60-27-60-60V295.5c0-33 27-60 60-60h484.3c33 0 60 27 60 60v427.8c0 33-27 60-60 60z" fill="#F8A000"></path><path d="M568.8 736.1H329.2c-33.1 0-60-26.9-60-60V148.9c0-33.1 26.9-60 60-60h365.5c33.1 0 60 26.9 60 60V520L568.8 736.1z" fill="#B9FCF3"></path><path d="M568.6 736.1H512V88.9h182.7c33.1 0 60 26.9 60 60V520L568.6 736.1z" fill="#96F5E6"></path><path d="M557.8 176.9c0-9.8 8-17.8 17.8-17.8H668c9.8 0 17.8 8 17.8 17.8s-8 17.8-17.8 17.8h-92.4c-9.8 0-17.8-8-17.8-17.8zM435.6 259.2H668c4.9 0 9.4 2 12.6 5.2 3.2 3.3 5.2 7.7 5.2 12.6 0 9.8-8 17.8-17.8 17.8H435.6c-4.9 0-9.4-2-12.6-5.2s-5.2-7.7-5.2-12.6c0-9.8 8-17.8 17.8-17.8z" fill="#3F2867"></path><path d="M423 289.6c-3.2-3.2-5.2-7.7-5.2-12.6 0-9.8 8-17.8 17.8-17.8h76v35.6h-76c-4.9 0-9.4-2-12.6-5.2z" fill="#8363D4"></path><path d="M814.4 395.5v327.8c0 33-27 60-60 60H270.1c-33 0-60-27-60-60V295.5c0-33 27-60 60-60h136.6l105.3 100h242.4c33 0 60 27 60 60z" fill="#FFD96E"></path><path d="M814.4 395.5v327.8c0 33-27 60-60 60H512V335.5h242.4c33 0 60 27 60 60z" fill="#F7C800"></path><path d="M612.6 599h-50.7v90.3c0 11-9 20-20 20h-59.8c-11 0-20-9-20-20V599h-50.7c-16.4 0-25.8-18.7-16.1-31.9l100.6-136.5c4-5.5 10.2-8.2 16.3-8.1 6 0.1 11.9 2.8 15.8 8.1l100.6 136.5c9.9 13.2 0.4 31.9-16 31.9z" fill="#E95C94"></path><path d="M612.6 599h-50.7v90.3c0 11-9 20-20 20h-29.6V422.5c6 0.1 11.9 2.8 15.8 8.1l100.6 136.5c9.8 13.2 0.3 31.9-16.1 31.9z" fill="#E02B6C"></path></svg></span><div class="ait-flex ait-flex-col ait-items-center ait-gap-1 ait-mt-2"><span class="ait-block ait-text-xs">Supported file types are PDF, Word, Excel, and PowerPoint</span></div><span class="ait-block ait-mt-2 ait-opacity-60">Drag your file here or click to upload</span></div></label><!----><div class="ait-h-6"><!----></div></div><!----><!----></div></div></div></div></div></div><div class="ait-flex ait-flex-col ait-relative ait-items-end ait-p-1 ait-space-x-1 ait-border ait-rounded-xl ait-h-[140px]"><!----><div class="ait-flex ait-flex-wrap ait-gap-[6px] ait-max-w-full ait-place-self-end ait-self-center ait-min-w-[55px]"><ul class="ait-group-model-dropdown ait-hide ait-absolute ait-z-20 ait-width-full ait-w-max ait-min-w-[180px] ait-max-w-[250px] ait-bg-white ait-divide-y ait-divide-neutral-100 ait-rounded-lg ait-shadow dark:ait-bg-neutral-900 dark:ait-divide-neutral-700"><div class="ait-divide-y ait-divide-neutral-100 dark:ait-divide-neutral-700"><!----></div></ul></div><span class="ait-hide ait-my-2.5 ait-left-[-8px]"></span><!----><textarea name="ask" class="ait-selection-container ait-ai-text-item ait-relative ait-w-full ait-h-full ait-p-1 ait-border-0 focus:ait-border-0 focus:ait-shadow-none ait-outline-none ait-resize-none dark:ait-bg-neutral-700 dark:ait-text-neutral-200" id="ask" rows="4" placeholder="Ask me anything..."></textarea><div class="ait-flex ait-w-full ait-justify-between ait-items-center ait-gap-2 ait-p-0.5"><div class="ait-flex ait-gap-1.5 ait-ml-1.5"><div class="ait-flex ait-items-center ait-justify-start ait-gap-3"><li data-v-123660cf="" class="ait-relative ait-block ait-popper-container"><button class="ait-cursor-pointer ait-p-1 ait-rounded-full ait-flex ait-items-center ait-justify-center hover:ait-bg-neutral-300 dark:hover:ait-bg-neutral-900 ait-border ait-transition-all"><span><svg class="ait-w-3.5 ait-h-3.5 ait-at_icon" width="14" height="14" viewBox="0 0 14 14" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M11.03 2.31c1.014 1.048 1.36 2.47 1.36 3.688 0 1.294-.638 2.546-1.408 3.393-.388.427-.833.778-1.286.983-.445.201-.977.293-1.459.053a1 1 0 0 1-.475-.528c-.797.772-1.983 1.077-3.082.528-1.136-.568-1.424-1.846-1.347-2.948.077-1.114.535-2.308 1.21-2.983.945-.945 2.12-1.329 3.126-1.055.555.152 1.01.49 1.313.973q.073-.171.142-.326a.525.525 0 0 1 .977.38c-.26.779-.765 2.243-1.208 3.38-.129.509-.203.95-.207 1.28a1.1 1.1 0 0 0 .047.37c.092.035.26.041.53-.08.29-.132.622-.382.942-.733.644-.708 1.136-1.719 1.136-2.687 0-1.045-.3-2.168-1.066-2.958-.746-.771-2.02-1.314-4.164-1.046-1.827.228-3.242 1.494-3.944 3.13-.703 1.638-.661 3.581.357 5.108.611.917 1.893 1.64 3.475 1.855a7.17 7.17 0 0 0 4.911-1.117.525.525 0 1 1 .58.875 8.22 8.22 0 0 1-5.633 1.282c-1.778-.242-3.379-1.07-4.207-2.313C.405 8.947.382 6.621 1.202 4.71 2.023 2.797 3.72 1.235 5.981.952c2.38-.297 4.017.291 5.049 1.358M8.35 6.039v-.041c0-.937-.446-1.405-.957-1.544-.55-.15-1.354.031-2.107.784-.45.45-.84 1.377-.906 2.314-.066.951.209 1.655.77 1.936.824.412 1.826.025 2.287-.897.124-.247.282-.624.454-1.063l.017-.066c.122-.464.277-.95.443-1.423" fill="currentColor"></path></svg></span></button><div data-v-123660cf="" class="ait-absolute ait-z-[9999999] ait-top-0 ait-transform ait--translate-x-1/2 ait-py-1 ait-px-2 ait-rounded-md ait-shadow-lg dark:ait-bg-neutral-100 ait-bg-neutral-800 ait-text-gray-900 dark:ait-text-gray-200 ait-translate-y-[-120%] ait:border-[1px] dark:ait-border-neutral-200 ait-border-neutral-300 ait-left-1/2" style="display: none;"><div data-v-123660cf="" class="ait-text-xs ait-font-medium ait-text-gray-200 dark:ait-text-gray-800 ait-whitespace-nowrap sait-w-full">Group Chat</div></div><div data-v-123660cf="" class="ait-hide ait-left-0 ait-top-0 ait-bottom-0 ait-left-0 ait-top-1/2 ait-left-1/2 ait-right-1/2 ait-bottom-1/2 ait-translate-x-[-100%] ait-translate-y-[-100%] ait-translate-x-[-120%] ait-translate-y-[-120%]"></div></li></div><div class="ait-flex ait-items-center ait-justify-start ait-gap-3"><label class="ait-relative ait-inline-flex ait-items-center ait-cursor-pointer"><input type="checkbox" class="ait-ai-web-access-checkbox ait-sr-only ait-peer"><div class="ait-w-7 ait-h-4 ait-bg-neutral-200 ait-rounded-full ait-peer peer-focus:ait-ring-3 dark:peer-focus:ait-ring-[var(--ait-link-color)] dark:ait-bg-neutral-700 peer-checked:after:ait-translate-x-full rtl:peer-checked:after:-ait-translate-x-full peer-checked:after:ait-border-white after:ait-content-[&#39;&#39;] after:ait-absolute after:ait-top-0.5 after:ait-start-[2px] after:ait-bg-white after:ait-border-neutral-300 after:ait-border after:ait-rounded-full after:ait-h-3 after:ait-w-3 after:ait-transition-all dark:ait-border-neutral-600 peer-checked:ait-bg-[var(--ait-link-color)]"></div><span class="ait-ms-1.5 ait-text-xs ait-font-medium ait-text-[var(--ait-link-color)] ait-opacity-60 ait-transition-all ait-select-none peer-checked:ait-opacity-100">Web Access</span></label></div></div><li data-v-123660cf="" class="ait-relative ait-block ait-popper-container"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAAZCAYAAADE6YVjAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAz0lEQVR4nN3VoU7CURTH8Y9IsNAwSjDZfALGeAgak2IxWbXpE5jceIZ/hsRG+j8BFDpJosnirnO7bMY/jPNX+W3fdu++O7v3nMOxpokRhjiLkjwiZda4zeKDpvgh2bLCACeRki2LLAuVpEyJbrQkZWa4jpYkfOY7l7tIxjtKUuYDLzivIrnABG97yt7xhFbVqtro4Q6vmGNTUfZ97h4Ne+YKz1hWkPV/rZIOptFvMq7jdxV19EnxVzq+jJxdi8gpfPB98lDHZjzFTfSO92/zBcBszGtUUreMAAAAAElFTkSuQmCC" class="ait-w-5 ait-h-5 ait-opacity-80 ait-cursor-pointer dark:ait-invert" style="filter: invert(0.5) !important;"><div data-v-123660cf="" class="ait-absolute ait-z-[9999999] ait-top-0 ait-transform ait--translate-x-1/2 ait-py-1 ait-px-2 ait-rounded-md ait-shadow-lg dark:ait-bg-neutral-100 ait-bg-neutral-800 ait-text-gray-900 dark:ait-text-gray-200 ait-translate-y-[-120%] ait:border-[1px] dark:ait-border-neutral-200 ait-border-neutral-300 ait-left-1/2" style="display: none;"><div data-v-123660cf="" class="ait-text-xs ait-font-medium ait-text-gray-200 dark:ait-text-gray-800 ait-whitespace-nowrap sait-w-full">Send</div></div><div data-v-123660cf="" class="ait-hide ait-left-0 ait-top-0 ait-bottom-0 ait-left-0 ait-top-1/2 ait-left-1/2 ait-right-1/2 ait-bottom-1/2 ait-translate-x-[-100%] ait-translate-y-[-100%] ait-translate-x-[-120%] ait-translate-y-[-120%]"></div></li></div></div></div></div></div><div class="ait-flex ait-relative ait-items-end ait-justify-between"><div class="ait-w-full ait-text-center ait-pr-3"><button type="button" data-ait-dropdown-toggle="ait-make-a-review" class="ait-flex-col ait-text-[11px] ait-text-[var(--ait-link-color)] hover:ait-text-neutral-700 dark:hover:ait-text-neutral-100">Make a Review &amp; Earn Credit <span class="ait-text-red-600 ait-text-[10px]">❤</span></button></div></div></div><!----><!----><!----><!----><!----><!----><div class="ait-switchbar ait-w-[60px] ait-min-w-[60px] ait-bg-[var(--ait-switchbar-bg-color)] ait-py-2 ait-flex ait-flex-col ait-items-center ait-gap-4 ait-h-full ait-flex-grow ait-overflow-x-hidden" style="box-shadow: none;"><div><div class="ait-w-8 ait-h-8 ait-flex ait-items-center ait-justify-center ait-rounded-lg ait-cursor-pointer text-[var(--ait-secondary-text-color)] hover:bg-[var(--ait-switchbar-btn-hover-bg-color)] !w-[30px] !h-[30px]"><span><svg class="ait-w-4.5 ait-h-4.5 ait-collapse_sidebar_icon" aria-hide="true" focusable="false" role="img" viewBox="0 0 16 16" width="16" fill="currentColor" style="display: inline-block; user-select: none; vertical-align: text-bottom; overflow: visible;"> <path d="M6.823 7.823a.25.25 0 0 1 0 .354l-2.396 2.396A.25.25 0 0 1 4 10.396V5.604a.25.25 0 0 1 .427-.177Z"></path> <path d="M1.75 0h12.5C15.216 0 16 .784 16 1.75v12.5A1.75 1.75 0 0 1 14.25 16H1.75A1.75 1.75 0 0 1 0 14.25V1.75C0 .784.784 0 1.75 0ZM1.5 1.75v12.5c0 .138.112.25.25.25H9.5v-13H1.75a.25.25 0 0 0-.25.25ZM11 14.5h3.25a.25.25 0 0 0 .25-.25V1.75a.25.25 0 0 0-.25-.25H11Z"></path> </svg></span></div></div><div class="ait-flex ait-flex-col ait-gap-2 ait-justify-center"><div class="ait-switchbar-tab-item ait-rounded-lg ait-p-2 ait-cursor-pointer ait-arc-edge ait-flex ait-flex-col ait-items-center  active"><span><span><svg class="ait-w-5 ait-h-5 ait-chat_icon" viewBox="0 0 31 32" version="1.1" xmlns="http://www.w3.org/2000/svg"> <g stroke="none" stroke-width="1" fill="none" fill-rule="evenodd" sketch:type="MSPage"> <g sketch:type="MSLayerGroup" transform="translate(-259.000000, -257.000000)" fill="currentColor"> <path d="M265.5,267 C266.329,267 267,267.672 267,268.5 C267,269.329 266.329,270 265.5,270 C264.671,270 264,269.329 264,268.5 C264,267.672 264.671,267 265.5,267 L265.5,267 Z M271.5,267 C272.329,267 273,267.672 273,268.5 C273,269.329 272.329,270 271.5,270 C270.671,270 270,269.329 270,268.5 C270,267.672 270.671,267 271.5,267 L271.5,267 Z M277.5,267 C278.329,267 279,267.672 279,268.5 C279,269.329 278.329,270 277.5,270 C276.671,270 276,269.329 276,268.5 C276,267.672 276.671,267 277.5,267 L277.5,267 Z M268.637,279.736 C269.414,279.863 271.181,280 272,280 C279.18,280 284,274.657 284,268.375 C284,262.093 277.977,257 272,257 C264.811,257 259,262.093 259,268.375 C259,272.015 260.387,275.104 263,277.329 L263,283 L268.637,279.736 L268.637,279.736 Z M285.949,266.139 L286,267 C286.008,267.817 286,267.742 286,268.5 C286,276.475 279.716,282 271,282 L268,282 C270.38,284.328 273.149,285.75 277,285.75 C277.819,285.75 278.618,285.676 279.395,285.549 L285,289 L285,283.329 C288.04,281.246 290,278.015 290,274.375 C290,271.131 288.439,268.211 285.949,266.139 L285.949,266.139 Z" id="ait-comments" sketch:type="MSShapeGroup"></path> </g> </g> </svg></span></span><span class="ait-pt-2 ait-text-[10px]">Chat</span></div><div class="ait-switchbar-tab-item ait-rounded-lg ait-p-2 ait-cursor-pointer ait-arc-edge ait-flex ait-flex-col ait-items-center"><span><span><svg class="ait-w-5 ait-h-5 ait-ask_icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 256 256"><rect width="256" height="256" fill="none"></rect><path fill="currentColor" d="M225.86,102.82c-3.77-3.94-7.67-8-9.14-11.57-1.36-3.27-1.44-8.69-1.52-13.94-.15-9.76-.31-20.82-8-28.51s-18.75-7.85-28.51-8c-5.25-.08-10.67-.16-13.94-1.52-3.56-1.47-7.63-5.37-11.57-9.14C146.28,23.51,138.44,16,128,16s-18.27,7.51-25.18,14.14c-3.94,3.77-8,7.67-11.57,9.14C88,40.64,82.56,40.72,77.31,40.8c-9.76.15-20.82.31-28.51,8S41,67.55,40.8,77.31c-.08,5.25-.16,10.67-1.52,13.94-1.47,3.56-5.37,7.63-9.14,11.57C23.51,109.72,16,117.56,16,128s7.51,18.27,14.14,25.18c3.77,3.94,7.67,8,9.14,11.57,1.36,3.27,1.44,8.69,1.52,13.94.15,9.76.31,20.82,8,28.51s18.75,7.85,28.51,8c5.25.08,10.67.16,13.94,1.52,3.56,1.47,7.63,5.37,11.57,9.14C109.72,232.49,117.56,240,128,240s18.27-7.51,25.18-14.14c3.94-3.77,8-7.67,11.57-9.14,3.27-1.36,8.69-1.44,13.94-1.52,9.76-.15,20.82-.31,28.51-8s7.85-18.75,8-28.51c.08-5.25.16-10.67,1.52-13.94,1.47-3.56,5.37-7.63,9.14-11.57C232.49,146.28,240,138.44,240,128S232.49,109.73,225.86,102.82ZM128,192a12,12,0,1,1,12-12A12,12,0,0,1,128,192Zm8-48.72V144a8,8,0,0,1-16,0v-8a8,8,0,0,1,8-8c13.23,0,24-9,24-20s-10.77-20-24-20-24,9-24,20v4a8,8,0,0,1-16,0v-4c0-19.85,17.94-36,40-36s40,16.15,40,36C168,125.38,154.24,139.93,136,143.28Z"></path></svg></span></span><span class="ait-pt-2 ait-text-[10px]">Ask</span></div><div class="ait-switchbar-tab-item ait-rounded-lg ait-p-2 ait-cursor-pointer ait-arc-edge ait-flex ait-flex-col ait-items-center"><span><svg class="svg-inline--fa fa-magnifying-glass ait-h-5 ait-w-5" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="magnifying-glass" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M416 208c0 45.9-14.9 88.3-40 122.7L502.6 457.4c12.5 12.5 12.5 32.8 0 45.3s-32.8 12.5-45.3 0L330.7 376c-34.4 25.2-76.8 40-122.7 40C93.1 416 0 322.9 0 208S93.1 0 208 0S416 93.1 416 208zM208 352a144 144 0 1 0 0-288 144 144 0 1 0 0 288z"></path></svg></span><span class="ait-pt-2 ait-text-[10px]">Search</span></div><div class="ait-switchbar-tab-item ait-rounded-lg ait-p-2 ait-cursor-pointer ait-arc-edge ait-flex ait-flex-col ait-items-center"><span><svg class="svg-inline--fa fa-square-pen ait-h-5 ait-w-5" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="square-pen" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path class="" fill="currentColor" d="M64 32C28.7 32 0 60.7 0 96L0 416c0 35.3 28.7 64 64 64l320 0c35.3 0 64-28.7 64-64l0-320c0-35.3-28.7-64-64-64L64 32zM325.8 139.7l14.4 14.4c15.6 15.6 15.6 40.9 0 56.6l-21.4 21.4-71-71 21.4-21.4c15.6-15.6 40.9-15.6 56.6 0zM119.9 289L225.1 183.8l71 71L190.9 359.9c-4.1 4.1-9.2 7-14.9 8.4l-60.1 15c-5.5 1.4-11.2-.2-15.2-4.2s-5.6-9.7-4.2-15.2l15-60.1c1.4-5.6 4.3-10.8 8.4-14.9z"></path></svg></span><span class="ait-pt-2 ait-text-[10px]">Write</span></div><div class="ait-switchbar-tab-item ait-rounded-lg ait-p-2 ait-cursor-pointer ait-arc-edge ait-flex ait-flex-col ait-items-center"><span><svg class="svg-inline--fa fa-image ait-h-5 ait-w-5" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="image" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M0 96C0 60.7 28.7 32 64 32l384 0c35.3 0 64 28.7 64 64l0 320c0 35.3-28.7 64-64 64L64 480c-35.3 0-64-28.7-64-64L0 96zM323.8 202.5c-4.5-6.6-11.9-10.5-19.8-10.5s-15.4 3.9-19.8 10.5l-87 127.6L170.7 297c-4.6-5.7-11.5-9-18.7-9s-14.2 3.3-18.7 9l-64 80c-5.8 7.2-6.9 17.1-2.9 25.4s12.4 13.6 21.6 13.6l96 0 32 0 208 0c8.9 0 17.1-4.9 21.2-12.8s3.6-17.4-1.4-24.7l-120-176zM112 192a48 48 0 1 0 0-96 48 48 0 1 0 0 96z"></path></svg></span><span class="ait-pt-2 ait-text-[10px]">Image</span></div><div class="ait-switchbar-tab-item ait-rounded-lg ait-p-2 ait-cursor-pointer ait-arc-edge ait-flex ait-flex-col ait-items-center" data-ait-dropdown-toggle="ait-pdf-upload-modal"><span><svg class="ait-w-5 ait-h-5 ait-chat_with_file_icon" style="width: 1em; height: 1em;vertical-align: middle;fill: currentColor;overflow: hidden;" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"><path d="M486.4 1024A230.656 230.656 0 0 1 256 793.6v-614.4C256 80.384 336.384 0 435.2 0S614.4 80.384 614.4 179.2v563.2c0 70.5536-57.4464 128-128 128S358.4 812.9536 358.4 742.4v-307.2a25.6 25.6 0 0 1 51.2 0v307.2c0 42.3424 34.4576 76.8 76.8 76.8s76.8-34.4576 76.8-76.8v-563.2C563.2 108.6464 505.7536 51.2 435.2 51.2S307.2 108.6464 307.2 179.2v614.4C307.2 892.416 387.584 972.8 486.4 972.8s179.2-80.384 179.2-179.2v-358.4a25.6 25.6 0 0 1 51.2 0v358.4c0 127.0272-103.3728 230.4-230.4 230.4z" fill=""></path></svg></span><span class="ait-pt-2 ait-text-[10px]">ChatFile</span></div><div class="ait-switchbar-tab-item ait-rounded-lg ait-p-2 ait-cursor-pointer ait-arc-edge ait-flex ait-flex-col ait-items-center" data-ait-dropdown-toggle="ait-image-vision-modal"><span><svg class="svg-inline--fa fa-eye ait-h-5 ait-w-5" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="eye" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 576 512"><path class="" fill="currentColor" d="M288 32c-80.8 0-145.5 36.8-192.6 80.6C48.6 156 17.3 208 2.5 243.7c-3.3 7.9-3.3 16.7 0 24.6C17.3 304 48.6 356 95.4 399.4C142.5 443.2 207.2 480 288 480s145.5-36.8 192.6-80.6c46.8-43.5 78.1-95.4 93-131.1c3.3-7.9 3.3-16.7 0-24.6c-14.9-35.7-46.2-87.7-93-131.1C433.5 68.8 368.8 32 288 32zM144 256a144 144 0 1 1 288 0 144 144 0 1 1 -288 0zm144-64c0 35.3-28.7 64-64 64c-7.1 0-13.9-1.2-20.3-3.3c-5.5-1.8-11.9 1.6-11.7 7.4c.3 6.9 1.3 13.8 3.2 20.7c13.7 51.2 66.4 81.6 117.6 67.9s81.6-66.4 67.9-117.6c-11.1-41.5-47.8-69.4-88.6-71.1c-5.8-.2-9.2 6.1-7.4 11.7c2.1 6.4 3.3 13.2 3.3 20.3z"></path></svg></span><span class="ait-pt-2 ait-text-[10px]">Vision</span></div><div class="ait-switchbar-tab-item ait-rounded-lg ait-p-2 ait-cursor-pointer ait-arc-edge ait-flex ait-flex-col ait-items-center"><span><svg class="svg-inline--fa fa-robot ait-h-5 ait-w-5" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="robot" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 512"><path class="" fill="currentColor" d="M320 0c17.7 0 32 14.3 32 32l0 64 120 0c39.8 0 72 32.2 72 72l0 272c0 39.8-32.2 72-72 72l-304 0c-39.8 0-72-32.2-72-72l0-272c0-39.8 32.2-72 72-72l120 0 0-64c0-17.7 14.3-32 32-32zM208 384c-8.8 0-16 7.2-16 16s7.2 16 16 16l32 0c8.8 0 16-7.2 16-16s-7.2-16-16-16l-32 0zm96 0c-8.8 0-16 7.2-16 16s7.2 16 16 16l32 0c8.8 0 16-7.2 16-16s-7.2-16-16-16l-32 0zm96 0c-8.8 0-16 7.2-16 16s7.2 16 16 16l32 0c8.8 0 16-7.2 16-16s-7.2-16-16-16l-32 0zM264 256a40 40 0 1 0 -80 0 40 40 0 1 0 80 0zm152 40a40 40 0 1 0 0-80 40 40 0 1 0 0 80zM48 224l16 0 0 192-16 0c-26.5 0-48-21.5-48-48l0-96c0-26.5 21.5-48 48-48zm544 0c26.5 0 48 21.5 48 48l0 96c0 26.5-21.5 48-48 48l-16 0 0-192 16 0z"></path></svg></span><span class="ait-pt-2 ait-text-[10px]">Agent</span></div></div><div class="divider w-[70%] ait-mx-auto h-[1px] bg-[var(--ait-switchbar-btn-hover-bg-color)]"></div><div class="bottom-area ait-mt-auto ait-flex ait-flex-col ait-justify-center ait-items-center ait-gap-2 ait-mb-4"><div class="ait-flex ait-flex-col ait-w-full ait-gap-1 ait-cursor-pointer"><div class="ait-switchbar-tab-item ait-rounded-lg ait-p-1 ait-cursor-pointer ait-items-center ait-flex ait-flex-col"><span><svg class="ait-w-4 ait-h-4 ait-full_screen_icon" style="width: 1em; height: 1em;vertical-align: middle;fill: currentColor;overflow: hidden;" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg"><path d="M237.248 192H352a32 32 0 1 0 0-64H160a32 32 0 0 0-32 32v192a32 32 0 1 0 64 0v-114.752l137.36 137.36a32 32 0 1 0 45.232-45.264L237.248 192zM832 237.248V352a32 32 0 1 0 64 0V160a32 32 0 0 0-32-32H672a32 32 0 1 0 0 64h114.752l-137.36 137.36a32 32 0 1 0 45.264 45.232L832 237.248zM237.248 832H352a32 32 0 1 1 0 64H160a32 32 0 0 1-32-32V672a32 32 0 1 1 64 0v114.752l137.36-137.36a32 32 0 1 1 45.232 45.264L237.248 832zM832 786.752V672a32 32 0 1 1 64 0v192a32 32 0 0 1-32 32H672a32 32 0 1 1 0-64h114.752l-137.36-137.36a32 32 0 1 1 45.264-45.232L832 786.752z"></path></svg></span><label class="ait-cursor-pointer" style="font-size: 8px;">Full Page</label></div></div><div class="ait-flex ait-flex-col ait-w-full ait-gap-1 ait-cursor-pointer"><div class="ait-switchbar-tab-item ait-rounded-lg ait-p-1 ait-items-center ait-flex ait-flex-col ait-cursor-pointer" data-ait-dropdown-toggle="ait-invite-friends"><span><svg class="ait-w-4 ait-h-4 ait-gift_icon" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 14 14" fill="none"><g clip-path="url(#ait-clip0_11821_42642)"><path d="M2.18208 6.77174H11.8179M2.18208 6.77174C1.64991 6.77174 1.21851 6.34033 1.21851 5.80816V4.84458C1.21851 4.31241 1.64991 3.881 2.18208 3.881H11.8179C12.35 3.881 12.7814 4.31241 12.7814 4.84458V5.80816C12.7814 6.34033 12.35 6.77174 11.8179 6.77174M2.18208 6.77174L2.18208 11.5896C2.18208 12.1218 2.61349 12.5532 3.14566 12.5532H10.8543C11.3865 12.5532 11.8179 12.1218 11.8179 11.5896V6.77174M6.99998 3.881L9.31257 3.11014C9.67652 2.98882 9.96211 2.70323 10.0834 2.33927C10.401 1.38644 9.49454 0.479936 8.5417 0.797549C8.17775 0.918867 7.89216 1.20446 7.77084 1.56841L6.99998 3.881ZM6.99998 3.881L4.68739 3.11014C4.32344 2.98882 4.03784 2.70323 3.91653 2.33927C3.59891 1.38644 4.50541 0.479936 5.45825 0.797549C5.8222 0.918867 6.1078 1.20446 6.22911 1.56841L6.99998 3.881ZM6.99998 3.881V12.5532" stroke="currentColor" stroke-width="1.2"></path></g><defs><clippath id="ait-clip0_11821_42642"><rect width="14" height="14" fill="white"></rect></clippath></defs></svg></span><label class="ait-cursor-pointer ait-text-center ait-text-balance" style="font-size: 8px;">Invite &amp;
            Earn</label></div></div><div class="ait-flex ait-flex-col ait-gap-1 ait-w-full ait-cursor-pointer"><div class="ait-switchbar-tab-item ait-rounded-lg ait-p-1 ait-cursor-pointer ait-items-center ait-flex ait-flex-col ait-min-h-[36px] ait-justify-center"><svg class="svg-inline--fa fa-envelope ait-h-4 ait-w-4 aitopia-contact" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="envelope" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M48 64C21.5 64 0 85.5 0 112c0 15.1 7.1 29.3 19.2 38.4L236.8 313.6c11.4 8.5 27 8.5 38.4 0L492.8 150.4c12.1-9.1 19.2-23.3 19.2-38.4c0-26.5-21.5-48-48-48L48 64zM0 176L0 384c0 35.3 28.7 64 64 64l384 0c35.3 0 64-28.7 64-64l0-208L294.4 339.2c-22.8 17.1-54 17.1-76.8 0L0 176z"></path></svg></div></div><div class="ait-flex ait-flex-col ait-gap-1 ait-w-full ait-cursor-pointer"><div class="ait-switchbar-tab-item ait-rounded-lg ait-p-1 ait-cursor-pointer ait-items-center ait-flex ait-flex-col ait-min-h-[36px] ait-justify-center aitopia-options"><svg class="svg-inline--fa fa-gear ait-h-4 ait-w-4" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="gear" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M495.9 166.6c3.2 8.7 .5 18.4-6.4 24.6l-43.3 39.4c1.1 8.3 1.7 16.8 1.7 25.4s-.6 17.1-1.7 25.4l43.3 39.4c6.9 6.2 9.6 15.9 6.4 24.6c-4.4 11.9-9.7 23.3-15.8 34.3l-4.7 8.1c-6.6 11-14 21.4-22.1 31.2c-5.9 7.2-15.7 9.6-24.5 6.8l-55.7-17.7c-13.4 10.3-28.2 18.9-44 25.4l-12.5 57.1c-2 9.1-9 16.3-18.2 17.8c-13.8 2.3-28 3.5-42.5 3.5s-28.7-1.2-42.5-3.5c-9.2-1.5-16.2-8.7-18.2-17.8l-12.5-57.1c-15.8-6.5-30.6-15.1-44-25.4L83.1 425.9c-8.8 2.8-18.6 .3-24.5-6.8c-8.1-9.8-15.5-20.2-22.1-31.2l-4.7-8.1c-6.1-11-11.4-22.4-15.8-34.3c-3.2-8.7-.5-18.4 6.4-24.6l43.3-39.4C64.6 273.1 64 264.6 64 256s.6-17.1 1.7-25.4L22.4 191.2c-6.9-6.2-9.6-15.9-6.4-24.6c4.4-11.9 9.7-23.3 15.8-34.3l4.7-8.1c6.6-11 14-21.4 22.1-31.2c5.9-7.2 15.7-9.6 24.5-6.8l55.7 17.7c13.4-10.3 28.2-18.9 44-25.4l12.5-57.1c2-9.1 9-16.3 18.2-17.8C227.3 1.2 241.5 0 256 0s28.7 1.2 42.5 3.5c9.2 1.5 16.2 8.7 18.2 17.8l12.5 57.1c15.8 6.5 30.6 15.1 44 25.4l55.7-17.7c8.8-2.8 18.6-.3 24.5 6.8c8.1 9.8 15.5 20.2 22.1 31.2l4.7 8.1c6.1 11 11.4 22.4 15.8 34.3zM256 336a80 80 0 1 0 0-160 80 80 0 1 0 0 160z"></path></svg></div></div><div class="ait-flex ait-flex-col ait-gap-1 ait-w-full ait-cursor-pointer"><div data-ait-dropdown-toggle="ait-user-dropdown" data-placement="top-end" class="ait-switchbar-tab-item ait-rounded-lg ait-p-1 ait-cursor-pointer ait-items-center ait-flex ait-flex-col ait-min-h-[36px] ait-justify-center"><svg class="svg-inline--fa fa-user ait-h-4 ait-w-4" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="user" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path class="" fill="currentColor" d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512l388.6 0c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304l-91.4 0z"></path></svg></div></div></div></div><div id="ait-user-dropdown" class="ait-stroke ait-z-20 ait-width-full ait-hide ait-w-max ait-min-w-[180px] ait-max-w-[250px] ait-bg-white ait-divide-y ait-divide-neutral-100 ait-rounded-lg ait-shadow dark:ait-bg-neutral-900 dark:ait-divide-neutral-700"><div class="ait-p-2 ait-flex ait-flex-col ait-gap-2 ait-min-w-[240px]"><div class="ait-flex ait-items-center ait-cursor-pointer ait-rounded-lg ait-text-white ait-bg-green-700 hover:ait-opacity-90 ait-px-3 ait-py-1 ait-text-center dark:ait-bg-green-600 dark:hover:ait-bg-green-700"><div class="ait-flex ait-cursor-pointer ait-h-8 ait-w-8 ait-flex-center ait-justify-center ait-items-center"><div class="ait-relative ait-flex-shrink-0"><svg class="svg-inline--fa fa-user ait-h-4 ait-w-4" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="user" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path class="" fill="currentColor" d="M224 256A128 128 0 1 0 224 0a128 128 0 1 0 0 256zm-45.7 48C79.8 304 0 383.8 0 482.3C0 498.7 13.3 512 29.7 512l388.6 0c16.4 0 29.7-13.3 29.7-29.7C448 383.8 368.2 304 269.7 304l-91.4 0z"></path></svg></div></div><div class="ait-flex ait-flex-col ait-ml-1 aitopia-login-prefix"><div class="ait-flex ait-items-center"><div class="ait-text-sm ait-leading-5 ait-truncate ait-w-full ait-text-white aitopia-login-prefix">Log in as a user</div></div><!----></div></div><div><!----><!----><!----><div class="ait-flex ait-flex-align ait-gap-3 hover:ait-bg-[var(--ait-tab-menu-active-bg-color)] ait-rounded-lg ait-py-2 ait-px-3 ait-cursor-pointer aitopia-contact"><div class="ait-size-[16px] ait-flex-center ait-items-center"><svg class="svg-inline--fa fa-envelope ait-h-4 ait-w-4" aria-hidden="true" focusable="false" data-prefix="far" data-icon="envelope" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M64 112c-8.8 0-16 7.2-16 16l0 22.1L220.5 291.7c20.7 17 50.4 17 71.1 0L464 150.1l0-22.1c0-8.8-7.2-16-16-16L64 112zM48 212.2L48 384c0 8.8 7.2 16 16 16l384 0c8.8 0 16-7.2 16-16l0-171.8L322 328.8c-38.4 31.5-93.7 31.5-132 0L48 212.2zM0 128C0 92.7 28.7 64 64 64l384 0c35.3 0 64 28.7 64 64l0 256c0 35.3-28.7 64-64 64L64 448c-35.3 0-64-28.7-64-64L0 128z"></path></svg></div><div>Feedback</div></div><!----><!----></div></div></div></div><div><!----></div><div id="ait-invite-friends" class="ait-hide"><div tabindex="-1" aria-hide="true" class="ait-fixed !ait-z-[999999] ait-modal ait-m-0 ait-bg-[rgba(0,0,0,.5)] ait-top-0 ait-left-0 ait-bottom-0 ait-right-0 ait-w-full ait-p-4 ait-overflow-x-hidden ait-overflow-y-auto lg:ait-inset-0 h-[calc(100%)] ait-max-h-full ait-justify-center ait-flex ait-items-center" data-modal-hide=""><div class="ait-relative ait-w-full lg:ait-max-w-screen-xl ait-max-h-full"><div class="ait-relative ait-bg-white ait-rounded-lg ait-shadow dark:ait-bg-neutral-800"><div class="ait-px-6 ait-py-4 ait-border-b ait-rounded-t dark:ait-border-neutral-600"><h3 class="ait-text-base ait-font-semibold ait-text-neutral-900 lg:ait-text-lg dark:ait-text-white ait-text-center">Invite Friends &amp; Earn Credits</h3><button type="button" class="ait-absolute ait-top-3 ait-right-2.5 ait-text-neutral-400 ait-bg-transparent hover:ait-bg-neutral-200 hover:ait-text-neutral-900 ait-rounded-lg ait-text-sm ait-w-8 ait-h-8 ait-ml-auto ait-inline-flex ait-justify-center ait-items-center dark:hover:ait-bg-neutral-600 dark:hover:ait-text-white" data-modal-hide=""><svg class="ait-w-3 ait-h-3" aria-hide="true" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 14 14"><path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m1 1 6 6m0 0 6 6M7 7l6-6M7 7l-6 6"></path></svg><span class="ait-sr-only">Close modal</span></button></div><div class="ait-p-4 ait-w-full ait-text-center ait-flex ait-flex-col ait-items-center ait-gap-3"><div class="ait-w-full ait-text-start ait-p-[10px]"><span>Earn <span class="text-primary-600 font-bold">5 Fast credits &amp; 1 Advanced</span> credit for both of you and your friend.</span><span class="ait-font-bold">Earn more when you refer more!</span><div class="ait-w-full ait-px-[40px] ait-my-[30px]"><div class="ait-flex ait-items-center ait-gap-[12px]"><svg width="20" height="22" viewBox="0 0 43 40" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M22.8423 3.0436C24.885 1.06876 27.6211 -0.0242977 30.4616 0.000409932C33.302 0.0251175 36.0188 1.1656 38.0268 3.17566C40.0348 5.18565 41.1735 7.90432 41.1981 10.746C41.2228 13.5877 40.1315 16.3257 38.1588 18.3703L38.1371 18.3928L32.7165 23.8185C32.7164 23.8186 32.7165 23.8184 32.7165 23.8185C31.6186 24.9178 30.297 25.7683 28.8418 26.3117C27.3864 26.8551 25.8313 27.0789 24.2819 26.9678C22.7324 26.8568 21.2251 26.4134 19.862 25.668C18.499 24.9225 17.3122 23.8924 16.382 22.6477C15.7881 21.8528 15.9509 20.7269 16.7458 20.133C17.5407 19.539 18.6665 19.7019 19.2605 20.4967C19.8823 21.3288 20.6755 22.0172 21.5862 22.5153C22.4969 23.0133 23.5039 23.3095 24.5388 23.3837C25.5737 23.4579 26.6125 23.3084 27.5848 22.9454C28.557 22.5823 29.44 22.0142 30.1738 21.2793L35.5831 15.8647C36.8952 14.4992 37.6214 12.673 37.6049 10.7772C37.5884 8.87653 36.8268 7.05875 35.4847 5.71527C34.1426 4.37185 32.3275 3.61014 30.4303 3.59364C28.5373 3.57717 26.713 4.304 25.3488 5.61846L22.2507 8.70169C21.5473 9.40164 20.4098 9.3989 19.7098 8.69556C19.0098 7.99222 19.0126 6.85462 19.7159 6.15467L22.8423 3.0436ZM14.0283 13.2153C15.4836 12.6719 17.0388 12.4481 18.5882 12.5592C20.1376 12.6703 21.645 13.1136 23.008 13.8591C24.3711 14.6045 25.5579 15.6346 26.488 16.8793C27.082 17.6742 26.9191 18.8001 26.1243 19.3941C25.3294 19.988 24.2035 19.8252 23.6095 19.0303C22.9878 18.1982 22.1946 17.5098 21.2838 17.0117C20.3731 16.5137 19.3662 16.2176 18.3312 16.1434C17.2963 16.0692 16.2575 16.2186 15.2853 16.5817C14.3131 16.9447 13.43 17.5129 12.6962 18.2477L7.28698 23.6624C5.97482 25.0279 5.24869 26.8541 5.26515 28.7498C5.28165 30.6505 6.04327 32.4683 7.3854 33.8118C8.72747 35.1552 10.5426 35.9169 12.4397 35.9334C14.3319 35.9499 16.1554 35.2237 17.5195 33.9103L20.5976 30.829C21.2989 30.127 22.4365 30.1265 23.1385 30.8278C23.8405 31.5291 23.8411 32.6667 23.1398 33.3687L20.0279 36.4836C17.9853 38.4585 15.2489 39.5513 12.4085 39.5266C9.56802 39.5019 6.85126 38.3614 4.84322 36.3514C2.83525 34.3414 1.69659 31.6227 1.67192 28.781C1.64725 25.9393 2.73854 23.2013 4.7113 21.1567L4.73298 21.1342L10.1536 15.7085C10.1537 15.7085 10.1535 15.7086 10.1536 15.7085C11.2515 14.6092 12.573 13.7587 14.0283 13.2153Z" fill="white"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M22.8423 3.0436C24.885 1.06876 27.6211 -0.0242977 30.4616 0.000409932C33.302 0.0251175 36.0188 1.1656 38.0268 3.17566C40.0348 5.18565 41.1735 7.90432 41.1981 10.746C41.2228 13.5877 40.1315 16.3257 38.1588 18.3703L38.1371 18.3928L32.7165 23.8185C32.7164 23.8186 32.7165 23.8184 32.7165 23.8185C31.6186 24.9178 30.297 25.7683 28.8418 26.3117C27.3864 26.8551 25.8313 27.0789 24.2819 26.9678C22.7324 26.8568 21.2251 26.4134 19.862 25.668C18.499 24.9225 17.3122 23.8924 16.382 22.6477C15.7881 21.8528 15.9509 20.7269 16.7458 20.133C17.5407 19.539 18.6665 19.7019 19.2605 20.4967C19.8823 21.3288 20.6755 22.0172 21.5862 22.5153C22.4969 23.0133 23.5039 23.3095 24.5388 23.3837C25.5737 23.4579 26.6125 23.3084 27.5848 22.9454C28.557 22.5823 29.44 22.0142 30.1738 21.2793L35.5831 15.8647C36.8952 14.4992 37.6214 12.673 37.6049 10.7772C37.5884 8.87653 36.8268 7.05875 35.4847 5.71527C34.1426 4.37185 32.3275 3.61014 30.4303 3.59364C28.5373 3.57717 26.713 4.304 25.3488 5.61846L22.2507 8.70169C21.5473 9.40164 20.4098 9.3989 19.7098 8.69556C19.0098 7.99222 19.0126 6.85462 19.7159 6.15467L22.8423 3.0436ZM14.0283 13.2153C15.4836 12.6719 17.0388 12.4481 18.5882 12.5592C20.1376 12.6703 21.645 13.1136 23.008 13.8591C24.3711 14.6045 25.5579 15.6346 26.488 16.8793C27.082 17.6742 26.9191 18.8001 26.1243 19.3941C25.3294 19.988 24.2035 19.8252 23.6095 19.0303C22.9878 18.1982 22.1946 17.5098 21.2838 17.0117C20.3731 16.5137 19.3662 16.2176 18.3312 16.1434C17.2963 16.0692 16.2575 16.2186 15.2853 16.5817C14.3131 16.9447 13.43 17.5129 12.6962 18.2477L7.28698 23.6624C5.97482 25.0279 5.24869 26.8541 5.26515 28.7498C5.28165 30.6505 6.04327 32.4683 7.3854 33.8118C8.72747 35.1552 10.5426 35.9169 12.4397 35.9334C14.3319 35.9499 16.1554 35.2237 17.5195 33.9103L20.5976 30.829C21.2989 30.127 22.4365 30.1265 23.1385 30.8278C23.8405 31.5291 23.8411 32.6667 23.1398 33.3687L20.0279 36.4836C17.9853 38.4585 15.2489 39.5513 12.4085 39.5266C9.56802 39.5019 6.85126 38.3614 4.84322 36.3514C2.83525 34.3414 1.69659 31.6227 1.67192 28.781C1.64725 25.9393 2.73854 23.2013 4.7113 21.1567L4.73298 21.1342L10.1536 15.7085C10.1537 15.7085 10.1535 15.7086 10.1536 15.7085C11.2515 14.6092 12.573 13.7587 14.0283 13.2153Z" fill="url(#paint0_linear_18047_3202)"></path><defs><lineargradient id="paint0_linear_18047_3202" x1="10.1416" y1="17.5048" x2="25.9524" y2="40.0917" gradientUnits="userSpaceOnUse"><stop stop-color="rgba(1, 167, 125, .9)"></stop><stop offset="1" stop-color="#60a5fa"></stop></lineargradient></defs></svg><span class="ait-text-[14px]">Refer your friend with an Invitation link</span></div><svg class="svg-inline--fa fa-arrow-down ait-w-[11px] ait-mx-[4px] ait-mt-[4px] ait-mb-[10px]" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-down" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path class="" fill="currentColor" d="M169.4 470.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 370.8 224 64c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 306.7L54.6 265.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"></path></svg><div class="ait-flex ait-items-center ait-gap-[12px]"><svg width="18" height="19" viewBox="0 0 38 39" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M11.8795 10.3401C11.8795 6.79968 14.7411 3.84276 18.3761 3.84276C22.011 3.84276 24.8727 6.79968 24.8727 10.3401C24.8727 13.8804 22.011 16.8374 18.3761 16.8374C18.1848 16.8374 18.0003 16.8673 17.8267 16.9229C15.64 17.0126 13.4838 17.502 11.4584 18.3704C9.20642 19.336 7.16019 20.7513 5.43658 22.5354C3.71298 24.3196 2.34573 26.4377 1.41292 28.7689C0.480111 31.1 0 33.5985 0 36.1217C0 37.1828 0.831034 38.043 1.85617 38.043H35.2672C36.2923 38.043 37.1233 37.1828 37.1233 36.1217C37.1233 33.5985 36.6432 31.1 35.7104 28.7689C34.7776 26.4377 33.4104 24.3196 31.6867 22.5354C30.9619 21.7851 29.7866 21.7851 29.0617 22.5354C28.3368 23.2858 28.3368 24.5023 29.0617 25.2527C30.4406 26.68 31.5344 28.3745 32.2807 30.2394C32.7889 31.5096 33.1292 32.8419 33.2945 34.2003L3.8288 34.2003C3.99413 32.8419 4.3344 31.5096 4.84267 30.2394C5.58892 28.3745 6.68271 26.68 8.0616 25.2527C9.44049 23.8254 11.0775 22.6931 12.8791 21.9207C14.6807 21.1482 16.6116 20.7506 18.5617 20.7506C18.7692 20.7506 18.9688 20.7154 19.1551 20.6503C24.3899 20.2483 28.585 15.8289 28.585 10.3401C28.585 4.58142 23.9673 0 18.3761 0C12.7848 0 8.16717 4.58142 8.16717 10.3401C8.16717 11.4012 8.9982 12.2614 10.0233 12.2614C11.0485 12.2614 11.8795 11.4012 11.8795 10.3401Z" fill="white"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M11.8795 10.3401C11.8795 6.79968 14.7411 3.84276 18.3761 3.84276C22.011 3.84276 24.8727 6.79968 24.8727 10.3401C24.8727 13.8804 22.011 16.8374 18.3761 16.8374C18.1848 16.8374 18.0003 16.8673 17.8267 16.9229C15.64 17.0126 13.4838 17.502 11.4584 18.3704C9.20642 19.336 7.16019 20.7513 5.43658 22.5354C3.71298 24.3196 2.34573 26.4377 1.41292 28.7689C0.480111 31.1 0 33.5985 0 36.1217C0 37.1828 0.831034 38.043 1.85617 38.043H35.2672C36.2923 38.043 37.1233 37.1828 37.1233 36.1217C37.1233 33.5985 36.6432 31.1 35.7104 28.7689C34.7776 26.4377 33.4104 24.3196 31.6867 22.5354C30.9619 21.7851 29.7866 21.7851 29.0617 22.5354C28.3368 23.2858 28.3368 24.5023 29.0617 25.2527C30.4406 26.68 31.5344 28.3745 32.2807 30.2394C32.7889 31.5096 33.1292 32.8419 33.2945 34.2003L3.8288 34.2003C3.99413 32.8419 4.3344 31.5096 4.84267 30.2394C5.58892 28.3745 6.68271 26.68 8.0616 25.2527C9.44049 23.8254 11.0775 22.6931 12.8791 21.9207C14.6807 21.1482 16.6116 20.7506 18.5617 20.7506C18.7692 20.7506 18.9688 20.7154 19.1551 20.6503C24.3899 20.2483 28.585 15.8289 28.585 10.3401C28.585 4.58142 23.9673 0 18.3761 0C12.7848 0 8.16717 4.58142 8.16717 10.3401C8.16717 11.4012 8.9982 12.2614 10.0233 12.2614C11.0485 12.2614 11.8795 11.4012 11.8795 10.3401Z" fill="url(#paint0_linear_18047_3240)"></path><defs><lineargradient id="paint0_linear_18047_3240" x1="7.955" y1="16.8477" x2="23.2962" y2="38.2338" gradientUnits="userSpaceOnUse"><stop stop-color="rgba(1, 167, 125, .9)"></stop><stop offset="1" stop-color="#60a5fa"></stop></lineargradient></defs></svg><span class="ait-text-[14px]">Your friends sign up</span></div><svg class="svg-inline--fa fa-arrow-down ait-w-[11px] ait-mx-[4px] ait-mt-[10px] ait-mb-[3px]" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="arrow-down" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 384 512"><path class="" fill="currentColor" d="M169.4 470.6c12.5 12.5 32.8 12.5 45.3 0l160-160c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0L224 370.8 224 64c0-17.7-14.3-32-32-32s-32 14.3-32 32l0 306.7L54.6 265.4c-12.5-12.5-32.8-12.5-45.3 0s-12.5 32.8 0 45.3l160 160z"></path></svg><div class="ait-flex ait-items-center ait-gap-[12px]"><svg width="25" height="25" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg" style="max-width: 25px;"><path fill-rule="evenodd" clip-rule="evenodd" d="M11.1524 6.83074C11.1524 3.6117 13.7641 1 16.9831 1C20.2021 1 22.8138 3.6117 22.8138 6.83074V7.76822H27.9815C30.7352 7.76822 32.9662 9.99923 32.9662 12.7529V17.9206H33.9037C37.1227 17.9206 39.7344 20.5323 39.7344 23.7514C39.7344 26.9704 37.1227 29.5821 33.9037 29.5821H32.9662V34.7497C32.9662 37.5034 30.7352 39.7344 27.9815 39.7344H19.9511V35.5957C19.9511 33.9586 18.6203 32.6278 16.9831 32.6278C15.3459 32.6278 14.0151 33.9586 14.0151 35.5957V39.7344H5.98473C3.23101 39.7344 1 37.5034 1 34.7497L1.01059 26.7193H5.13867C6.77585 26.7193 8.10663 25.3885 8.10663 23.7513C8.10663 22.1141 6.77585 20.7833 5.13867 20.7833H1.00633L1.01692 12.7529C1.01692 12.7526 1.01692 12.7522 1.01692 12.7518C1.01755 10.0091 3.22096 7.76822 5.98473 7.76822H11.1524V6.83074ZM16.9831 4.20119C15.532 4.20119 14.3535 5.37967 14.3535 6.83074V10.9694H5.98473C5.00942 10.9694 4.21811 11.7567 4.21811 12.7529L4.21174 17.5822H5.13867C8.54382 17.5822 11.3078 20.3462 11.3078 23.7513C11.3078 27.1565 8.54382 29.9205 5.13867 29.9205H4.20756L4.20119 34.7497C4.20119 34.75 4.20119 34.7503 4.20119 34.7506C4.20168 35.7359 4.99928 36.5332 5.98473 36.5332H10.8139V35.5957C10.8139 32.1906 13.5779 29.4266 16.9831 29.4266C20.3882 29.4266 23.1522 32.1906 23.1522 35.5957V36.5332H27.9815C28.9672 36.5332 29.765 35.7354 29.765 34.7497V26.3809H33.9037C35.3547 26.3809 36.5332 25.2024 36.5332 23.7514C36.5332 22.3003 35.3547 21.1218 33.9037 21.1218H29.765V12.7529C29.765 11.7672 28.9672 10.9694 27.9815 10.9694H19.6126V6.83074C19.6126 5.37967 18.4342 4.20119 16.9831 4.20119Z" fill="white"></path><path fill-rule="evenodd" clip-rule="evenodd" d="M11.1524 6.83074C11.1524 3.6117 13.7641 1 16.9831 1C20.2021 1 22.8138 3.6117 22.8138 6.83074V7.76822H27.9815C30.7352 7.76822 32.9662 9.99923 32.9662 12.7529V17.9206H33.9037C37.1227 17.9206 39.7344 20.5323 39.7344 23.7514C39.7344 26.9704 37.1227 29.5821 33.9037 29.5821H32.9662V34.7497C32.9662 37.5034 30.7352 39.7344 27.9815 39.7344H19.9511V35.5957C19.9511 33.9586 18.6203 32.6278 16.9831 32.6278C15.3459 32.6278 14.0151 33.9586 14.0151 35.5957V39.7344H5.98473C3.23101 39.7344 1 37.5034 1 34.7497L1.01059 26.7193H5.13867C6.77585 26.7193 8.10663 25.3885 8.10663 23.7513C8.10663 22.1141 6.77585 20.7833 5.13867 20.7833H1.00633L1.01692 12.7529C1.01692 12.7526 1.01692 12.7522 1.01692 12.7518C1.01755 10.0091 3.22096 7.76822 5.98473 7.76822H11.1524V6.83074ZM16.9831 4.20119C15.532 4.20119 14.3535 5.37967 14.3535 6.83074V10.9694H5.98473C5.00942 10.9694 4.21811 11.7567 4.21811 12.7529L4.21174 17.5822H5.13867C8.54382 17.5822 11.3078 20.3462 11.3078 23.7513C11.3078 27.1565 8.54382 29.9205 5.13867 29.9205H4.20756L4.20119 34.7497C4.20119 34.75 4.20119 34.7503 4.20119 34.7506C4.20168 35.7359 4.99928 36.5332 5.98473 36.5332H10.8139V35.5957C10.8139 32.1906 13.5779 29.4266 16.9831 29.4266C20.3882 29.4266 23.1522 32.1906 23.1522 35.5957V36.5332H27.9815C28.9672 36.5332 29.765 35.7354 29.765 34.7497V26.3809H33.9037C35.3547 26.3809 36.5332 25.2024 36.5332 23.7514C36.5332 22.3003 35.3547 21.1218 33.9037 21.1218H29.765V12.7529C29.765 11.7672 28.9672 10.9694 27.9815 10.9694H19.6126V6.83074C19.6126 5.37967 18.4342 4.20119 16.9831 4.20119Z" fill="url(#paint0_linear_18267_3259)"></path><defs><lineargradient id="paint0_linear_18267_3259" x1="9.30023" y1="18.1538" x2="24.794" y2="40.2877" gradientUnits="userSpaceOnUse"><stop stop-color="rgba(1, 167, 125, .9)"></stop><stop offset="1" stop-color="#60a5fa"></stop></lineargradient></defs></svg><span class="ait-text-[14px]">They install extension &amp; login. You both earn credits!</span></div></div><div class="ait-copy-link-wrapper ait-flex ait-items-center ait-justify-between ait-mt-[10px] ait-cursor-not-allowed"><span class="ait-overflow-hidden ait-w-5/12 ait-whitespace-nowrap ait-text-ellipsis ait-px-[18px] ait-opacity-50"></span><button type="button" class="ait-w-7/12 ait-h-[36px] ait-rounded-full hover:ait-opacity-90 active:ait-opacity-80 ait-text-white ait-bg-gradient-to-r ait-from-[#01a77d] ait-to-[#60a5fa]" style="text-shadow: rgba(0, 0, 0, 0.3) 1px 1px 1px;"><span class="ait-text-white">Copy Invitation Link</span></button></div><div class="ait-mt-[18px] ait-text-[--ait-tab-menu-active-bg-color] ait-cursor-pointer ait-text-center"><span class="ait-cursor-[pointer]">Check Invitation Records</span></div></div></div><!----></div></div></div></div><div class="ai-el-resize"></div></div></div><div class="sidebar-container"><div id="aitopia-sidebar-opener" class="ait-cursor-pointer ait-show" style="bottom: 70px; right: 0px;"><div class="ai-opener-close ait-rounded-lg ait-bg-neutral-800 ait-text-white dark:ait-bg-neutral-200 dark:ait-text-neutral-800 ait-size-4 ait-text-center ait-align-middle ait-text-[10px] ait-font-bold"> x </div><div class="opener-logo"><span><svg class="ait-w-[45px] ait-h-[45px] ait-logo" xmlns="http://www.w3.org/2000/svg" baseProfile="tiny" viewBox="0 0 125 121.7" overflow="visible"><circle fill="#01a77d" cx="63.4" cy="61.2" r="57.8"></circle><g fill="#fff"><path d="M46.9 60.5h-.4c-1.9-.2-3.3-1.9-3.1-3.8.6-6.3 4.5-38 17.3-41.2 8.2-2 14.4 7.5 16.5 10.6 1.1 1.6.6 3.8-1 4.9s-3.8.6-4.9-1c-3.5-5.3-6.9-8.2-9-7.7-4.2 1-10 14.8-12 35.1-.2 1.7-1.7 3.1-3.4 3.1zm51.9-4.9c-.5 0-1-.1-1.4-.3-1.8-.8-2.6-2.9-1.8-4.6 2.6-5.8 3.2-10.2 1.7-11.7-3.1-3-17.8-.6-36.1 8.6-1.7.9-3.8.2-4.7-1.6-.9-1.7-.2-3.8 1.6-4.7.3-.2 8.3-4.1 17.4-7.1 13.4-4.5 22.2-4.5 26.7-.2 6.1 5.8 1.4 16.2-.1 19.6-.7 1.3-2 2-3.3 2zM88.2 89.5c-1.8 0-3.3-1.3-3.5-3.1-.2-1.9 1.1-3.7 3.1-3.9 6.3-.7 10.4-2.5 10.9-4.6 1-4.2-8.7-15.6-25.9-26.6-1.6-1-2.1-3.2-1.1-4.8s3.2-2.1 4.8-1.1c.3.2 7.8 5 15.1 11.3 10.7 9.3 15.3 16.7 13.9 22.8-1.9 8.2-13.2 9.5-16.9 10h-.4zm-25.9 18.1c-7.2 0-12.4-8.3-14.2-11.2-1-1.6-.5-3.8 1.1-4.8s3.8-.5 4.8 1.1c3.4 5.4 6.7 8.3 8.8 7.9 4.2-.9 10.3-14.5 12.9-34.8.2-1.9 2-3.3 3.9-3 1.9.2 3.3 2 3 3.9-.8 6.3-5.4 37.9-18.4 40.7-.5.1-1.2.2-1.9.2zm-25-18.1c-5.5 0-9.4-1.3-11.8-4-5.6-6.3-.1-16.3 1.6-19.5.9-1.7 3.1-2.3 4.7-1.4 1.7.9 2.3 3.1 1.4 4.7-3.1 5.6-4 9.9-2.6 11.5 2.9 3.2 17.7 1.9 36.7-5.7a3.57 3.57 0 0 1 4.6 1.9 3.57 3.57 0 0 1-1.9 4.6c-.3.1-8.6 3.5-17.9 5.8-5.9 1.4-10.8 2.1-14.8 2.1zm16.5-12.6c-.6 0-1.2-.2-1.8-.5-.3-.2-7.9-4.8-15.4-10.8-11-8.9-15.8-16.2-14.6-22.3 1.6-8.2 12.9-9.9 16.6-10.5 1.9-.3 3.7 1 4 2.9s-1 3.7-2.9 4c-6.3.9-10.3 2.8-10.7 4.9-1 4.3 9 15.3 26.6 25.8 1.7 1 2.2 3.1 1.2 4.8-.7 1.1-1.8 1.7-3 1.7z"></path><circle cx="63.8" cy="60.5" r="8.4"></circle></g></svg></span></div></div><div class="ait-fixed ait-flex-col ait-items-center ait-bg-[--ait-main-color] dark:ait-bg-[--ait-option-card-bg-color] ait-p-1.5 ait-shadow-lg ait-quick-action-container" style="bottom: 114px; right: 0px;"><li data-v-123660cf="" class="ait-relative ait-block ait-popper-container"><button class="ait-cursor-pointer ait-p-1 ait-rounded-full ait-flex ait-items-center ait-justify-center ait-border ait-transition-all"><svg class="svg-inline--fa fa-book ait-w-4 ait-h-4" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="book" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><path class="" fill="currentColor" d="M96 0C43 0 0 43 0 96L0 416c0 53 43 96 96 96l288 0 32 0c17.7 0 32-14.3 32-32s-14.3-32-32-32l0-64c17.7 0 32-14.3 32-32l0-320c0-17.7-14.3-32-32-32L384 0 96 0zm0 384l256 0 0 64L96 448c-17.7 0-32-14.3-32-32s14.3-32 32-32zm32-240c0-8.8 7.2-16 16-16l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16zm16 48l192 0c8.8 0 16 7.2 16 16s-7.2 16-16 16l-192 0c-8.8 0-16-7.2-16-16s7.2-16 16-16z"></path></svg></button><div data-v-123660cf="" class="ait-absolute ait-z-[9999999] ait-top-0 ait-transform ait--translate-x-1/2 ait-py-1 ait-px-2 ait-rounded-md ait-shadow-lg dark:ait-bg-neutral-100 ait-bg-neutral-800 ait-text-gray-900 dark:ait-text-gray-200 ait-translate-y-[-120%] ait:border-[1px] dark:ait-border-neutral-200 ait-border-neutral-300 ait-left-[0px]" style="display: none;"><div data-v-123660cf="" class="ait-text-xs ait-font-medium ait-text-gray-200 dark:ait-text-gray-800">Summarize Page</div></div><div data-v-123660cf="" class="ait-hide ait-left-0 ait-top-0 ait-bottom-0 ait-left-0 ait-top-1/2 ait-left-1/2 ait-right-1/2 ait-bottom-1/2 ait-translate-x-[-100%] ait-translate-y-[-100%] ait-translate-x-[-120%] ait-translate-y-[-120%]"></div></li></div></div><div style="display: none;"><div class="ait-mb-5 ait-max-w-[372px] ait-min-w-[360px]" id="aitopia-search-container"><div class="ait-bg-neutral-100 dark:ait-bg-neutral-900 dark:ait-text-gray-200 ait-rounded-lg ait-px-4 ait-py-3 ait-border ait-border-gray-50 dark:ait-border-neutral-700"><div class="ait-flex"><div class="ait-w-11/12 ait-flex ait-gap-2 xl:ait-gap-3 ait-items-center"><div class="ait-logo ait-flex ait-w-7/12 ait-place-items-center"><span><svg class="ait-w-7 ait-flex-initial ait-logo" xmlns="http://www.w3.org/2000/svg" baseProfile="tiny" viewBox="0 0 125 121.7" overflow="visible"><circle fill="#01a77d" cx="63.4" cy="61.2" r="57.8"></circle><g fill="#fff"><path d="M46.9 60.5h-.4c-1.9-.2-3.3-1.9-3.1-3.8.6-6.3 4.5-38 17.3-41.2 8.2-2 14.4 7.5 16.5 10.6 1.1 1.6.6 3.8-1 4.9s-3.8.6-4.9-1c-3.5-5.3-6.9-8.2-9-7.7-4.2 1-10 14.8-12 35.1-.2 1.7-1.7 3.1-3.4 3.1zm51.9-4.9c-.5 0-1-.1-1.4-.3-1.8-.8-2.6-2.9-1.8-4.6 2.6-5.8 3.2-10.2 1.7-11.7-3.1-3-17.8-.6-36.1 8.6-1.7.9-3.8.2-4.7-1.6-.9-1.7-.2-3.8 1.6-4.7.3-.2 8.3-4.1 17.4-7.1 13.4-4.5 22.2-4.5 26.7-.2 6.1 5.8 1.4 16.2-.1 19.6-.7 1.3-2 2-3.3 2zM88.2 89.5c-1.8 0-3.3-1.3-3.5-3.1-.2-1.9 1.1-3.7 3.1-3.9 6.3-.7 10.4-2.5 10.9-4.6 1-4.2-8.7-15.6-25.9-26.6-1.6-1-2.1-3.2-1.1-4.8s3.2-2.1 4.8-1.1c.3.2 7.8 5 15.1 11.3 10.7 9.3 15.3 16.7 13.9 22.8-1.9 8.2-13.2 9.5-16.9 10h-.4zm-25.9 18.1c-7.2 0-12.4-8.3-14.2-11.2-1-1.6-.5-3.8 1.1-4.8s3.8-.5 4.8 1.1c3.4 5.4 6.7 8.3 8.8 7.9 4.2-.9 10.3-14.5 12.9-34.8.2-1.9 2-3.3 3.9-3 1.9.2 3.3 2 3 3.9-.8 6.3-5.4 37.9-18.4 40.7-.5.1-1.2.2-1.9.2zm-25-18.1c-5.5 0-9.4-1.3-11.8-4-5.6-6.3-.1-16.3 1.6-19.5.9-1.7 3.1-2.3 4.7-1.4 1.7.9 2.3 3.1 1.4 4.7-3.1 5.6-4 9.9-2.6 11.5 2.9 3.2 17.7 1.9 36.7-5.7a3.57 3.57 0 0 1 4.6 1.9 3.57 3.57 0 0 1-1.9 4.6c-.3.1-8.6 3.5-17.9 5.8-5.9 1.4-10.8 2.1-14.8 2.1zm16.5-12.6c-.6 0-1.2-.2-1.8-.5-.3-.2-7.9-4.8-15.4-10.8-11-8.9-15.8-16.2-14.6-22.3 1.6-8.2 12.9-9.9 16.6-10.5 1.9-.3 3.7 1 4 2.9s-1 3.7-2.9 4c-6.3.9-10.3 2.8-10.7 4.9-1 4.3 9 15.3 26.6 25.8 1.7 1 2.2 3.1 1.2 4.8-.7 1.1-1.8 1.7-3 1.7z"></path><circle cx="63.8" cy="60.5" r="8.4"></circle></g></svg></span><div class="ait-logo-text"><div class="ait-font-bold ait-pl-1 ait-pr-2 ait-break-keep ait-text-sm">AITOPIA Sidebar</div></div></div><div class="ait-credits ait-mr-3 ait-w-5/12"><button type="button" class="ait-text-neutral-500 dark:ait-text-neutral-300 ait-border-2 ait-border-solid ait-border-[var(--ait-tab-menu-active-bg-color)] hover:ait-bg-[var(--ait-tab-menu-active-bg-color)] hover:ait-text-white ait-rounded-lg focus:ait-outline-none ait-text-xs ait-p-2 ait-text-center aitopia-ask-search">Ask AITOPIA</button></div></div><div class="ait-w-1/12 ait-flex ait-grid ait-grid-cols-1 ait-gap-3 ait-items-center"><div class="ait-switchbar-tab-item ait-gap-3 ait-place-items-end ait-rounded-lg ait-p-2 ait-cursor-pointer arc-edge aitopia-options-search"><svg class="svg-inline--fa fa-gear ait-h-4 ait-w-4" aria-hidden="true" focusable="false" data-prefix="fas" data-icon="gear" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512"><path class="" fill="currentColor" d="M495.9 166.6c3.2 8.7 .5 18.4-6.4 24.6l-43.3 39.4c1.1 8.3 1.7 16.8 1.7 25.4s-.6 17.1-1.7 25.4l43.3 39.4c6.9 6.2 9.6 15.9 6.4 24.6c-4.4 11.9-9.7 23.3-15.8 34.3l-4.7 8.1c-6.6 11-14 21.4-22.1 31.2c-5.9 7.2-15.7 9.6-24.5 6.8l-55.7-17.7c-13.4 10.3-28.2 18.9-44 25.4l-12.5 57.1c-2 9.1-9 16.3-18.2 17.8c-13.8 2.3-28 3.5-42.5 3.5s-28.7-1.2-42.5-3.5c-9.2-1.5-16.2-8.7-18.2-17.8l-12.5-57.1c-15.8-6.5-30.6-15.1-44-25.4L83.1 425.9c-8.8 2.8-18.6 .3-24.5-6.8c-8.1-9.8-15.5-20.2-22.1-31.2l-4.7-8.1c-6.1-11-11.4-22.4-15.8-34.3c-3.2-8.7-.5-18.4 6.4-24.6l43.3-39.4C64.6 273.1 64 264.6 64 256s.6-17.1 1.7-25.4L22.4 191.2c-6.9-6.2-9.6-15.9-6.4-24.6c4.4-11.9 9.7-23.3 15.8-34.3l4.7-8.1c6.6-11 14-21.4 22.1-31.2c5.9-7.2 15.7-9.6 24.5-6.8l55.7 17.7c13.4-10.3 28.2-18.9 44-25.4l12.5-57.1c2-9.1 9-16.3 18.2-17.8C227.3 1.2 241.5 0 256 0s28.7 1.2 42.5 3.5c9.2 1.5 16.2 8.7 18.2 17.8l12.5 57.1c15.8 6.5 30.6 15.1 44 25.4l55.7-17.7c8.8-2.8 18.6-.3 24.5 6.8c8.1 9.8 15.5 20.2 22.1 31.2l4.7 8.1c6.1 11 11.4 22.4 15.8 34.3zM256 336a80 80 0 1 0 0-160 80 80 0 1 0 0 160z"></path></svg></div></div></div><div class="ait-single-response" style="display: none;"><!----></div></div></div></div><textarea id="ait_clipboard" style="position: fixed; bottom: -10px; z-index: -1; height: 1px; width: 1px; font-size: 0.1px;"></textarea><!----><!----><span class="ait-min-h-[180px] ait-max-h-[180px] ait-min-h-[145px] ait-max-h-[145px] ait-min-h-[150px] ait-max-h-[150px] ait-min-h-[160px] ait-h-[160px] ait-max-h-[160px] ait-min-h-[265px] ait-h-[265px] ait-max-h-[265px] ait-hide"></span><!----></div><div data-v-135dc5aa="" class="aitopia light" nocolor=""><div data-v-135dc5aa="" class="aitopia-context-container" style="position: absolute; left: 0px; top: 0px; pointer-events: none; z-index: 2147483645;"><div data-v-135dc5aa="" style="top: 0px; left: 0px; position: absolute;"><div data-v-135dc5aa="" style="top: 135px; left: 108px; width: 76992px; height: 1px; position: absolute;"><!----><div data-v-135dc5aa="" class="aitopia-writing-btn-wrapper" id="aitopia-writing-btn" style="bottom: 14px; right: 14px; width: 16px; height: 16px; position: absolute;"><div data-v-135dc5aa="" class="ait-bg-[--ait-tab-menu-active-bg-color]" style="display: inline-block; width: 12px; height: 12px; border-radius: 16px; cursor: pointer; pointer-events: all;"><!----></div></div></div></div></div><!----><!----><!----></div><grammarly-desktop-integration data-grammarly-shadow-root="true"><template shadowrootmode="open"><style>
      div.grammarly-desktop-integration {
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        white-space: nowrap;
        border: 0;
        -moz-user-select: none;
        -webkit-user-select: none;
        -ms-user-select:none;
        user-select:none;
      }

      div.grammarly-desktop-integration:before {
        content: attr(data-content);
      }
    </style><div aria-label="grammarly-integration" role="group" tabindex="-1" class="grammarly-desktop-integration" data-content="{&quot;mode&quot;:&quot;full&quot;,&quot;isActive&quot;:true,&quot;isUserDisabled&quot;:false}"></div></template></grammarly-desktop-integration></html>
