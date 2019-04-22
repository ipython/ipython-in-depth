# Exercise 5: Extensions

Remove all the sticky notes from your screen :-) and attempt the following.
These are _guidelines_, feel free to ere on the side of workflow and
options that suits _you_ if you find them best.

Keep in mind, if something is not intuitive, or not in the place you expected it, write
it down (for example on the red sticky note), and give it to us at the break.

## Creating a new blank extension

We will be using the cookie-cutter project to generate a basic extension. This will generate a basic extension that reads data from a `.cert.json` JSON file and displays it nicely in JupyterLab.

Open a terminal and run:

```
cookiecutter https://github.com/jupyterlab/mimerender-cookiecutter-ts
```

At the prompts, enter the following:
```
author_name []: <Your name>
author_email []: <Your email>
extension_name [myextension]: my_certificate_viewer
viewer_name [My Viewer]: Certificate Viewer
mimetype [application/vnd.my_organization.my_type]: application/vnd.jupyterlab.certificate
mimetype_name [my_type]: certificate
file_extension [.my_type]: .cert.json
Select data_format:
1 - string
2 - json
Choose from 1, 2 [1]: 2
```

## Install the extension

In the terminal, install your new extension

```
conda activate scipy18jlab
jupyter labextension install ./my_certificate_viewer
```

You can check what extensions are installed with:

```
jupyter labextension list
```

Refresh your browser to pick up the new extension javascript.

Test it out by opening the `scipy2018.cert.json` file. Right-clicking on the file should show your viewer in the 'Open with' menu, and double-clicking should open and display the file in a blank tab.

Right-click on the `scipy2018.cert.json` file and open it in the editor to change the name to your name and the event to "Scipy 2018". Notice that the extension-rendered tab updates in real-time.

## Customize the display

In order to develop our extension and have our changes appear automatically, we'll link the extension rather than just installing it. Run the following in your terminal that has the scipy18jlab environment active:

```
jupyter labextension link ./my_certificate_viewer
```

Now customize the display. Open the `my_certificate_viewer/src/index.ts` TypeScript file. Edit the `renderModel` function to replace the line that sets the `this.node.textContent` line with a bit fancier HTML:

```javascript
    this.node.innerHTML = `
    <section class="cert">
  <div class="paper">
    <div class="title">Certificate</div>
    <div class="textX">${data.given}</div>
    <div class="textX">For mastery of JupyterLab</div>
    <div class="textX">${data.event}</div>
  </div>
  <div class="medal"></div>
  <div class="ribbon1"></div>
  <div class="ribbon2"></div>
</section>
`
```

Now rebuild JupyterLab to incorporate these changes by running the following in your terminal:

```
jupyter lab build
```

Open the `scipy2018.cert.json` file again to see that things look a bit better.

## Style the display

Finally, let's style this certificate to look really nice. Add the following to
the `my_certificate_viewer/style/index.css` file:

```css
.mimerenderer-certificate .cert{
    background-color: #07618B;
    width: 350px;height: 250px;
    margin-left: 35%;margin-top: 10%;
    position: relative;
    border-radius: 20px 20px 20px 20px;
    -webkit-box-shadow: 0px 5px 10px 0px;
    -moz-box-shadow: 0px 5px 10px 0px;
    box-shadow: 0px 5px 10px 0px;
}

.mimerenderer-certificate .paper{
    position: absolute;
    width: 300px;
    height: 200px;
    background: #E0E0E0;
    left: 25px;
    top: 25px;
    border-radius: 5px 5px 5px 5px;
}

.mimerenderer-certificate .cert .medal {
    background: #C9992E;
    width: 20px;
    height: 20px;
    top: 30px;
    left: 30px;
    position: absolute;
    padding: 10px 10px 10px 10px;
    font-size: 2em;
    border-radius: 50%;
    z-index:30;
}

.mimerenderer-certificate .ribbon1 {
    width: 15px;
    height: 40px;
    background-color: #9bdbf6;
    position: absolute;
    top: 50px;
    left: 35px;
    z-index: 1;
    -webkit-transform: rotate(30deg);
    border-right: 1px solid white;
  }

.mimerenderer-certificate .ribbon2 {
    width: 15px;
    height: 40px;
    background-color: #9bdbf6;
    position: absolute;
    top: 50px;
    left: 50px;
    z-index: 1;
    -webkit-transform: rotate(150deg);
    border-right: 1px solid white;
  }

.mimerenderer-certificate .title {
  background:#E0E0E0;
  font-weight: bold;
  text-align: center;
  margin-top: 20px;
  height: 30px;
  z-index:999;
}

.mimerenderer-certificate .textX {
  z-index: 200;
  text-align: center;
  padding: 0px;
  text-align: center;
  margin-top: 20px;
 }

.mimerenderer-certificate .text2 {
  background-color: #E0E0E0;
  z-index: 200;
  padding: 0px 200px;
  text-align: center;
  margin-left: 50px;
 }

.mimerenderer-certificate .text3 {
  background-color: #B3B3B3;
  z-index: 200;
  padding: 0px 200px;
  text-align: center;
  margin-left: 50px;
 }
 ```

 Rebuild JupyterLab and open the certificate again to see these changes.

## Install plugin

Congratulations! You can now install the extension again to wrap things up.

 ```
jupyter labextension install ./my_certificate_viewer
```

## Notebook

A mimerender extension is used to render both files and rich outputs in
notebooks. Open the `Certificate.ipynb` notebook and run it.

## More information

For more information about writing extensions, especially more substantial ones, see the [XKCD extension tutorial](http://jupyterlab.readthedocs.io/en/stable/developer/xkcd_extension_tutorial.html) in the JupyterLab documentation.