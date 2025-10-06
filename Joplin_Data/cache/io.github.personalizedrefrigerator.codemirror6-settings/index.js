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
const types_1 = __webpack_require__(613);
const types_2 = __webpack_require__(143);
let registeredSyncListeners = false;
const registerSyncStatusListeners = (onStatusChange) => __awaiter(void 0, void 0, void 0, function* () {
    if (registeredSyncListeners) {
        return;
    }
    yield api_1.default.workspace.onSyncStart(() => {
        onStatusChange(types_1.SyncStatus.Syncing);
    });
    yield api_1.default.workspace.onSyncComplete((event) => {
        onStatusChange(event.withErrors ? types_1.SyncStatus.SyncedWithErrors : types_1.SyncStatus.NotSyncing);
    });
    registeredSyncListeners = true;
});
api_1.default.plugins.register({
    onStart: function () {
        return __awaiter(this, void 0, void 0, function* () {
            let lastSettings;
            let contentScriptRegistered = false;
            let syncStatus = types_1.SyncStatus.NotSyncing;
            let onSyncStatusChange = () => { };
            lastSettings = yield (0, settings_1.registerSettings)((settings) => {
                lastSettings = settings;
                // Calling editor.execCommand before a content script is registered can cause
                // errors to be logged.
                if (contentScriptRegistered) {
                    try {
                        api_1.default.commands.execute('editor.execCommand', {
                            name: 'cm6-extended-settings-update',
                            args: [settings],
                        });
                    }
                    catch (error) {
                        console.info('Failed to load settings. On mobile, this can happen if the editor is not currently open. Error: ', error);
                    }
                }
                if (settings.syncIndicator && settings.syncIndicator !== types_1.SyncIndicatorMode.NotShown) {
                    void registerSyncStatusListeners((newStatus) => {
                        syncStatus = newStatus;
                        onSyncStatusChange();
                    });
                }
            });
            const contentScriptId = 'cm6-extended-settings';
            yield api_1.default.contentScripts.register(types_2.ContentScriptType.CodeMirrorPlugin, contentScriptId, './contentScript/contentScript.js');
            yield api_1.default.contentScripts.onMessage(contentScriptId, (message) => __awaiter(this, void 0, void 0, function* () {
                if (typeof message === 'object' && 'type' in message) {
                    if (message.type === 'renderMarkup' && 'markup' in message) {
                        if (typeof message.markup !== 'string') {
                            throw new Error(`Invalid markup type in message: ${typeof message.markup}`);
                        }
                        const markdown = 1;
                        const rendered = yield api_1.default.commands.execute('renderMarkup', markdown, message.markup);
                        return rendered;
                    }
                    else if (message.type === 'openUrl') {
                        if (!('url' in message) || typeof message.url !== 'string') {
                            throw new Error('Message is missing URL property or URL is not a string.');
                        }
                        return api_1.default.commands.execute('openItem', message.url);
                    }
                }
                else if (message === 'getSettings') {
                    contentScriptRegistered = true;
                    return lastSettings;
                }
                else if (message === 'getSyncStatus') {
                    return syncStatus;
                }
                else if (message === 'awaitSyncStatusChanged') {
                    return new Promise(resolve => {
                        let priorCallback = onSyncStatusChange;
                        onSyncStatusChange = () => {
                            resolve();
                            // Remove this listener, allow other listeners to run.
                            onSyncStatusChange = priorCallback;
                            priorCallback();
                        };
                    });
                }
                else if (message === 'sync') {
                    void api_1.default.commands.execute('synchronize');
                    return null;
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
    settings__appName: 'Extra editor settings',
    settings__description: 'Additional settings for Joplin\'s beta and mobile Markdown editors.',
    setting__showLineNumber: 'Show line numbers',
    setting__enableCodeFolding: 'Enable code folding',
    setting__enableAutocomplete: 'Enable autocomplete',
    setting__highlightLineGutter: 'Highlight the gutter for the active line',
    setting__highlightLineGutter__description: 'Requires "show line numbers" to be enabled.',
    setting__highlightActiveLine: 'Highlight active line',
    setting__highlightSpaces: 'Highlight spaces',
    setting__highlightTrailingSpaces: 'Highlight trailing spaces',
    setting__highlightSelectionMatches: 'Highlight selection matches',
    setting__bracketMatching: 'Highlight matching brackets',
    setting__showGridPattern: 'Show background grid pattern',
    setting__showLinkTooltip: 'Show link tooltip',
    setting__showLinkTooltip__description: 'Shows tooltips that allow opening links under the cursor',
    setting__showWordCount: 'Show word count',
    setting__showVisualSyncIndicator: 'Show visual sync indicator',
    setting__showVisualSyncIndicator__description: 'Shows the sync status in the Markdown editor.',
    setting__editorMaximumWidth: 'Editor maximum width',
    setting__editorMaximumWidth__description: 'Setting this to a positive number (e.g. 600) centers the editor and prevents it from having a width larger than this size. Set this to "none" for the editor to fill the screen.',
    setting__editorMaximumWidth__none: 'None',
    setting__textDirection: 'Text direction',
    setting__textDirection__description: 'Overrides the default direction of text in the CodeMirror editor. For most users, this should be set to "auto".',
    setting__textDirection__auto: 'Auto',
    setting__textDirection__leftToRight: 'Left-to-right',
    setting__textDirection__rightToLeft: 'Right-to-left',
    setting__showVisualSyncIndicator__textual: 'With text',
    setting__showVisualSyncIndicator__icon: 'With an icon',
    setting__hideMarkdown: 'Hide Markdown',
    setting__hideMarkdown__description: 'Hides/replaces certain Markdown characters when the cursor is on a different line.\n\nWhen set to "Some", only some Markup is rendered. When set to "More", somewhat more Markup is rendered, though may not be rendered correctly.',
    setting__hideMarkdown__none: 'None',
    setting__hideMarkdown__some: 'Some',
    setting__hideMarkdown__more: 'More (experimental)',
    sync_status__not_syncing: 'Not syncing',
    sync_status__syncing: 'Syncing...',
    sync_status__synced_with_errors: 'Failed to sync',
    link__followUrl(url) { return `Follow link: ${url}`; },
    words: 'Words',
    yes: 'Yes',
    no: 'No',
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
const isVersionGreater_1 = __webpack_require__(34);
const registerSettings = (applySettings) => __awaiter(void 0, void 0, void 0, function* () {
    const sectionName = 'codemirror6-extended-options';
    yield api_1.default.settings.registerSection(sectionName, {
        label: localization_1.default.settings__appName,
        description: localization_1.default.settings__description,
        iconName: 'fas fa-edit',
    });
    const onMobile = yield (0, isMobile_1.isMobile)();
    const version = (yield api_1.default.versionInfo()).version;
    // Only some of the 3.2 pre-releases support the renderMarkup command.
    // For now, assume any 3.2 release supports it, since renderMarkup was added in
    // different versions on different platforms.
    const supportsExtendedRender = (0, isVersionGreater_1.default)(version, '3.2.0');
    const defaultSettingOptions = {
        section: sectionName,
        public: true,
        type: types_1.SettingItemType.Bool,
        storage: types_1.SettingStorage.File,
    };
    const settingsSpec = {
        lineNumbers: Object.assign(Object.assign({}, defaultSettingOptions), { value: true, label: localization_1.default.setting__showLineNumber }),
        codeFolding: Object.assign(Object.assign({}, defaultSettingOptions), { value: false, label: localization_1.default.setting__enableCodeFolding }),
        enableAutocomplete: Object.assign(Object.assign({}, defaultSettingOptions), { value: false, label: localization_1.default.setting__enableAutocomplete }),
        highlightActiveLineGutter: Object.assign(Object.assign({}, defaultSettingOptions), { value: true, label: localization_1.default.setting__highlightLineGutter, description: localization_1.default.setting__highlightLineGutter__description }),
        highlightActiveLine: Object.assign(Object.assign({}, defaultSettingOptions), { value: false, label: localization_1.default.setting__highlightActiveLine }),
        highlightSpaces: Object.assign(Object.assign({}, defaultSettingOptions), { value: false, label: localization_1.default.setting__highlightSpaces }),
        highlightTrailingSpaces: Object.assign(Object.assign({}, defaultSettingOptions), { value: false, label: localization_1.default.setting__highlightTrailingSpaces }),
        highlightSelectionMatches: Object.assign(Object.assign({}, defaultSettingOptions), { value: false, label: localization_1.default.setting__highlightSelectionMatches }),
        bracketMatching: Object.assign(Object.assign({}, defaultSettingOptions), { value: false, label: localization_1.default.setting__bracketMatching }),
        editorMaximumWidth: Object.assign(Object.assign({}, defaultSettingOptions), { public: onMobile, value: 'none', options: {
                ['none']: localization_1.default.setting__editorMaximumWidth__none,
                ['300px']: '300 (small)',
                ['400px']: '400',
                ['500px']: '500',
                ['600px']: '600',
                ['800px']: '800',
                ['1000px']: '1000',
                ['1500px']: '1500 (large)',
            }, type: types_1.SettingItemType.String, isEnum: true, label: localization_1.default.setting__editorMaximumWidth, description: localization_1.default.setting__editorMaximumWidth__description }),
        gridPattern: Object.assign(Object.assign({}, defaultSettingOptions), { value: false, label: localization_1.default.setting__showGridPattern }),
        wordCount: Object.assign(Object.assign({}, defaultSettingOptions), { value: false, label: localization_1.default.setting__showWordCount }),
        syncIndicator: Object.assign(Object.assign({}, defaultSettingOptions), { type: types_1.SettingItemType.String, value: types_2.SyncIndicatorMode.NotShown, label: localization_1.default.setting__showVisualSyncIndicator, description: localization_1.default.setting__showVisualSyncIndicator__description, isEnum: true, options: {
                [types_2.SyncIndicatorMode.NotShown]: localization_1.default.no,
                [types_2.SyncIndicatorMode.Text]: localization_1.default.setting__showVisualSyncIndicator__textual,
                [types_2.SyncIndicatorMode.Icon]: localization_1.default.setting__showVisualSyncIndicator__icon,
            } }),
        hideMarkdown: Object.assign(Object.assign({}, defaultSettingOptions), { type: types_1.SettingItemType.String, value: types_2.HideMarkdownMode.None, label: localization_1.default.setting__hideMarkdown, description: localization_1.default.setting__hideMarkdown__description, isEnum: true, options: Object.assign({ [types_2.HideMarkdownMode.None]: localization_1.default.setting__hideMarkdown__none, [types_2.HideMarkdownMode.Some]: localization_1.default.setting__hideMarkdown__some }, (supportsExtendedRender ? {
                [types_2.HideMarkdownMode.More]: localization_1.default.setting__hideMarkdown__more,
            } : {})) }),
        showLinkTooltip: Object.assign(Object.assign({}, defaultSettingOptions), { value: false, label: localization_1.default.setting__showLinkTooltip, description: localization_1.default.setting__showLinkTooltip__description }),
        textDirection: Object.assign(Object.assign({}, defaultSettingOptions), { type: types_1.SettingItemType.String, advanced: true, value: types_2.TextDirection.Auto, label: localization_1.default.setting__textDirection, description: localization_1.default.setting__textDirection__description, isEnum: true, options: {
                [types_2.TextDirection.Auto]: localization_1.default.setting__textDirection__auto,
                [types_2.TextDirection.LeftToRight]: localization_1.default.setting__textDirection__leftToRight,
                [types_2.TextDirection.RightToLeft]: localization_1.default.setting__textDirection__rightToLeft,
            } }),
    };
    const readSettings = () => __awaiter(void 0, void 0, void 0, function* () {
        var _a;
        const result = {};
        for (const key in settingsSpec) {
            result[key] = (_a = (yield api_1.default.settings.value(key))) !== null && _a !== void 0 ? _a : true;
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
exports.SyncStatus = exports.HideMarkdownMode = exports.SyncIndicatorMode = exports.TextDirection = void 0;
var TextDirection;
(function (TextDirection) {
    TextDirection["Auto"] = "auto";
    TextDirection["LeftToRight"] = "ltr";
    TextDirection["RightToLeft"] = "rtl";
})(TextDirection || (exports.TextDirection = TextDirection = {}));
var SyncIndicatorMode;
(function (SyncIndicatorMode) {
    SyncIndicatorMode["NotShown"] = "not-shown";
    SyncIndicatorMode["Text"] = "text";
    SyncIndicatorMode["Icon"] = "icon";
})(SyncIndicatorMode || (exports.SyncIndicatorMode = SyncIndicatorMode = {}));
var HideMarkdownMode;
(function (HideMarkdownMode) {
    HideMarkdownMode["None"] = "none";
    HideMarkdownMode["Some"] = "some";
    HideMarkdownMode["More"] = "more";
})(HideMarkdownMode || (exports.HideMarkdownMode = HideMarkdownMode = {}));
var SyncStatus;
(function (SyncStatus) {
    SyncStatus["NotSyncing"] = "not-syncing";
    SyncStatus["Syncing"] = "syncing";
    SyncStatus["SyncedWithErrors"] = "synced-with-errors";
})(SyncStatus || (exports.SyncStatus = SyncStatus = {}));


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


/***/ }),

/***/ 34:
/***/ ((__unused_webpack_module, exports) => {


Object.defineProperty(exports, "__esModule", ({ value: true }));
/**
 * Returns true iff `a` is greater than `b`, where both `a` and `b` are
 * semver versions.
 */
const isVersionGreater = (a, b) => {
    const versionRegex = /^(\d+)\.(\d+)\.(\d+)(-.*)?$/;
    const parsedVersionA = versionRegex.exec(a);
    const parsedVersionB = versionRegex.exec(b);
    if (!parsedVersionA || !parsedVersionB) {
        console.warn(`Invalid version, ${parsedVersionA} or ${parsedVersionB} (expected number.number.number).`);
        return false;
    }
    const majorA = parseInt(parsedVersionA[1]);
    const minorA = parseInt(parsedVersionA[2]);
    const patchA = parseInt(parsedVersionA[3]);
    const majorB = parseInt(parsedVersionB[1]);
    const minorB = parseInt(parsedVersionB[2]);
    const patchB = parseInt(parsedVersionB[3]);
    return (majorA > majorB ||
        (majorA === majorB && (minorA > minorB || (minorA === minorB && patchA > patchB))));
};
exports["default"] = isVersionGreater;


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