import {
  IRenderMime
} from '@jupyterlab/rendermime-interfaces';

import {
  JSONObject
} from '@phosphor/coreutils';

import {
  Widget
} from '@phosphor/widgets';

import '../style/index.css';


/**
 * The default mime type for the extension.
 */
const MIME_TYPE = 'application/vnd.scipy2018.certificate';

/**
 * The class name added to the extension.
 */
const CLASS_NAME = 'jp-OutputWidgetcert';


/**
 * A widget for rendering cert.
 */
export
class OutputWidget extends Widget implements IRenderMime.IRenderer {
  /**
   * Construct a new output widget.
   */
  constructor(options: IRenderMime.IRendererOptions) {
    super();
    this._mimeType = options.mimeType;
    this.addClass(CLASS_NAME);
  }

  /**
   * Render cert into this widget's node.
   */
  renderModel(model: IRenderMime.IMimeModel): Promise<void> {
    let mod = model.data[this._mimeType] as JSONObject;
    let given = mod['given'];
    let ev = mod['event'];

    this.node.innerHTML = `
    <section class="cert">
  <div class="paper">
    <div class="title">Certificate</div>
    <div class="textX">${given}</div>
    <div class="textX">For mastery of JupyterLab</div>
    <div class="textX">${ev}</div>
  </div>
  <div class="medal"></div>
  <div class="ribbon1"></div>
  <div class="ribbon2"></div>
</section>
`
    
    //JSON.stringify(model.data[this._mimeType]);
    return Promise.resolve(void 0);
  }

  private _mimeType: string;
}


/**
 * A mime renderer factory for cert data.
 */
export
const rendererFactory: IRenderMime.IRendererFactory = {
  safe: true,
  mimeTypes: [MIME_TYPE],
  createRenderer: options => new OutputWidget(options)
};

console.log('CERT EXt')
const extension: IRenderMime.IExtension = {
  id: 'scipy_cert:plugin',
  rendererFactory,
  rank: 0,
  dataType: 'json',
  fileTypes: [{
      name: 'jsoncert',
      mimeTypes: [MIME_TYPE],
      extensions: ['.json', '.cert.json'],
  }],
  documentWidgetFactoryOptions: {
      name: 'CertViewer',
      primaryFileType: 'jsoncert',
      fileTypes: ['jsoncert', 'json'],
      defaultFor: ['jsoncert']
    }
};

export default extension;

