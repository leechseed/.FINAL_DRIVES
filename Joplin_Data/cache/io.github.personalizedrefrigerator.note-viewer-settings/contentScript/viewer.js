/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ 921:
/***/ ((__unused_webpack_module, exports) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.savedLocationUserDataId = exports.contentScriptId = void 0;
exports.contentScriptId = 'personalizedrefrigerator-extra-viewer-settings-content-script';
exports.savedLocationUserDataId = 'extra-viewer-settings-last-location';


/***/ }),

/***/ 580:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


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
exports.setUpPagination = void 0;
const debounce_1 = __webpack_require__(164);
const makePaginated_1 = __webpack_require__(174);
let lastNoteId = '';
const paginate = (0, debounce_1.debounce)((control) => {
    var _a, _b, _c;
    let noteId = '';
    const lastPageNumber = (_b = (_a = window.paginationController) === null || _a === void 0 ? void 0 : _a.getPageNumber()) !== null && _b !== void 0 ? _b : 0;
    (_c = window.paginationController) === null || _c === void 0 ? void 0 : _c.cleanUp();
    const container = document.querySelector('#rendered-md');
    container.classList.add('-loading');
    const sendPageChange = (0, debounce_1.debounce)(() => {
        if (!noteId)
            return;
        void control.setLastLocation(noteId, paginationController.getLocation());
    }, 1000);
    window.paginationController = (0, makePaginated_1.makePaginated)(container, container, sendPageChange);
    const paginationController = window.paginationController;
    paginationController.setPageNumber(lastPageNumber);
    (() => __awaiter(void 0, void 0, void 0, function* () {
        const data = yield control.getNoteAndLocation();
        const location = data.location;
        if (data.noteId !== lastNoteId) {
            paginationController.scrollToCurrentPage();
            // Delay -- give time to render.
            requestAnimationFrame(() => {
                if (location) {
                    paginationController.setLocation(location);
                }
                paginationController.scrollToCurrentPage();
                container.classList.remove('-loading');
                noteId = data.noteId;
                lastNoteId = noteId;
            });
        }
        else {
            container.classList.remove('-loading');
            noteId = lastNoteId;
        }
    }))();
}, 100);
const setUpPagination = (control) => __awaiter(void 0, void 0, void 0, function* () {
    let paginateEnabled = (yield control.getSettings()).paginate;
    const updatePaginated = () => {
        if (paginateEnabled) {
            document.body.classList.add('paginate');
            paginate(control);
        }
        else {
            document.body.classList.remove('paginate');
        }
    };
    control.addOnSettingsChangeListener(() => __awaiter(void 0, void 0, void 0, function* () {
        var _a;
        const settings = yield control.getSettings();
        if (!settings.paginate) {
            (_a = window.paginationController) === null || _a === void 0 ? void 0 : _a.cleanUp();
            window.paginationController = null;
            paginateEnabled = false;
        }
        else if (!paginateEnabled) {
            paginateEnabled = true;
        }
        updatePaginated();
    }));
    document.addEventListener('joplin-noteDidUpdate', () => {
        updatePaginated();
    });
    updatePaginated();
});
exports.setUpPagination = setUpPagination;


/***/ }),

/***/ 957:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


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
exports.setUpToolbar = void 0;
const localization_1 = __webpack_require__(31);
const debounce_1 = __webpack_require__(164);
const makeButton_1 = __webpack_require__(485);
const makeInput_1 = __webpack_require__(221);
const showSettingsDialog = (control) => __awaiter(void 0, void 0, void 0, function* () {
    const settingsDialog = document.createElement('dialog');
    settingsDialog.classList.add('viewer-settings-dialog');
    let settings = yield control.getSettings();
    const setSettings = (newSettings) => {
        settings = Object.assign(Object.assign({}, settings), newSettings);
        control.updateSettings(settings);
    };
    const textSizeInput = (0, makeInput_1.makeInput)(settingsDialog, {
        label: 'Text size:',
        type: 'number',
        classList: [],
    });
    textSizeInput.min = '5';
    textSizeInput.max = '24';
    textSizeInput.oninput = () => {
        setSettings({
            fontSize: Number(textSizeInput.value),
        });
    };
    const viewerMaxWidth = (0, makeInput_1.makeInput)(settingsDialog, {
        label: 'Maximum width:',
        type: 'number',
        classList: [],
    });
    viewerMaxWidth.oninput = () => {
        setSettings({
            maxWidth: Number(viewerMaxWidth.value),
        });
    };
    const showReaderCheckbox = (0, makeInput_1.makeInput)(settingsDialog, {
        label: localization_1.default.label__paginate,
        type: 'checkbox',
        classList: [],
    });
    showReaderCheckbox.oninput = () => {
        setSettings({
            paginate: !!showReaderCheckbox.checked,
        });
    };
    const closeButton = (0, makeButton_1.makeButton)(settingsDialog, {
        content: localization_1.default.button__close,
        classList: ['close']
    });
    const updateControlValues = () => {
        var _a;
        textSizeInput.value = `${(_a = settings.fontSize) !== null && _a !== void 0 ? _a : 10}`;
        showReaderCheckbox.checked = settings.paginate;
        viewerMaxWidth.value = `${settings.maxWidth}`;
    };
    const settingsOnChange = control.addOnSettingsChangeListener(() => __awaiter(void 0, void 0, void 0, function* () {
        settings = yield control.getSettings();
        updateControlValues();
    }));
    updateControlValues();
    closeButton.onclick = () => {
        settingsDialog.close();
    };
    document.body.appendChild(settingsDialog);
    settingsDialog.showModal();
    settingsDialog.onclose = () => {
        settingsOnChange.remove();
        // Delay -- give time for a closing animation
        setTimeout(() => {
            settingsDialog.remove();
        }, 1000);
    };
});
const setUpToolbar = (control) => {
    const toolbar = document.createElement('div');
    toolbar.classList.add('viewer-toolbar');
    const settingsButton = (0, makeButton_1.makeButton)(toolbar, {
        title: 'Settings',
        content: '⚙️',
        classList: ['settings-button'],
    });
    settingsButton.onclick = () => {
        showSettingsDialog(control);
    };
    const applyViewerSettings = () => __awaiter(void 0, void 0, void 0, function* () {
        var _a;
        const savedScroll = control.cacheScroll();
        const settings = yield control.getSettings();
        document.documentElement.style.setProperty('--user-font-family', settings.fontFamily);
        document.documentElement.style.setProperty('--user-font-size', settings.fontSize ? `${settings.fontSize}pt` : '');
        document.documentElement.style.setProperty('--user-text-align', (_a = settings.textAlign) !== null && _a !== void 0 ? _a : '');
        if (!settings.showQuickSettings) {
            settingsButton.style.display = 'none';
        }
        else {
            settingsButton.style.display = '';
        }
        if (settings.maxWidth) {
            document.documentElement.classList.add('-custom-max-width');
            document.documentElement.style.setProperty('--user-max-width', `${Math.max(settings.maxWidth, 100)}px`);
        }
        else {
            document.documentElement.classList.remove('-custom-max-width');
            document.documentElement.style.removeProperty('--user-max-width');
        }
        if (settings.codeBlockScroll === 'scroll') {
            document.body.classList.add('-scroll-code-blocks');
        }
        else {
            document.body.classList.remove('-scroll-code-blocks');
        }
        control.restoreScroll(savedScroll);
    });
    control.addOnSettingsChangeListener((0, debounce_1.debounce)(applyViewerSettings, 500));
    applyViewerSettings();
    document.body.appendChild(toolbar);
};
exports.setUpToolbar = setUpToolbar;


/***/ }),

/***/ 636:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


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
exports.createScrollDetector = void 0;
const debounce_1 = __webpack_require__(164);
const createScrollDetector = (getScroll, onScrollEnd) => {
    let lastScroll = getScroll();
    let lastTime = performance.now();
    let velocity = 0;
    const updateState = () => {
        const nowTime = performance.now();
        if (nowTime > lastTime + 50) {
            velocity = (getScroll() - lastScroll) / (nowTime - lastTime);
            if (Math.abs(velocity) < 1e-8) {
                velocity = 0;
            }
            lastTime = nowTime;
            lastScroll = getScroll();
            return true;
        }
        return false;
    };
    const checkScrollEnd = (0, debounce_1.debounce)(() => {
        if (updateState() && velocity === 0) {
            onScrollEnd();
        }
        else {
            checkScrollEnd();
        }
    }, 100);
    return {
        onScrollUpdate: () => __awaiter(void 0, void 0, void 0, function* () {
            checkScrollEnd();
        }),
        getVelocity: () => velocity,
    };
};
exports.createScrollDetector = createScrollDetector;


/***/ }),

/***/ 164:
/***/ ((__unused_webpack_module, exports) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.debounce = void 0;
const debounce = (callback, timeout) => {
    let timeoutId = null;
    const result = (...args) => {
        if (timeoutId !== null) {
            clearTimeout(timeoutId);
        }
        timeoutId = setTimeout(() => {
            timeoutId = null;
            callback(...args);
        }, timeout);
    };
    return result;
};
exports.debounce = debounce;


/***/ }),

/***/ 485:
/***/ ((__unused_webpack_module, exports) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.makeButton = void 0;
const makeButton = (parent, options) => {
    var _a;
    const button = document.createElement('button');
    button.textContent = (_a = options.content) !== null && _a !== void 0 ? _a : '?';
    if (options.title) {
        button.title = options.title;
        button.setAttribute('aria-label', options.title);
    }
    button.classList.add(...options.classList);
    parent.appendChild(button);
    return button;
};
exports.makeButton = makeButton;


/***/ }),

/***/ 221:
/***/ ((__unused_webpack_module, exports) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.makeInput = void 0;
let idCounter = 0;
const makeInput = (parent, options) => {
    var _a;
    const input = document.createElement('input');
    input.type = options.type;
    input.value = options.value;
    input.setAttribute('placeHolder', (_a = options.placeholder) !== null && _a !== void 0 ? _a : '');
    input.classList.add(...options.classList);
    if (options.label) {
        const labelElement = document.createElement('label');
        input.id = `input-${idCounter++}`;
        labelElement.htmlFor = input.id;
        labelElement.textContent = options.label;
        const container = document.createElement('div');
        container.replaceChildren(labelElement, input);
        parent.appendChild(container);
    }
    else {
        parent.appendChild(input);
    }
    return input;
};
exports.makeInput = makeInput;


/***/ }),

/***/ 174:
/***/ ((__unused_webpack_module, exports, __webpack_require__) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.makePaginated = void 0;
const createScrollDetector_1 = __webpack_require__(636);
const debounce_1 = __webpack_require__(164);
const makeButton_1 = __webpack_require__(485);
const makeInput_1 = __webpack_require__(221);
const autoAddedClassName = 'reader-auto-added';
const makePaginated = (container, contentWrapper, onPageNumberChange) => {
    container.classList.add('paginated-element');
    const nextButton = (0, makeButton_1.makeButton)(container, {
        content: '>',
        title: 'Next',
        classList: ['reader-button', '-right', autoAddedClassName],
    });
    const prevButton = (0, makeButton_1.makeButton)(container, {
        content: '<',
        title: 'Previous',
        classList: ['reader-button', '-left', autoAddedClassName],
    });
    const pageNumberInput = (0, makeInput_1.makeInput)(container, {
        placeholder: 'Page',
        type: 'number',
        classList: ['reader-page-number', autoAddedClassName],
    });
    const getPageSize = () => {
        return container.clientWidth;
    };
    const convertScrollPositionToPageNumber = (position) => {
        return Math.ceil(position / getPageSize()) - 1;
    };
    let pageNumber = 0;
    const scrollToCurrentPage = () => {
        const target = pageNumber * getPageSize();
        if (Math.floor(container.scrollLeft) !== Math.floor(target)) {
            container.scrollTo(target, 0);
        }
    };
    const pageNumberFromCurrentScroll = () => {
        return convertScrollPositionToPageNumber(container.scrollLeft + getPageSize() / 2);
    };
    const updateControls = () => {
        const currentPageNumber = pageNumberFromCurrentScroll();
        pageNumberInput.value = `${currentPageNumber + 1}`;
        const maxPage = convertScrollPositionToPageNumber(container.scrollWidth);
        prevButton.disabled = currentPageNumber === 0;
        nextButton.disabled = currentPageNumber === maxPage;
    };
    const setPageNumber = (newPageNumber) => {
        const maxPage = convertScrollPositionToPageNumber(container.scrollWidth);
        newPageNumber = Math.max(0, Math.min(newPageNumber, maxPage));
        if (newPageNumber !== pageNumber && isFinite(newPageNumber)) {
            pageNumber = newPageNumber;
            onPageNumberChange === null || onPageNumberChange === void 0 ? void 0 : onPageNumberChange(pageNumber);
            scrollToCurrentPage();
        }
    };
    const nextPage = () => {
        setPageNumber(pageNumber + 1);
    };
    const prevPage = () => {
        setPageNumber(pageNumber - 1);
    };
    const scrollToElement = (element) => {
        if (!container.contains(element)) {
            console.log('can\'t scroll to element -- not in container');
            return;
        }
        const containerRect = container.getBoundingClientRect();
        const targetRect = element.getBoundingClientRect();
        // targetRect.left is relative to the current **viewport**. As such,
        // if the viewport is already scrolled, offset is relative to the current
        // **scroll*, and so we add to pageNumber.
        const offset = targetRect.left - containerRect.left;
        console.log('scrolling by', offset, 'page size', getPageSize());
        setPageNumber(pageNumber + Math.floor(offset / getPageSize()));
    };
    const setCurrentLocation = (location) => {
        location = Math.min(location, contentWrapper.children.length - 1);
        const target = contentWrapper.children.item(location);
        if (target) {
            scrollToElement(target);
            return target;
        }
        return null;
    };
    const getCurrentLocation = () => {
        const containerBox = container.getBoundingClientRect();
        let i = 0;
        for (const child of contentWrapper.children) {
            const childRect = child.getBoundingClientRect();
            if (getComputedStyle(child).position !== 'fixed' &&
                !child.classList.contains(autoAddedClassName) &&
                childRect.left >= containerBox.left) {
                return i;
            }
            i++;
        }
        return i;
    };
    nextButton.onclick = nextPage;
    prevButton.onclick = prevPage;
    pageNumberInput.oninput = (0, debounce_1.debounce)(() => {
        setPageNumber(parseInt(pageNumberInput.value) - 1);
    }, 250);
    requestAnimationFrame(updateControls);
    const onKeyDown = (event) => {
        if (event.defaultPrevented)
            return;
        const allowIfFocused = [container, document.body, document.documentElement];
        const canExcludeActiveElement = document.activeElement && !allowIfFocused.includes(document.activeElement);
        if (canExcludeActiveElement && (!container.contains(document.activeElement) || document.activeElement.tagName === 'INPUT')) {
            return;
        }
        let newPageNumber = pageNumber;
        if (event.code === 'ArrowRight') {
            newPageNumber++;
        }
        else if (event.code === 'ArrowLeft') {
            newPageNumber--;
        }
        if (pageNumber !== newPageNumber) {
            event.preventDefault();
            setPageNumber(newPageNumber);
        }
    };
    window.addEventListener('keydown', onKeyDown);
    let lastLocation = 0;
    const scrollEndDetector = (0, createScrollDetector_1.createScrollDetector)(() => container.scrollLeft, () => {
        setPageNumber(pageNumberFromCurrentScroll());
        scrollToCurrentPage();
        lastLocation = getCurrentLocation();
    });
    const onScroll = () => {
        scrollEndDetector.onScrollUpdate();
        updateControls();
    };
    container.addEventListener('scroll', onScroll);
    // This method is provided as a workaround -- setCurrentLocation may fail if the document is currently
    // scrolling. However, scrollLocationIntoView may unnecessarily scroll anscestors.
    const scrollLocationIntoView = (loc) => {
        var _a;
        (_a = setCurrentLocation(loc)) === null || _a === void 0 ? void 0 : _a.scrollIntoView({ block: 'end' });
    };
    const onResize = (0, debounce_1.debounce)(() => {
        // Prevent the reading location from being lost
        scrollLocationIntoView(lastLocation);
    }, 100);
    window.addEventListener('resize', onResize);
    let destroyed = false;
    const cleanUp = () => {
        if (destroyed)
            return;
        const autoAdded = document.querySelectorAll(`.${autoAddedClassName}`);
        for (const element of autoAdded) {
            element.remove();
        }
        container.classList.remove('paginated-element');
        window.removeEventListener('keydown', onKeyDown);
        window.removeEventListener('resize', onResize);
        container.removeEventListener('scroll', onScroll);
        destroyed = true;
    };
    return {
        cleanUp,
        setPageNumber: (newPageNumber) => {
            if (destroyed)
                return;
            setPageNumber(newPageNumber);
        },
        getPageNumber: () => pageNumber,
        scrollToCurrentPage,
        setLocation: setCurrentLocation,
        getLocation: getCurrentLocation,
        scrollLocationIntoView,
    };
};
exports.makePaginated = makePaginated;


/***/ }),

/***/ 799:
/***/ (function(__unused_webpack_module, exports, __webpack_require__) {


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
const constants_1 = __webpack_require__(921);
const setUpPagination_1 = __webpack_require__(580);
const setUpToolbar_1 = __webpack_require__(957);
const control = {
    setLastLocation: (noteId, location) => {
        return webviewApi.postMessage(constants_1.contentScriptId, {
            location,
            noteId,
        });
    },
    getNoteAndLocation: () => {
        return webviewApi.postMessage(constants_1.contentScriptId, 'getLocation');
    },
    getSettings: function () {
        return webviewApi.postMessage(constants_1.contentScriptId, 'getSettings');
    },
    addOnSettingsChangeListener: (listener) => {
        let removed = false;
        void (() => __awaiter(void 0, void 0, void 0, function* () {
            while (!removed) {
                yield webviewApi.postMessage(constants_1.contentScriptId, 'waitForSettingsChange');
                if (!removed) {
                    listener();
                }
            }
        }))();
        return {
            remove: () => {
                removed = true;
            },
        };
    },
    updateSettings: (settings) => {
        return webviewApi.postMessage(constants_1.contentScriptId, {
            newSettings: settings,
        });
    },
    cacheScroll: () => {
        var _a;
        if ('paginationController' in window) {
            const paginationController = window.paginationController;
            return (_a = paginationController === null || paginationController === void 0 ? void 0 : paginationController.getLocation()) !== null && _a !== void 0 ? _a : -1;
        }
        return -1;
    },
    restoreScroll: (cacheKey) => {
        if (cacheKey >= 0 && 'paginationController' in window) {
            const paginationController = window.paginationController;
            paginationController === null || paginationController === void 0 ? void 0 : paginationController.scrollLocationIntoView(cacheKey);
        }
    },
};
(0, setUpPagination_1.setUpPagination)(control);
(0, setUpToolbar_1.setUpToolbar)(control);


/***/ }),

/***/ 31:
/***/ ((__unused_webpack_module, exports) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
const defaultStrings = {
    settings__appName: 'Extra viewer settings',
    settings__description: 'Additional settings for Joplin\'s Markdown viewer.',
    setting__textAlign: 'Text alignment',
    setting__textAlign__unset: 'Unset',
    setting__textAlign__start: 'Start',
    setting__textAlign__end: 'End',
    setting__textAlign__center: 'Center',
    setting__textAlign__justify: 'Justify',
    setting__codeBlockScroll: 'Scroll or wrap codeblocks',
    setting__codeBlockScroll__scroll: 'Scroll',
    setting__codeBlockScroll__wrap: 'Wrap',
    setting__maximumWidth: 'Maximum width',
    setting__maximumWidth__description: 'Maximum width of rendered content in the note viewer. Set this to 0 to use the default.',
    setting__fontSize: 'Font size',
    setting__fontSize__description: 'Text size in points.',
    setting__fontFamily: 'Font family',
    setting__paginate: 'Paginate',
    setting__paginate__description: 'If enabled, Markdown notes are shown in a paged reading mode. In this mode, reading progress is saved and synced across devices.',
    setting__quickSettingsVisible: 'Show quick settings',
    setting__quickSettingsVisible__description: 'If enabled, shows a gear button that allows quickly changing viewer settings.',
    label__paginate: 'Paginate: ',
    button__close: 'Close',
};
const localizations = {
    en: defaultStrings,
    es: Object.assign({}, defaultStrings),
};
let localization;
const languages = [...navigator.languages];
for (const language of navigator.languages) {
    const localeSep = language.indexOf('-');
    if (localeSep !== -1) {
        languages.push(language.substring(0, localeSep));
    }
}
for (const locale of languages) {
    if (locale in localizations) {
        localization = localizations[locale];
        break;
    }
}
if (!localization) {
    console.log('No supported localization found. Falling back to default.');
    localization = defaultStrings;
}
exports["default"] = localization;


/***/ })

/******/ 	});
/************************************************************************/
/******/ 	// The module cache
/******/ 	var __webpack_module_cache__ = {};
/******/ 	
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/ 		// Check if module is in cache
/******/ 		var cachedModule = __webpack_module_cache__[moduleId];
/******/ 		if (cachedModule !== undefined) {
/******/ 			return cachedModule.exports;
/******/ 		}
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = __webpack_module_cache__[moduleId] = {
/******/ 			// no module.id needed
/******/ 			// no module.loaded needed
/******/ 			exports: {}
/******/ 		};
/******/ 	
/******/ 		// Execute the module function
/******/ 		__webpack_modules__[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/ 	
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/ 	
/************************************************************************/
/******/ 	
/******/ 	// startup
/******/ 	// Load entry module and return exports
/******/ 	// This entry module is referenced by other modules so it can't be inlined
/******/ 	var __webpack_exports__ = __webpack_require__(799);
/******/ 	exports["default"] = __webpack_exports__["default"];
/******/ 	
/******/ })()
;