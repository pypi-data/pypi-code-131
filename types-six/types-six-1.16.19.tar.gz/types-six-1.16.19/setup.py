from setuptools import setup

name = "types-six"
description = "Typing stubs for six"
long_description = '''
## Typing stubs for six

This is a PEP 561 type stub package for the `six` package.
It can be used by type-checking tools like mypy, PyCharm, pytype etc. to check code
that uses `six`. The source for this package can be found at
https://github.com/python/typeshed/tree/master/stubs/six. All fixes for
types and metadata should be contributed there.

See https://github.com/python/typeshed/blob/master/README.md for more details.
This package was generated from typeshed commit `2066b9533c5845dbecc5e7841efefaa2974b46fc`.
'''.lstrip()

setup(name=name,
      version="1.16.19",
      description=description,
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/python/typeshed",
      project_urls={
          "GitHub": "https://github.com/python/typeshed",
          "Changes": "https://github.com/typeshed-internal/stub_uploader/blob/main/data/changelogs/six.md",
          "Issue tracker": "https://github.com/python/typeshed/issues",
          "Chat": "https://gitter.im/python/typing",
      },
      install_requires=[],
      packages=['six-stubs'],
      package_data={'six-stubs': ['__init__.pyi', 'moves/BaseHTTPServer.pyi', 'moves/CGIHTTPServer.pyi', 'moves/SimpleHTTPServer.pyi', 'moves/__init__.pyi', 'moves/_dummy_thread.pyi', 'moves/_thread.pyi', 'moves/builtins.pyi', 'moves/cPickle.pyi', 'moves/collections_abc.pyi', 'moves/configparser.pyi', 'moves/copyreg.pyi', 'moves/email_mime_base.pyi', 'moves/email_mime_multipart.pyi', 'moves/email_mime_nonmultipart.pyi', 'moves/email_mime_text.pyi', 'moves/html_entities.pyi', 'moves/html_parser.pyi', 'moves/http_client.pyi', 'moves/http_cookiejar.pyi', 'moves/http_cookies.pyi', 'moves/queue.pyi', 'moves/reprlib.pyi', 'moves/socketserver.pyi', 'moves/tkinter.pyi', 'moves/tkinter_commondialog.pyi', 'moves/tkinter_constants.pyi', 'moves/tkinter_dialog.pyi', 'moves/tkinter_filedialog.pyi', 'moves/tkinter_tkfiledialog.pyi', 'moves/tkinter_ttk.pyi', 'moves/urllib/__init__.pyi', 'moves/urllib/error.pyi', 'moves/urllib/parse.pyi', 'moves/urllib/request.pyi', 'moves/urllib/response.pyi', 'moves/urllib/robotparser.pyi', 'moves/urllib_error.pyi', 'moves/urllib_parse.pyi', 'moves/urllib_request.pyi', 'moves/urllib_response.pyi', 'moves/urllib_robotparser.pyi', 'METADATA.toml']},
      license="Apache-2.0 license",
      classifiers=[
          "License :: OSI Approved :: Apache Software License",
          "Programming Language :: Python :: 3",
          "Typing :: Stubs Only",
      ]
)
