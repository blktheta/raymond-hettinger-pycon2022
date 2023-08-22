[![Writing Great Unit Tests and Documentation][repo_banner_img]][repo_url]

> Crop: "The Blue Cup", Joseph DeCamp, *1909* Year, oil on canvas. [Image source.][repo_banner_url]

# Writing Great Unit Tests and Documentation

[![Python version][py_version_img]][repo_url]
[![Python style guide][py_style_guide_img]][repo_url]
[![Python code coverage][py_code_coverage_img]][repo_url]
[![Repo wiki][repo_wiki_img]][repo_wiki_url]
[![Repo license][repo_license_img]][repo_license_url]

Notes from Raymond Hettinger's *Pro tips for writing great unit tests* talk presented at PyCon Italia 2022, supplemented by David Andersson's *Writing Great Docstrings* and *Writing Great Test Documentation* articles, with the latter also being a talk presented at PyCon 2023.

The full talk by Raymond Hettinger is availbable at [YouTube][rh_pycon2022_yt], the code examples in the repo are based on the presentation code. While David Andersson's presentation is available at at [PyVideo][da_pycon2023_pv].

## ⚡️ Getting started
First, [download][py_download_url] and install **Python**. Version `3.10.12` or higher is required.

Secondly, the repo makes use of testing packages such as; **Pytest**, **Coverage**, **Hypothesis** and **Pyflakes**. It is recommended to install the packages in a virtual environment. You can install the packeges seperately by calling:
```bash
pip install packagename
```
Or make use the command below to install the packages according to the configuration file `requirements.txt`:
```bash
pip install -r requirements.txt
```
## 📖 Project wiki
Explore all feaures of the **Writing Great Unit Test and Documentation** by reading the project [Wiki][repo_wiki_url].

You will find best pracices and practical knowledge from the presentations, as well as code examples to better communicate the testing concepts.

## 🔧 Usage
Clone the repo and navigate to the project directory. To run the test call:
```bash
pytest test/test_sample_data.py test/test_math_tools.py
```
To measure the code coverage run the command:
```bash
coverage run -m pytest test/test_sample_data.py test/test_math_tools.py
```
And to export the report to html run the command:
```bash
coverage html
```

The code is written with intention to teach about testing concepts and include several `docstrings` explaining the steps taken.

## ⭐️ Project assistance
If you want to say **thank you** or/and support a lone developers journey:

- Add a [GitHub Star][repo_url] to the project.
- Reach out to [Blk Theta][author].

## ⚠️ License

[`Writing Great Unit Test and Documentation`][repo_url] is free and open-source software licensed under the [MIT License][repo_license_url]. All designs were created by [Blk Theta][author] and distributed under Creative Commons license (CC BY-NC-SA 4.0 International).

<!--Python-->
[py_version_img]: https://img.shields.io/badge/Python-3.10.12-yellow?style=for-the-badge&logo=none
[py_style_guide_img]: https://img.shields.io/badge/Style_guide-PEP8-blue?style=for-the-badge&logo=none
[py_code_coverage_img]: https://img.shields.io/badge/Code_coverage-95%25-success?style=for-the-badge&logo=none
[py_download_url]: https://www.python.org/downloads/

<!-- Repository -->
[repo_url]: https://github.com/blktheta/raymond-hettinger-pycon2022
[repo_banner_url]: https://upload.wikimedia.org/wikipedia/commons/f/fd/DeCamp_Joseph_The_Blue_Cup.jpg
[repo_banner_img]: https://github.com/blktheta/raymond-hettinger-pycon2022/blob/main/media/TheBlueCup-JosephDecamp.png
[repo_wiki_url]: https://github.com/blktheta/raymond-hettinger-pycon2022/wiki
[repo_wiki_img]: https://img.shields.io/badge/docs-wiki_page-lightgrey?style=for-the-badge&logo=none
[repo_license_url]: https://github.com/blktheta/raymond-hettinger-pycon2022/blob/main/LICENSE.md
[repo_license_img]: https://img.shields.io/badge/license-MIT-red?style=for-the-badge&logo=none

<!-- Author -->
[author]: https://github.com/blktheta

<!-- Readme links -->
[rh_pycon2022_yt]: https://www.youtube.com/watch?v=jSIsyMd2-RY
[da_pycon2023_pv]: https://pyvideo.org/pycon-fr-2023/writing-great-test-documentation.html
