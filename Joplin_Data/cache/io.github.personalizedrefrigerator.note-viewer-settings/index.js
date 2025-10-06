/******/ (() => { // webpackBootstrap
/******/ 	"use strict";
/******/ 	var __webpack_modules__ = ({

/***/ 998:
/***/ ((__unused_webpack_module, exports) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports["default"] = joplin;


/***/ }),

/***/ 143:
/***/ ((__unused_webpack_module, exports) => {


/* eslint-disable multiline-comment-style */
Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.ContentScriptType = exports.SettingStorage = exports.AppType = exports.SettingItemSubType = exports.SettingItemType = exports.ToolbarButtonLocation = exports.isContextMenuItemLocation = exports.MenuItemLocation = exports.ModelType = exports.ImportModuleOutputFormat = exports.FileSystemItem = void 0;
// =================================================================
// Interop API types
// =================================================================
var FileSystemItem;
(function (FileSystemItem) {
    FileSystemItem["File"] = "file";
    FileSystemItem["Directory"] = "directory";
})(FileSystemItem || (exports.FileSystemItem = FileSystemItem = {}));
var ImportModuleOutputFormat;
(function (ImportModuleOutputFormat) {
    ImportModuleOutputFormat["Markdown"] = "md";
    ImportModuleOutputFormat["Html"] = "html";
})(ImportModuleOutputFormat || (exports.ImportModuleOutputFormat = ImportModuleOutputFormat = {}));
var ModelType;
(function (ModelType) {
    ModelType[ModelType["Note"] = 1] = "Note";
    ModelType[ModelType["Folder"] = 2] = "Folder";
    ModelType[ModelType["Setting"] = 3] = "Setting";
    ModelType[ModelType["Resource"] = 4] = "Resource";
    ModelType[ModelType["Tag"] = 5] = "Tag";
    ModelType[ModelType["NoteTag"] = 6] = "NoteTag";
    ModelType[ModelType["Search"] = 7] = "Search";
    ModelType[ModelType["Alarm"] = 8] = "Alarm";
    ModelType[ModelType["MasterKey"] = 9] = "MasterKey";
    ModelType[ModelType["ItemChange"] = 10] = "ItemChange";
    ModelType[ModelType["NoteResource"] = 11] = "NoteResource";
    ModelType[ModelType["ResourceLocalState"] = 12] = "ResourceLocalState";
    ModelType[ModelType["Revision"] = 13] = "Revision";
    ModelType[ModelType["Migration"] = 14] = "Migration";
    ModelType[ModelType["SmartFilter"] = 15] = "SmartFilter";
    ModelType[ModelType["Command"] = 16] = "Command";
})(ModelType || (exports.ModelType = ModelType = {}));
var MenuItemLocation;
(function (MenuItemLocation) {
    MenuItemLocation["File"] = "file";
    MenuItemLocation["Edit"] = "edit";
    MenuItemLocation["View"] = "view";
    MenuItemLocation["Note"] = "note";
    MenuItemLocation["Tools"] = "tools";
    MenuItemLocation["Help"] = "help";
    /**
     * @deprecated Do not use - same as NoteListContextMenu
     */
    MenuItemLocation["Context"] = "context";
    // If adding an item here, don't forget to update isContextMenuItemLocation()
    /**
     * When a command is called from the note list context menu, the
     * command will receive the following arguments:
     *
     * - `noteIds:string[]`: IDs of the notes that were right-clicked on.
     */
    MenuItemLocation["NoteListContextMenu"] = "noteListContextMenu";
    MenuItemLocation["EditorContextMenu"] = "editorContextMenu";
    /**
     * When a command is called from a folder context menu, the
     * command will receive the following arguments:
     *
     * - `folderId:string`: ID of the folder that was right-clicked on
     */
    MenuItemLocation["FolderContextMenu"] = "folderContextMenu";
    /**
     * When a command is called from a tag context menu, the
     * command will receive the following arguments:
     *
     * - `tagId:string`: ID of the tag that was right-clicked on
     */
    MenuItemLocation["TagContextMenu"] = "tagContextMenu";
})(MenuItemLocation || (exports.MenuItemLocation = MenuItemLocation = {}));
function isContextMenuItemLocation(location) {
    return [
        MenuItemLocation.Context,
        MenuItemLocation.NoteListContextMenu,
        MenuItemLocation.EditorContextMenu,
        MenuItemLocation.FolderContextMenu,
        MenuItemLocation.TagContextMenu,
    ].includes(location);
}
exports.isContextMenuItemLocation = isContextMenuItemLocation;
var ToolbarButtonLocation;
(function (ToolbarButtonLocation) {
    /**
     * This toolbar in the top right corner of the application. It applies to the note as a whole, including its metadata.
     *
     * <span class="platform-desktop">desktop</span>
     */
    ToolbarButtonLocation["NoteToolbar"] = "noteToolbar";
    /**
     * This toolbar is right above the text editor. It applies to the note body only.
     */
    ToolbarButtonLocation["EditorToolbar"] = "editorToolbar";
})(ToolbarButtonLocation || (exports.ToolbarButtonLocation = ToolbarButtonLocation = {}));
// =================================================================
// Settings types
// =================================================================
var SettingItemType;
(function (SettingItemType) {
    SettingItemType[SettingItemType["Int"] = 1] = "Int";
    SettingItemType[SettingItemType["String"] = 2] = "String";
    SettingItemType[SettingItemType["Bool"] = 3] = "Bool";
    SettingItemType[SettingItemType["Array"] = 4] = "Array";
    SettingItemType[SettingItemType["Object"] = 5] = "Object";
    SettingItemType[SettingItemType["Button"] = 6] = "Button";
})(SettingItemType || (exports.SettingItemType = SettingItemType = {}));
var SettingItemSubType;
(function (SettingItemSubType) {
    SettingItemSubType["FilePathAndArgs"] = "file_path_and_args";
    SettingItemSubType["FilePath"] = "file_path";
    SettingItemSubType["DirectoryPath"] = "directory_path";
})(SettingItemSubType || (exports.SettingItemSubType = SettingItemSubType = {}));
var AppType;
(function (AppType) {
    AppType["Desktop"] = "desktop";
    AppType["Mobile"] = "mobile";
    AppType["Cli"] = "cli";
})(AppType || (exports.AppType = AppType = {}));
var SettingStorage;
(function (SettingStorage) {
    SettingStorage[SettingStorage["Database"] = 1] = "Database";
    SettingStorage[SettingStorage["File"] = 2] = "File";
})(SettingStorage || (exports.SettingStorage = SettingStorage = {}));
var ContentScriptType;
(function (ContentScriptType) {
    /**
     * Registers a new Markdown-It plugin, which should follow the template
     * below.
     *
     * ```javascript
     * module.exports = {
     *     default: function(context) {
     *         return {
     *             plugin: function(markdownIt, pluginOptions) {
     *                 // ...
     *             },
     *             assets: {
     *                 // ...
     *             },
     *         }
     *     }
     * }
     * ```
     *
     * See [the
     * demo](https://github.com/laurent22/joplin/tree/dev/packages/app-cli/tests/support/plugins/content_script)
     * for a simple Markdown-it plugin example.
     *
     * ## Exported members
     *
     * - The `context` argument is currently unused but could be used later on
     *   to provide access to your own plugin so that the content script and
     *   plugin can communicate.
     *
     * - The **required** `plugin` key is the actual Markdown-It plugin - check
     *   the [official doc](https://github.com/markdown-it/markdown-it) for more
     *   information.
     *
     * - Using the **optional** `assets` key you may specify assets such as JS
     *   or CSS that should be loaded in the rendered HTML document. Check for
     *   example the Joplin [Mermaid
     *   plugin](https://github.com/laurent22/joplin/blob/dev/packages/renderer/MdToHtml/rules/mermaid.ts)
     *   to see how the data should be structured.
     *
     * ## Supporting the Rich Text Editor
     *
     * Joplin's Rich Text Editor works with rendered HTML, which is converted back
     * to markdown when saving. To prevent the original markdown for your plugin from
     * being lost, Joplin needs additional metadata.
     *
     * To provide this,
     * 1. Wrap the HTML generated by your plugin in an element with class `joplin-editable`.
     *    For example,
     *    ```html
     *    <div class="joplin-editable">
     *        ...your html...
     *    </div>
     *    ```
     * 2. Add a child with class `joplin-source` that contains the original markdown that
     *    was rendered by your plugin. Include `data-joplin-source-open`, `data-joplin-source-close`,
     *    and `data-joplin-language` attributes.
     *    For example, if your plugin rendered the following code block,
     *    ````
     *    ```foo
     *    ... original source here ...
     *    ```
     *    ````
     *    then it should render to
     *    ```html
     *    <div class="joplin-editable">
     *        <pre
     *            class="joplin-source"
     *            data-joplin-language="foo"
     *            data-joplin-source-open="```foo&NewLine;"
     *            data-joplin-source-close="```"
     *        > ... original source here ... </pre>
     *        ... rendered HTML here ...
     *    </div>
     *    ```
     *
     * See [the demo](https://github.com/laurent22/joplin/tree/dev/packages/app-cli/tests/support/plugins/content_script)
     * for a complete example.
     *
     * ## Getting the settings from the renderer
     *
     * You can access your plugin settings from the renderer by calling
     * `pluginOptions.settingValue("your-setting-key')`.
     *
     * ## Posting messages from the content script to your plugin
     *
     * The application provides the following function to allow executing
     * commands from the rendered HTML code:
     *
     * ```javascript
     * const response = await webviewApi.postMessage(contentScriptId, message);
     * ```
     *
     * - `contentScriptId` is the ID you've defined when you registered the
     *   content script. You can retrieve it from the
     *   {@link ContentScriptContext | context}.
     * - `message` can be any basic JavaScript type (number, string, plain
     *   object), but it cannot be a function or class instance.
     *
     * When you post a message, the plugin can send back a `response` thus
     * allowing two-way communication:
     *
     * ```javascript
     * await joplin.contentScripts.onMessage(contentScriptId, (message) => {
     *     // Process message
     *     return response; // Can be any object, string or number
     * });
     * ```
     *
     * See {@link JoplinContentScripts.onMessage} for more details, as well as
     * the [postMessage
     * demo](https://github.com/laurent22/joplin/tree/dev/packages/app-cli/tests/support/plugins/post_messages).
     *
     * ## Registering an existing Markdown-it plugin
     *
     * To include a regular Markdown-It plugin, that doesn't make use of any
     * Joplin-specific features, you would simply create a file such as this:
     *
     * ```javascript
     * module.exports = {
     *     default: function(context) {
     *         return {
     *             plugin: require('markdown-it-toc-done-right');
     *         }
     *     }
     * }
     * ```
     */
    ContentScriptType["MarkdownItPlugin"] = "markdownItPlugin";
    /**
     * Registers a new CodeMirror plugin, which should follow the template
     * below.
     *
     * ```javascript
     * module.exports = {
     *     default: function(context) {
     *         return {
     *             plugin: function(CodeMirror) {
     *                 // ...
     *             },
     *             codeMirrorResources: [],
     *             codeMirrorOptions: {
     *                                  // ...
     *                       },
     *             assets: {
     *                 // ...
     *             },
     *         }
     *     }
     * }
     * ```
     *
     * - The `context` argument allows communicating with other parts of
     *   your plugin (see below).
     *
     * - The `plugin` key is your CodeMirror plugin. This is where you can
     *   register new commands with CodeMirror or interact with the CodeMirror
     *   instance as needed.
     *
     * - **CodeMirror 5 only**: The `codeMirrorResources` key is an array of CodeMirror resources that
     *   will be loaded and attached to the CodeMirror module. These are made up
     *   of addons, keymaps, and modes. For example, for a plugin that want's to
     *   enable clojure highlighting in code blocks. `codeMirrorResources` would
     *   be set to `['mode/clojure/clojure']`.
     *   This field is ignored on mobile and when the desktop beta editor is enabled.
     *
     * - **CodeMirror 5 only**: The `codeMirrorOptions` key contains all the
     *   [CodeMirror](https://codemirror.net/doc/manual.html#config) options
     *   that will be set or changed by this plugin. New options can alse be
     *   declared via
     *   [`CodeMirror.defineOption`](https://codemirror.net/doc/manual.html#defineOption),
     *   and then have their value set here. For example, a plugin that enables
     *   line numbers would set `codeMirrorOptions` to `{'lineNumbers': true}`.
     *
     * - Using the **optional** `assets` key you may specify **only** CSS assets
     *   that should be loaded in the rendered HTML document. Check for example
     *   the Joplin [Mermaid
     *   plugin](https://github.com/laurent22/joplin/blob/dev/packages/renderer/MdToHtml/rules/mermaid.ts)
     *   to see how the data should be structured.
     *
     * One of the `plugin`, `codeMirrorResources`, or `codeMirrorOptions` keys
     * must be provided for the plugin to be valid. Having multiple or all
     * provided is also okay.
     *
     * See also:
     * - The [demo plugin](https://github.com/laurent22/joplin/tree/dev/packages/app-cli/tests/support/plugins/codemirror_content_script)
     *   for an example of all these keys being used in one plugin.
     * - See [the editor plugin tutorial](https://joplinapp.org/help/api/tutorials/cm6_plugin)
     *   for how to develop a plugin for the mobile editor and the desktop beta markdown editor.
     *
     * ## Posting messages from the content script to your plugin
     *
     * In order to post messages to the plugin, you can use the postMessage
     * function passed to the {@link ContentScriptContext | context}.
     *
     * ```javascript
     * const response = await context.postMessage('messageFromCodeMirrorContentScript');
     * ```
     *
     * When you post a message, the plugin can send back a `response` thus
     * allowing two-way communication:
     *
     * ```javascript
     * await joplin.contentScripts.onMessage(contentScriptId, (message) => {
     *     // Process message
     *     return response; // Can be any object, string or number
     * });
     * ```
     *
     * See {@link JoplinContentScripts.onMessage} for more details, as well as
     * the [postMessage
     * demo](https://github.com/laurent22/joplin/tree/dev/packages/app-cli/tests/support/plugins/post_messages).
     *
     */
    ContentScriptType["CodeMirrorPlugin"] = "codeMirrorPlugin";
})(ContentScriptType || (exports.ContentScriptType = ContentScriptType = {}));


/***/ }),

/***/ 921:
/***/ ((__unused_webpack_module, exports) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.savedLocationUserDataId = exports.contentScriptId = void 0;
exports.contentScriptId = 'personalizedrefrigerator-extra-viewer-settings-content-script';
exports.savedLocationUserDataId = 'extra-viewer-settings-last-location';


/***/ }),

/***/ 156:
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
const api_1 = __webpack_require__(998);
const settings_1 = __webpack_require__(451);
const types_1 = __webpack_require__(143);
const constants_1 = __webpack_require__(921);
api_1.default.plugins.register({
    onStart: function () {
        return __awaiter(this, void 0, void 0, function* () {
            let lastSettings;
            let onSettingsChange = () => { };
            let contentScriptRegistered = false;
            lastSettings = yield (0, settings_1.registerSettings)((settings) => {
                lastSettings = settings;
                onSettingsChange();
            });
            yield api_1.default.contentScripts.register(types_1.ContentScriptType.MarkdownItPlugin, constants_1.contentScriptId, './contentScript/contentScript.js');
            yield api_1.default.contentScripts.onMessage(constants_1.contentScriptId, (message) => __awaiter(this, void 0, void 0, function* () {
                if (message === 'getSettings') {
                    contentScriptRegistered = true;
                    return lastSettings;
                }
                else if (message === 'waitForSettingsChange') {
                    return new Promise(resolve => {
                        let lastOnSettingsChange = onSettingsChange;
                        onSettingsChange = () => {
                            onSettingsChange = () => { };
                            lastOnSettingsChange();
                            resolve(lastSettings);
                        };
                    });
                }
                const selectedNoteId = (yield api_1.default.workspace.selectedNoteIds())[0];
                if (message === 'getLocation') {
                    if (!selectedNoteId) {
                        console.log('no selected note');
                        return 0;
                    }
                    const data = yield api_1.default.data.userDataGet(types_1.ModelType.Note, selectedNoteId, constants_1.savedLocationUserDataId);
                    console.log('getloc', data);
                    return {
                        location: data || 0,
                        noteId: selectedNoteId,
                    };
                }
                else if (typeof message === 'object' && 'location' in message && 'noteId' in message) {
                    if (!selectedNoteId || message.noteId !== selectedNoteId)
                        return;
                    yield api_1.default.data.userDataSet(types_1.ModelType.Note, selectedNoteId, constants_1.savedLocationUserDataId, message.location);
                }
                else if (typeof message === 'object' && 'newSettings' in message) {
                    const newSettings = message.newSettings;
                    yield api_1.default.settings.setValue('fontFamily', `${newSettings.fontFamily}`);
                    yield api_1.default.settings.setValue('fontSize', Number(newSettings.fontSize));
                    yield api_1.default.settings.setValue('maxWidth', Number(newSettings.maxWidth));
                    yield api_1.default.settings.setValue('paginate', !!newSettings.paginate);
                }
                else {
                    console.warn('unknown message', message);
                }
            }));
        });
    },
});


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


/***/ }),

/***/ 451:
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
exports.registerSettings = void 0;
const api_1 = __webpack_require__(998);
const types_1 = __webpack_require__(143);
const types_2 = __webpack_require__(613);
const localization_1 = __webpack_require__(31);
const isMobile_1 = __webpack_require__(790);
const registerSettings = (applySettings) => __awaiter(void 0, void 0, void 0, function* () {
    const sectionName = 'viewer-extended-options';
    yield api_1.default.settings.registerSection(sectionName, {
        label: localization_1.default.settings__appName,
        description: localization_1.default.settings__description,
        iconName: 'fas fa-file-alt',
    });
    const defaultSettingOptions = {
        section: sectionName,
        public: true,
        type: types_1.SettingItemType.Bool,
        storage: types_1.SettingStorage.File,
    };
    const onMobile = yield (0, isMobile_1.isMobile)();
    const settingsSpec = {
        fontFamily: Object.assign(Object.assign({}, defaultSettingOptions), { type: types_1.SettingItemType.String, value: '', 
            // font_family was added after the types were last updated
            subType: 'font_family', label: localization_1.default.setting__fontFamily }),
        fontSize: Object.assign(Object.assign({}, defaultSettingOptions), { type: types_1.SettingItemType.Int, value: 12, minimum: 8, maximum: 30, label: localization_1.default.setting__fontSize, description: localization_1.default.setting__fontSize__description }),
        maxWidth: Object.assign(Object.assign({}, defaultSettingOptions), { type: types_1.SettingItemType.Int, value: 0, minimum: 0, maximum: 1000, label: localization_1.default.setting__maximumWidth, description: localization_1.default.setting__maximumWidth__description }),
        textAlign: Object.assign(Object.assign({}, defaultSettingOptions), { type: types_1.SettingItemType.String, value: '', isEnum: true, label: localization_1.default.setting__textAlign, options: {
                'unset': localization_1.default.setting__textAlign__unset,
                'start': localization_1.default.setting__textAlign__start,
                'end': localization_1.default.setting__textAlign__end,
                'center': localization_1.default.setting__textAlign__center,
                'justify': localization_1.default.setting__textAlign__justify,
            } }),
        codeBlockScroll: Object.assign(Object.assign({}, defaultSettingOptions), { type: types_1.SettingItemType.String, value: onMobile ? types_2.CodeBlockScrollMode.Wrap : types_2.CodeBlockScrollMode.Scroll, isEnum: true, label: localization_1.default.setting__codeBlockScroll, options: {
                [types_2.CodeBlockScrollMode.Scroll]: localization_1.default.setting__codeBlockScroll__scroll,
                [types_2.CodeBlockScrollMode.Wrap]: localization_1.default.setting__codeBlockScroll__wrap,
            } }),
        paginate: Object.assign(Object.assign({}, defaultSettingOptions), { value: onMobile, label: localization_1.default.setting__paginate, description: localization_1.default.setting__paginate__description }),
        showQuickSettings: Object.assign(Object.assign({}, defaultSettingOptions), { value: true, label: localization_1.default.setting__quickSettingsVisible, description: localization_1.default.setting__quickSettingsVisible__description }),
    };
    const readSettings = () => __awaiter(void 0, void 0, void 0, function* () {
        const result = {};
        for (const key in settingsSpec) {
            result[key] = yield api_1.default.settings.value(key);
        }
        return result;
    });
    yield api_1.default.settings.registerSettings(settingsSpec);
    yield api_1.default.settings.onChange(() => __awaiter(void 0, void 0, void 0, function* () {
        applySettings(yield readSettings());
    }));
    const settings = yield readSettings();
    applySettings(settings);
    return settings;
});
exports.registerSettings = registerSettings;


/***/ }),

/***/ 613:
/***/ ((__unused_webpack_module, exports) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
exports.CodeBlockScrollMode = void 0;
var CodeBlockScrollMode;
(function (CodeBlockScrollMode) {
    CodeBlockScrollMode["Scroll"] = "scroll";
    CodeBlockScrollMode["Wrap"] = "wrap";
})(CodeBlockScrollMode || (exports.CodeBlockScrollMode = CodeBlockScrollMode = {}));


/***/ }),

/***/ 790:
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
exports.isMobile = void 0;
const api_1 = __webpack_require__(998);
const isMobile = () => __awaiter(void 0, void 0, void 0, function* () {
    try {
        return (yield api_1.default.versionInfo()).platform === 'mobile';
    }
    catch (e) {
        console.warn('Error checking if on mobile:', e);
        return false;
    }
});
exports.isMobile = isMobile;


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
/******/ 	var __webpack_exports__ = __webpack_require__(156);
/******/ 	
/******/ })()
;