# Python Frameworks

A HTML page with curated list of Python frameworks!


[![image](static/image/screenshot.png)](https://pythonframeworks.com/)

[https://pythonframeworks.com/](https://pythonframeworks.com/)


## Contribution

#### Development Environment

Local development is supported by [`bottle.py`](https://bottlepy.org/). Fork and clone this repository, and run

```bash
$ python3 frameworks.py
```

Then visit [`http://localhost:8080/`](http://localhost:8080/).

That's it!

#### Add a Framework?

Add a Bootstrap card element, like this:
```html
<div class="col-sm-6 col-lg-3 mb-4">
    <div class="card">
        ...
    </div>
</div>
```
The `card` element would include the `name`, `link`, `logo` and `description` of the framework.
You can decarate it by using [Bootstrap Card Class](https://getbootstrap.com/docs/5.0/components/card/) with your preference.


#### Add a Category?
If you need a new category for Python frameworks, try this:

```html
<hr class="my-4">

<div class="category" id="CategoryName">
    <h3 class="mt-5 display-6">Category Name</h3>
    <p>Description of this category</p>

    <div class="row grids mt-4" data-masonry='{"percentPosition": true }'>
        <div class="col-sm-6 col-lg-3 mb-4">
            <div class="card">
                ...
            </div>
        </div>
    </div>
</div>
```

Review the update at your local, if everything looks good, then create a pull request to the `main` branch here.



## Contact

If you have any question about this opinionated list, do not hesitate to contact me [@jgujerry](https://twitter.com/jgujerry) on X (Twitter) or open an issue on GitHub.


## License

This project is released under [MIT License](LICENSE)
