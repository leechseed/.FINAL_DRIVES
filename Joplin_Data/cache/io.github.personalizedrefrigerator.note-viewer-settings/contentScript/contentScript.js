/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ 903:
/***/ (function(__unused_webpack_module, exports) {


var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports["default"] = (_context) => {
    return {
        plugin: (_markdownIt) => __awaiter(void 0, void 0, void 0, function* () {
        }),
        assets: () => ([
            { name: './viewer.css' },
            { name: './viewer.js' },
        ]),
    };
};


/***/ })

/******/ 	});
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module is referenced by other modules so it can't be inlined
/******/ 	var __webpack_exports__ = {};
/******/ 	__webpack_modules__[903](0, __webpack_exports__);
/******/ 	exports["default"] = __webpack_exports__["default"];
/******/ 	
/******/ })()
;