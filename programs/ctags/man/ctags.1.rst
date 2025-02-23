.. _ctags(1):

==============================================================
ctags
==============================================================
--------------------------------------------------------------
Generate tag files for source code
--------------------------------------------------------------
:Version: 0.0.0
:Manual group: Universal-ctags
:Manual section: 1

SYNOPSIS
--------
|	**ctags** [options] [source_file(s)]
|	**etags** [options] [source_file(s)]


DESCRIPTION
-----------

The **ctags** and **etags** programs
(hereinafter collectively referred to as ctags,
except where distinguished) generate an index (or "tag") file for a
variety of **language objects** found in **source file(s)**. This tag file allows
these items to be quickly and easily located by a text editor or other
utilities (**client tools**). A **tag** signifies a language object for which an index entry is
available (or, alternatively, the index entry created for that object).

Alternatively, ctags can generate a cross reference
file which lists, in human readable form, information about the various
language objects found in a set of source files.

Tag index files are supported by numerous editors, which allow the user to
locate the object associated with a name appearing in a source file and
jump to the file and line which defines the name. See the manual of your
favorite editor about utilizing ctags command and
the tag index files in the editor.

ctags is capable of generating different **kinds** of tags
for each of many different **languages**. For a complete list of supported
languages, the names by which they are recognized, and the kinds of tags
which are generated for each, see the ``--list-languages`` and ``--list-kinds-full``
options.

This man page describes **Universal-ctags**, an implementation of ctags
derived from **Exuberant-ctags**. The major incompatible changes between
Universal-ctags and Exuberant-ctags are enumerated in
ctags-incompatibilities(7).

One of the advantages of Exuberant-ctags is that it allows a user to
define a new parser from the command line. Extending this capability is one
of the major features of Universal-ctags. ctags-optlib(7)
describes how the capability is extended.

Newly introduced experimental features are not explained here. If you
are interested in such features and ctags internals,
visit https://docs.ctags.io/en/latest/.


COMMAND LINE INTERFACE
----------------------

Despite the wealth of available options, defaults are set so that
ctags is most commonly executed without any options (e.g.
"ctags \*", or "ctags -R"), which will
create a tag file in the current directory for all recognized source
files. The options described below are provided merely to allow custom
tailoring to meet special needs.

Note that spaces separating the single-letter options from their parameters
are optional.

Note also that the boolean parameters to the long form options (those
beginning with "--" and that take a "[=yes|no]" parameter) may be omitted,
in which case "=yes" is implied. (e.g. ``--sort`` is equivalent to ``--sort=yes``).
Note further that "=1", "=on", and "=true" are considered synonyms for "=yes",
and that "=0", "=off", and "=false" are considered synonyms for "=no".

Some options are either ignored or useful only when used while running in
etags mode (see -e option). Such options will be noted.

Most options may appear anywhere on the command line, affecting only those
files which follow the option. A few options, however, must appear
before the first file name and will be noted as such.

Options taking language names will accept those names in either upper or
lower case. See the ``--list-languages`` option for a complete list of the
built-in language names.


Letters and names
~~~~~~~~~~~~~~~~~

Some options take one-letter flags as parameters (e.g. ``--kinds-<LANG>`` option).
Specifying just letters help a user create a complicated command line
quickly.  However, a command line including sequences of one-letter flags
becomes difficult to understand.

Universal-ctags accepts long-name flags in
addition to such one-letter flags. The long-name and one-letter flags can be mixed in an
option parameter by surrounding each long-name by braces. Thus, for an
example, the following three notations for ``--kinds-C`` option have
the same meaning::

	--kinds-C=+pLl
	--kinds-C=+{prototype}{label}{local}
	--kinds-C=+{prototype}L{local}

Note that braces may be meta characters in your shell. Put
single quotes in such case.

``--list-...`` options shows one-letter flags and associated long-name flags.


List options
~~~~~~~~~~~~

Universal-ctags introduces many ``--list-...`` options that provide
the internal data of Universal-ctags. Both users and client tools may
use the data. ``--with-list-header`` and ``--machinable`` options
adjust the output of the most of ``--list-...`` options.

The default setting (``--with-list-header=yes`` and ``--machinable=no``)
is for using interactively from a terminal. The header that explains
the meaning of columns is simply added to the output, and each column is
aligned in all lines. The header line starts with a hash ('#') character.

For scripting in a client tool, ``--with-list-header=no`` and
``--machinable=yes`` may be useful. The header is not added to the
output, and each column is separated by tab characters.

Note the order of columns will change in the future release.
However, labels in the header will not change. So by scanning
the header, a client tool can find the index for the target
column.

.. options that should be explained and revised here
   ``--list-features``    (done)
   ``--machinable``       (done)
   ``--with-list-header`` (done)


OPTIONS
------------
ctags has more options than listed here.
Options starting with an underscore character, such as ``--_echo=msg``,
are not listed here. They are experimental or for debugging purpose.

``-?``
	Equivalent to ``--help``.

``-a``
	Equivalent to ``--append``.

``-B``
	Use backward searching patterns (e.g. ?pattern?). [Ignored in etags mode]

``-D macro=definition``
	Defines a C preprocessor macro. This emulates the behaviour of the
	corresponding gcc option. All types of macros are supported,
	including the ones with parameters and variable arguments.
	Stringification, token pasting and recursive macro expansion are also
	supported.
	This extends the function provided by ``-I`` option.

``-e``
	Same as ``--output-format=etags``.
	Enable etags mode, which will create a tag file for use with the Emacs
	editor. Alternatively, if ctags is invoked by a
	name containing the string "etags" (either by renaming,
	or creating a link to, the executable), etags mode will be enabled.
	This option must appear before the first file name.

``-f tagfile``
	Use the name specified by tagfile for the tag file (default is "tags",
	or "TAGS" when running in etags mode). If tagfile is specified as "-",
	then the tags are written to standard output instead. ctags
	will stubbornly refuse to take orders if tagfile exists and
	its first line contains something other than a valid tags line. This
	will save your neck if you mistakenly type "ctags -f
	\*.c", which would otherwise overwrite your first C file with the tags
	generated by the rest! It will also refuse to accept a multi-character
	file name which begins with a '-' (dash) character, since this most
	likely means that you left out the tag file name and this option tried to
	grab the next option as the file name. If you really want to name your
	output tag file "-ugly", specify it as "./-ugly". This option must
	appear before the first file name. If this option is specified more
	than once, only the last will apply.

``-F``
	Use forward searching patterns (e.g. /pattern/) (default). [Ignored
	in etags mode]

``-G``
	Equivalent to ``--guess-language-eagerly``.

``-h list``
	Specifies a list of file extensions, separated by periods, which are
	to be interpreted as include (or header) files. To indicate files having
	no extension, use a period not followed by a non-period character
	(e.g. ".", "..x", ".x."). This option only affects how the scoping of
	particular kinds of tags are interpreted (i.e. whether or not they are
	considered as globally visible or visible only within the file in which
	they are defined); it does not map the extension to any particular
	language. Any tag which is located in a non-include file and cannot be
	seen (e.g. linked to) from another file is considered to have file-limited
	(e.g. static) scope. No kind of tag appearing in an include file
	will be considered to have file-limited scope. If the first character
	in the list is a plus sign, then the extensions in the list will be
	appended to the current list; otherwise, the list will replace the
	current list. See, also, the "F/fileScope" flag of ``--extras`` option.
	The default list is
	".h.H.hh.hpp.hxx.h++.inc.def". To restore the default list, specify ``-h``
	default. Note that if an extension supplied to this option is not
	already mapped to a particular language (see "`Determining file language`_", above),
	you will also need to use either the ``--langmap`` or ``--language-force`` option.

``-I identifier-list``
	Specifies a list of identifiers which are to be specially handled while
	parsing C and C++ source files. This option is specifically provided
	to handle special cases arising through the use of preprocessor macros.
	When the identifiers listed are simple identifiers, these identifiers
	will be ignored during parsing of the source files. If an identifier is
	suffixed with a '+' character, ctags will also
	ignore any parenthesis-enclosed argument list which may immediately
	follow the identifier in the source files. If two identifiers are
	separated with the '=' character, the first identifiers is replaced by
	the second identifiers for parsing purposes. The list of identifiers may
	be supplied directly on the command line or read in from a separate file.
	If the first character of identifier-list is '@', '.' or a pathname
	separator (``'/'`` or ``'\'``), or the first two characters specify a drive
	letter (e.g. "C:"), the parameter identifier-list will be interpreted as
	a filename from which to read a list of identifiers, one per input line.
	Otherwise, identifier-list is a list of identifiers (or identifier
	pairs) to be specially handled, each delimited by either a comma or
	by white space (in which case the list should be quoted to keep the
	entire list as one command line argument). Multiple ``-I`` options may be
	supplied. To clear the list of ignore identifiers, supply a single
	dash ("-") for identifier-list.

	This feature is useful when preprocessor macros are used in such a way
	that they cause syntactic confusion due to their presence. Indeed,
	this is the best way of working around a number of problems caused by
	the presence of syntax-busting macros in source files (see "`CAVEATS`_").
	Some examples will illustrate this point.

	.. code-block:: C

		int foo ARGDECL4(void *, ptr, long int, nbytes)

	In the above example, the macro "ARGDECL4" would be mistakenly
	interpreted to be the name of the function instead of the correct name
	of "foo". Specifying "-I ARGDECL4" results in the correct behavior.

	.. code-block:: C

		/* creates an RCS version string in module */
		MODULE_VERSION("$Revision$")

	In the above example the macro invocation looks too much like a function
	definition because it is not followed by a semicolon (indeed, it
	could even be followed by a global variable definition that would look
	much like a K&R style function parameter declaration). In fact, this
	seeming function definition could possibly even cause the rest of the
	file to be skipped over while trying to complete the definition.
	Specifying "-I MODULE_VERSION+" would avoid such a problem.

	.. code-block:: C

		CLASS Example {
			// your content here
		};

	The example above uses "CLASS" as a preprocessor macro which expands to
	something different for each platform. For instance CLASS may be
	defined as "class __declspec(dllexport)" on Win32 platforms and simply
	"class" on UNIX. Normally, the absence of the C++ keyword "class"
	would cause the source file to be incorrectly parsed. Correct behavior
	can be restored by specifying "-I CLASS=class".

``-L file``
	Read from file a list of file names for which tags should be generated.
	If file is specified as "-", then file names are read from standard
	input. File names read using this option are processed following file
	names appearing on the command line. Options are also accepted in this
	input. If this option is specified more than once, only the last will
	apply. Note: file is read in line-oriented mode, where a new line is
	the only delimiter and non-trailing white space is considered significant,
	in order that file names containing spaces may be supplied
	(however, trailing white space is stripped from lines); this can affect
	how options are parsed if included in the input.

``-n``
	Equivalent to ``--excmd=number``.

``-N``
	Equivalent to ``--excmd=pattern``.

``-o tagfile``
	Equivalent to ``-f tagfile``.

``-R``
	Equivalent to ``--recurse``.

``-u``
	Equivalent to ``--sort=no`` (i.e. "unsorted").

``-V``
	Equivalent to ``--verbose``.

``-w``
	This option is silently ignored for backward-compatibility with the
	ctags of SVR4 Unix.

``-x``
	Same as ``--output-format=xref``.
	Print a tabular, human-readable cross reference (xref) file to standard
	output instead of generating a tag file. The information contained in
	the output includes: the tag name; the kind of tag; the line number,
	file name, and source line (with extra white space condensed) of the
	file which defines the tag. No tag file is written and all options
	affecting tag file output will be ignored. Example applications for this
	feature are generating a listing of all functions located in a source
	file (e.g. "ctags -x --kinds-c=f file"), or generating
	a list of all externally visible global variables located in a source
	file (e.g. "ctags -x --kinds-c=v --extras=-F file").
	This option must appear before the first file name.

``--alias-<LANG>=[+|-]aliasPattern``
	Adds ('+') or removes ('-') an alias pattern to a language specified
	with *<LANG>*. ctags refers to the alias pattern in
	"`Determining file language`_" stage.

	The parameter aliasPattern is not a list. Use this option multiple
	times in a command line to add or remove multiple alias
	patterns.

	To restore the default language aliases, specify "default" as the
	parameter aliasPattern. Using "all" for *<LANG>* has meaning in
	following two cases:

	``--alias-all=``
		This clears aliases setting of all languages.

	``--alias-all=default``
		This restores the default languages aliases for all languages.

``--append[=yes|no]``
	Indicates whether tags generated from the specified files should be
	appended to those already present in the tag file or should replace them.
	This option is "no" by default. This option must appear before the
	first file name.

``--etags-include=file``
	Include a reference to file in the tag file. This option may be specified
	as many times as desired. This supports Emacs' capability to use a
	tag file which "includes" other tag files. [Available only in etags mode]

``--exclude=[pattern]``
	Add pattern to a list of excluded files and directories. This option may
	be specified as many times as desired. For each file name considered
	by ctags, each pattern specified using this option
	will be compared against both the complete path (e.g.
	some/path/base.ext) and the base name (e.g. base.ext) of the file, thus
	allowing patterns which match a given file name irrespective of its
	path, or match only a specific path. If appropriate support is available
	from the runtime library of your C compiler, then pattern may
	contain the usual shell wildcards (not regular expressions) common on
	Unix (be sure to quote the option parameter to protect the wildcards from
	being expanded by the shell before being passed to ctags;
	also be aware that wildcards can match the slash character, '/').
	You can determine if shell wildcards are available on your platform by
	examining the output of the ``--list-features`` option, which will include
	"wildcards" in the compiled feature list; otherwise, pattern is matched
	against file names using a simple textual comparison.

	If pattern begins with the character '@', then the rest of the string
	is interpreted as a file name from which to read exclusion patterns,
	one per line. If pattern is empty, the list of excluded patterns is
	cleared.

	Note that at program startup, the default exclude list contains names of
	common hidden and system files, patterns for binary files, and directories
	for which it is generally not desirable to descend while processing the
	``--recurse`` option. To see the list of built-in exclude patterns, use
	``--list-excludes``.

	See also the description for ``--exclude-exception=`` option.

``--exclude-exception=[pattern]``
	Add pattern to a list of included files and directories. The pattern
	affects the files and directories that are excluded by the pattern
	specified with ``--exclude=`` option.

	For an example, you want @CTAGS_NAME_EXAMPLE@ to ignore all files
	under "foo" directory except "foo/main.c", use the following command
	line: "--exclude=foo/* --exclude-exception=foo/main.c". Don't forget
	shell quoting for '*'.

``--excmd=type``
	Determines the type of EX command used to locate tags in the source
	file. [Ignored in etags mode]

	The valid values for type (either the entire word or the first letter
	is accepted) are:

	number
		Use only line numbers in the tag file for locating tags. This has
		four advantages:

		1.	Significantly reduces the size of the resulting tag file.
		2.	Eliminates failures to find tags because the line defining the
			tag has changed, causing the pattern match to fail (note that
			some editors, such as vim, are able to recover in many such
			instances).
		3.	Eliminates finding identical matching, but incorrect, source
			lines (see "`BUGS`_").
		4.	Retains separate entries in the tag file for lines which are
			identical in content. In pattern mode, duplicate entries are
			dropped because the search patterns they generate are identical,
			making the duplicate entries useless.

		However, this option has one significant drawback: changes to the
		source files can cause the line numbers recorded in the tag file
		to no longer correspond to the lines in the source file, causing
		jumps to some tags to miss the target definition by one or more
		lines. Basically, this option is best used when the source code
		to which it is applied is not subject to change. Selecting this
		option type causes the following options to be ignored: ``-BF``.

	pattern
		Use only search patterns for all tags, rather than the line numbers
		usually used for macro definitions. This has the advantage of
		not referencing obsolete line numbers when lines have been added or
		removed since the tag file was generated.

	mixed
		In this mode, patterns are generally used with a few exceptions.
		For C, line numbers are used for macro definition tags. This was
		the default format generated by the original ctags and is, therefore,
		retained as the default for this option. For Fortran, line numbers
		are used for common blocks because their corresponding source lines
		are generally identical, making pattern searches useless
		for finding all matches.

	combine
		Combine adjusted line number and pattern with a semicolon.
		ctags adjusts the line number by decrementing
		or incrementing (if ``-B`` option is given) one.
		This adjustment helps a client tool like vim to search the pattern
		from the line before (or after) the pattern starts.

``--extra=[+|-]flags|*``
	Equivalent to ``--extras=[+|-]flags|*``, which was introduced to
	make the option naming convention align to the other options
	like ``--kinds-<LANG>=`` and ``--fields=``.

	This option is kept for backward-compatibility with Exuberant-ctags.

``--extras=[+|-]flags|*``
	Specifies whether to include extra tag entries for certain kinds of
	information. See also "`Extras`_" subsection to know what are extras.

	The parameter flags is a set of one-letter flags (and/or long-name flags), each
	representing one kind of extra tag entry to include in the tag file.
	If flags is preceded by either the '+' or '-' character, the effect of
	each flag is added to, or removed from, those currently enabled;
	otherwise the flags replace any current settings. All entries are
	included  if '*' is given.

	This ``--extras=`` option is for controlling extras common in all
	languages (or language-independent extras).  Universal-ctags also
	supports language-specific extras. (See "`Language-specific fields and
	extras`_" about the concept). Use ``--extras-<LANG>=`` option for
	controlling them.

	The meaning of major extras is as follows (one-letter flag/long-name flag):

	/anonymous
		Include an entry for the language object that has no name like lambda
		function. This extra has no one-letter flag and is enabled by
		default. The extra tag is useful as a placeholder to fill scope fields
		for language objects defined in a language object with no name.

		.. code-block:: C

			struct {
				double x, y;
			} p = { .x = 0.0, .y = 0.0 };

		"x" and "y" are the members of a structure. When filling the scope
		fields for them, ctags has trouble because the struct
		where "x" and "y" belong to has no name. For overcoming the trouble,
		ctags generates an anonymous extra tag for the struct
		and fills the scope fields with the name of the extra tag.

		.. code-block::

			__anon9f26d2460108	input.c	/^struct {$/;"	s
			p	input.c	/^} p = { .x = 0.0, .y = 0.0 };$/;"	v	typeref:struct:__anon9f26d2460108
			x	input.c	/^	double x, y;$/;"	m	struct:__anon9f26d2460108
			y	input.c	/^	double x, y;$/;"	m	struct:__anon9f26d2460108

		The above tag output has "__anon9f26d2460108" as an anonymous extra tag.
		The typeref field of "p" also receives the benefit of it.

	F/fileScope
		Indicates whether tags scoped only for a single file (i.e. tags which
		cannot be seen outside of the file in which they are defined, such as
		language objects with "static" modifier of C language) should be included
		in the output. See, also, the ``-h`` option. This option is enabled by
		default. This is the replacement for ``--file-scope`` option of
		Exuberant-ctags.

	f/inputFile
		Include an entry for the base file name of every source file
		(e.g. "example.c"), which addresses the first line of the file.
		This flag is the replacement for ``--file-tags`` hidden option of
		Exuberant-ctags.

		If the ``end:`` field is enabled, the end line number of the file can be
		attached to the tag. (However, @CTAGS_NAME_EXAMPLE@ omits the ``end:`` field
		if no newline is in the file like an empty file.)

		By default, @CTAGS_NAME_EXAMPLE@ doesn't create the "f/inputFile" extra
		tag for the source file when @CTAGS_NAME_EXAMPLE@ doesn't find a parser
		for it. Enabling "Unknown" parser with "--languages=+Unknown" forces
		@CTAGS_NAME_EXAMPLE@ to create the extra tags for any source files.

		The etags mode enables the "Unknown" parser implicitly.

	p/pseudo
		Include pseudo-tags. Enabled by default unless the tag file is
		written to standard output. See ctags-client-tools(7) about
		the detail of pseudo-tags.

	q/qualified
		Include an extra class-qualified or namespace-qualified tag entry
		for each tag which is a member of a class or a namespace.

		This may allow easier location of a specific tags when
		multiple occurrences of a tag name occur in the tag file.
		Note, however, that this could potentially more than double
		the size of the tag file.

		The actual form of the qualified tag depends upon the language
		from which the tag was derived (using a form that is most
		natural for how qualified calls are specified in the
		language). For C++ and Perl, it is in the form
		"class::member"; for Eiffel and Java, it is in the form
		"class.member".

		Note: Using backslash characters as separators forming
		qualified name in PHP. However, in tags output of
		Universal-ctags, a backslash character in a name is escaped
		with a backslash character. See tags(5) about the escaping.

	r/reference
		Include reference tags. See "`TAG ENTRIES`_" about reference tags.

	Inquire the output of ``--list-extras`` option for the other minor
	extras.

``--extras-<LANG>=[+|-]flags|*``
	Specifies whether to include extra tag entries for certain kinds of
	information for language <LANG>. Universal-ctags
	introduces language-specific extras. See "`Language-specific fields and
	extras`_" about the concept. This option is for controlling them.

	Specifies "all" as <LANG> to apply the parameter flags to all
	languages; all extras are enabled with specifying '*' as the
	parameter flags. If specifying nothing as the parameter flags
	(``--extras-all=``), all extras are disabled. These two combinations
	are useful for testing.

	Check the output of the ``--list-extras=<LANG>`` option for the
	extras of specific language <LANG>.

``--fields=[+|-]flags|*``
	Specifies which available extension fields are to be included in
	the tag entries (see "`TAG FILE FORMAT`_" second, and "`Fields`_"
	subsection , for more information).

	The parameter flags is a set of one-letter flags (and/or long-name flags),
	each representing one type of extension field to include.
	Each letter or group of letters may be preceded by either '+' to add it
	to the default set, or '-' to exclude it. In the absence of any
	preceding '+' or '-' sign, only those fields explicitly listed in flags
	will be included in the output (i.e. overriding the default set). All
	fields are included if '*' is given. This option is ignored if the
	option ``--format=1`` (legacy tag file format) has been specified.

	This ``--fields=`` option is for controlling fields common in all
	languages (or language-independent fields).  Universal-ctags also
	supports language-specific fields. (See "`Language-specific fields and
	extras`_" about the concept). Use ``--fields-<LANG>=`` option for
	controlling them.


	The meaning of major fields is as follows (one-letter flag/long-name flag):

	a/access
		Access (or export) of class members

	e/end
		End lines of various items

	f/file
		File-restricted scoping. Enabled by default.

	i/inherits
		Inheritance information.

	k
		Kind of tag as one-letter. Enabled by default.
		Exceptionally this has no field name.
		See also z/kind flag.

	K
		Kind of tag as long-name.
		Exceptionally this has no field name.
		See also z/kind flag.

	l/language
		Language of source file containing tag

	m/implementation
		Implementation information

	n/line
		Line number of tag definition

	p/scopeKind
		Kind of scope as long-name

	r/roles
		Roles assigned to the tag.
		For a definition tag, this field takes "def" as a value.

	s
		Scope of tag definition. Enabled by default.
		Exceptionally this has no name.
		See also Z flag.

		.. TODO? implement "scope" of Z/scope flag.

	S/signature
		Signature of routine (e.g. prototype or parameter list)

	t/typeref
		Type and name of a variable, typedef or return type of
		callable like function as "typeref:" field.
		Enabled by default.

	z/kind
		Include the "kind:" key in kind field

	Z
		Include the "scope:" key in scope field.
		Exceptionally this has no name.

	Check the output of the ``--list-fields`` option for the other minor
	fields.

``--fields-<LANG>=[+|-]flags|*``
	Specifies which language-specific fields are to be included in
	the entries of the tag file. Universal-ctags
	supports language-specific fields. (See "`Language-specific fields and
	extras`_" about the concept). This option is for controlling them.

	Specify "all" as <LANG> to apply the parameter flags to all
	fields; all fields are enabled with specifying '*' as the
	parameter flags. If specifying nothing as the parameter flags
	(``--fields-all=``), all fields are disabled. These two combinations
	are useful for testing.

``--file-scope[=yes|no]``
	This options is removed. Use "--extras=[+|-]F" or
	"--extras=[+|-]{fileScope}" instead.

``--filter[=yes|no]``
	Makes ctags behave as a filter, reading source
	file names from standard input and printing their tags to standard
	output on a file-by-file basis. If ``--sort`` is enabled, tags are sorted
	only within the source file in which they are defined. File names are
	read from standard input in line-oriented input mode (see note for ``-L``
	option) and only after file names listed on the command line or from
	any file supplied using the ``-L`` option. When this option is enabled,
	the options ``-f``, ``-o``, and ``--totals`` are ignored. This option is quite
	esoteric and is disabled by default. This option must appear before
	the first file name.

``--filter-terminator=string``
	Specifies a string to print to standard output following the tags for
	each file name parsed when the ``--filter`` option is enabled. This may
	permit an application reading the output of ctags
	to determine when the output for each file is finished. Note that if the
	file name read is a directory and ``--recurse`` is enabled, this string will
	be printed only once at the end of all tags found for by descending
	the directory. This string will always be separated from the last tag
	line for the file by its terminating newline. This option is quite
	esoteric and is empty by default. This option must appear before
	the first file name.

``--format=level``
	Change the format of the output tag file. Currently the only valid
	values for level are 1 or 2. Level 1 specifies the original tag file
	format and level 2 specifies a new extended format containing extension
	fields (but in a manner which retains backward-compatibility with
	original vi(1) implementations). The default level is 2. This option
	must appear before the first file name. [Ignored in etags mode]

``--guess-language-eagerly``
	Looks into the file contents for heuristically guessing the proper language parser.
	See "`Determining file language`_".

``--help``
	Prints to standard output a detailed usage description, and then exits.

``--help-full``
	Prints to standard output a detailed usage description about experimental
	features, and then exits. Visit https://docs.ctags.io/en/latest/ for information
	about the latest exciting experimental features.

``--if0[=yes|no]``
	Indicates a preference as to whether code within an "#if 0" branch of a
	preprocessor conditional should be examined for non-macro tags (macro
	tags are always included). Because the intent of this construct is to
	disable code, the default value of this option is no. Note that this
	indicates a preference only and does not guarantee skipping code within
	an "#if 0" branch, since the fall-back algorithm used to generate
	tags when preprocessor conditionals are too complex follows all branches
	of a conditional. This option is disabled by default.

``--input-encoding=encoding``
	Specifies the encoding of the input files.
	If this option is specified, Universal-ctags converts the input from this
	encoding to the encoding specified by ``--output-encoding=encoding``.

``--input-encoding-<LANG>=encoding``
	Specifies a specific input encoding for ``LANG``. It overrides the global
	default value given with ``--input-encoding``.

``--kinddef-<LANG>=letter,name,description``
	See ctags-optlib(7).
	Be not confused this with ``--kinds-<LANG>``.

``--kinds-<LANG>=[+|-]kinds|*``
	Specifies a list of language-specific kinds of tags (or kinds) to
	include in the output file for a particular language, where <LANG> is
	case-insensitive and is one of the built-in language names (see the
	``--list-languages`` option for a complete list). The parameter kinds is a group
	of one-letter flags (and/or long-name flags) designating kinds of tags (particular to the language)
	to either include or exclude from the output. The specific sets of
	flags recognized for each language, their meanings and defaults may be
	list using the ``--list-kinds-full`` option. Each letter or group of letters
	may be preceded by either '+' to add it to, or '-' to remove it from,
	the default set. In the absence of any preceding '+' or '-' sign, only
	those kinds explicitly listed in kinds will be included in the output
	(i.e. overriding the default for the specified language).

	Specify '*' as the parameter to include all kinds implemented
	in <LANG> in the output. Furthermore if "all" is given as <LANG>,
	specification of the parameter kinds affects all languages defined
	in ctags. Giving "all" makes sense only when '*' or
	'F' is given as the parameter kinds.

	As an example for the C language, in order to add prototypes and
	external variable declarations to the default set of tag kinds,
	but exclude macros, use "--kinds-c=+px-d"; to include only tags for
	functions, use "--kinds-c=f".

	Some kinds of C and C++ languages are synchronized; enabling
	(or disabling) a kind in one language enables the kind having
	the same one-letter and long-name in the other language. See also the
	description of MASTER column of ``--list-kinds-full``.

``--<LANG>-kinds=[+|-]kinds|*``
	This option is obsolete. Use ``--kinds-<LANG>=...`` instead.

``--langdef=name``
	See ctags-optlib(7).

``--langmap=map[,map[...]]``
	Controls how file names are mapped to languages (see the ``--list-maps``
	option). Each comma-separated *map* consists of the language name (either
	a built-in or user-defined language), a colon, and a list of **file
	extensions** and/or **file name patterns**. A file extension is specified by
	preceding the extension with a period (e.g. ".c"). A file name pattern
	is specified by enclosing the pattern in parentheses (e.g.
	"([Mm]akefile)").

	If appropriate support is available from the runtime
	library of your C compiler, then the file name pattern may contain the usual
	shell wildcards common on Unix (be sure to quote the option parameter to
	protect the wildcards from being expanded by the shell before being
	passed to ctags). You can determine if shell wildcards
	are available on your platform by examining the output of the
	``--list-features`` option, which will include "wildcards" in the compiled
	feature list; otherwise, the file name patterns are matched against
	file names using a simple textual comparison.

	When mapping a file extension with ``--langmap`` option,
	it will first be unmapped from any other languages. (``--map-<LANG>``
	option provides more fine-grained control.)

	If the first character in a map is a plus sign ('+'), then the extensions and
	file name patterns in that map will be appended to the current map
	for that language; otherwise, the map will replace the current map.
	For example, to specify that only files with extensions of .c and .x are
	to be treated as C language files, use "--langmap=c:.c.x"; to also add
	files with extensions of .j as Java language files, specify
	"--langmap=c:.c.x,java:+.j". To map makefiles (e.g. files named either
	"Makefile", "makefile", or having the extension ".mak") to a language
	called "make", specify "--langmap=make:([Mm]akefile).mak". To map files
	having no extension, specify a period not followed by a non-period
	character (e.g. ".", "..x", ".x.").

	To clear the mapping for a
	particular language (thus inhibiting automatic generation of tags for
	that language), specify an empty extension list (e.g. "--langmap=fortran:").
	To restore the default language mappings for a particular language,
	supply the keyword "default" for the mapping. To specify restore the
	default language mappings for all languages, specify "--langmap=default".

	Note that file name patterns are tested before file extensions when inferring
	the language of a file. This order of Universal-ctags is different from
	Exuberant-ctags. See ctags-incompatibilities(7) for the background of
	this incompatible change.

``--language-force=language``
	By default, ctags automatically selects the language
	of a source file, ignoring those files whose language cannot be
	determined (see "`Determining file language`_", above). This option forces the specified
	*language* (case-insensitive; either built-in or user-defined) to be used
	for every supplied file instead of automatically selecting the language
	based upon its extension. In addition, the special value "auto" indicates
	that the language should be automatically selected (which effectively
	disables this option).

``--languages=[+|-]list``
	Specifies the languages for which tag generation is enabled, with *list*
	containing a comma-separated list of language names (case-insensitive;
	either built-in or user-defined). If the first language of *list* is not
	preceded by either a '+' or '-', the current list (the current settings
	of enabled/disabled languages managed in ctags internally)
	will be cleared before adding or removing the languages in *list*. Until a '-' is
	encountered, each language in the *list* will be added to the current list.
	As either the '+' or '-' is encountered in the *list*, the languages
	following it are added or removed from the current list, respectively.
	Thus, it becomes simple to replace the current list with a new one, or
	to add or remove languages from the current list.

	The actual list of
	files for which tags will be generated depends upon the language
	extension mapping in effect (see the ``--langmap`` option). Note that the most of all
	languages, including user-defined languages, are enabled unless explicitly
	disabled using this option. Language names included in list may be any
	built-in language or one previously defined with ``--langdef``. The default
	is "all", which is also accepted as a valid argument. See the
	``--list-languages`` option for a list of the all (built-in and user-defined)
	language names.

	Note ``--languages=`` option works cumulative way; the option can be
	specified with different arguments multiple times in a command line.

``--license``
	Prints a summary of the software license to standard output, and then exits.

``--line-directives[=yes|no]``
	Specifies whether "#line" directives should be recognized. These are
	present in the output of preprocessors and contain the line number, and
	possibly the file name, of the original source file(s) from which the
	preprocessor output file was generated. When enabled, this option will
	cause ctags to generate tag entries marked with the
	file names and line numbers of their locations original source file(s),
	instead of their actual locations in the preprocessor output. The actual
	file names placed into the tag file will have the same leading path
	components as the preprocessor output file, since it is assumed that
	the original source files are located relative to the preprocessor
	output file (unless, of course, the #line directive specifies an
	absolute path). This option is off by default. Note: This option is generally
	only useful when used together with the ``--excmd=number`` (``-n``) option.
	Also, you may have to use either the ``--langmap`` or ``--language-force`` option
	if the extension of the preprocessor output file is not known to
	ctags.

``--links[=yes|no]``
	Indicates whether symbolic links (if supported) should be followed.
	When disabled, symbolic links are ignored. This option is on by default.

``--list-aliases[=language|all]``
	Lists the aliases for either the specified *language* or **all**
	languages, and then exits.
	**all** is used as default value if the option argument is omitted.
	The aliases are used when heuristically testing a language parser for a
	source file.

``--list-excludes``
	Lists the current exclusion patterns used to exclude files.

``--list-extras[=language|all]``
	Lists the extras recognized for either the specified *language* or
	**all** languages. See "`Extras`_" subsection to know what are extras.
	**all** is used as default value if the option argument is omitted.

	An extra can be enabled or disabled with ``--extras=`` for common
	extras in all languages, or ``--extras-<LANG>=`` for the specified
	language.  These option takes one-letter flag or long-name flag as a parameter
	for specifying an extra.

	The meaning of columns are as follows:

	LETTER
		One-letter flag. '-' means the extra does not have one-letter flag.

	NAME
		Long-name flag. The long-name is used in ``extras:`` field.

	ENABLED
		Whether the extra is enabled or not. It takes "yes" or "no".

	LANGUAGE
		The name of language if the extra is owned by a parser.
		"NONE" means the extra is common in parsers.

	DESCRIPTION
		Human readable description for the extra.

``--list-features``
	Lists the compiled features.

``--list-fields[=language|all]``
	Lists the fields recognized for either the specified *language* or
	**all** languages. See "`Fields`_" subsection to know what are fields.
	**all** is used as default value if the option argument is omitted.

	.. TODO? xref output

	A field can be enabled or disabled with ``--fields=`` for common
	fields in all languages, or ``--fields-<LANG>=`` for the specified
	language.  These option takes one-letter flags and/or long-name flags
	as a parameter for specifying fields.

	The meaning of columns are as follows:

	LETTER
		One-letter flag. '-' means the field does not have one-letter flag.

	NAME
		Long-name of field.

	ENABLED
		Whether the field is enabled or not. It takes "yes" or "no".

	LANGUAGE
		The name of language if the field is owned by a parser.
		"NONE" means the extra is common in parsers.

	JSTYPE
		Json type used in printing the value of field when "--output-format=json"
		is specified.

		Following characters are used for representing types.

		s
			string
		i
			integer
		b
			boolean (true or false)

		The representation of this field and the output format used in
		"--output-format=json" are still experimental.

	FIXED
	   Whether this field can be disabled or not. Some fields are printed always
	   in tags output. They have "yes" as the value for this column.

	DESCRIPTION
		Human readable description for the field.

``--list-kinds[=language|all]``
	Subset of ``--list-kinds-full``. This option is kept for
	backward-compatibility with Exuberant-ctags.

	This option prints only LETTER, DESCRIPTION, and ENABLED fields
	of ``--list-kinds-full`` output. However, the presentation of
	ENABLED column is different from that of ``--list-kinds-full``
	option; "[off]" follows after description if the kind is disabled,
	and nothing follows	if enabled. The most of all kinds are enabled
	by default.

	The critical weakness of this option is that this option does not
	print the name of kind. Universal-ctags introduces
	``--list-kinds-full`` because it considers that names are
	important.

	This option does not work with ``--machinable`` nor
	``--with-list-header``.

``--list-kinds-full[=language|all]``
	Lists the tag kinds recognized for either the specified *language*
	or **all** languages, and then exits. See "`Kinds`_" subsection to
	learn what kinds are.
	**all** is used as default value if the option argument is omitted.

	Each kind of tag recorded in the tag file is represented by a
	one-letter flag, or a long-name flag. They are also used to filter the tags
	placed into the output through use of the ``--kinds-<LANG>``
	option.

	The meaning of columns are as follows:

	LANGUAGE
		The name of language having the kind.

	LETTER
		One-letter flag. This must be unique in a language.

	NAME
		The long-name flag of the kind. This can be used as the alternative
		to the one-letter flag described above. If enabling 'K' field with
		``--fields=+K``, ctags uses long-names instead of
		one-letters in tags output. To enable/disable a kind with
		``--kinds-<LANG>`` option, long-name surrounded by braces instead
		of one-letter. See "`Letters and names`_" for details. This must be
		unique in a language.

	ENABLED
		Whether the kind is enabled or not. It takes "yes" or "no".

	REFONLY
		Whether the kind is specialized for reference tagging or not.
		If the column is "yes", the kind is for reference tagging, and
		it is never used for definition tagging. See also "`TAG ENTRIES`_".

	NROLES
		The number of roles this kind has. See also "`Roles`_".

	MASTER
		The master parser controlling enablement of the kind.
		A kind belongs to a language (owner) in Universal-ctags;
		enabling and disabling a kind in a language has no effect on
		a kind in another language even if both kinds has the
		same one-letter flag and/or the same long-name flag. In other words,
		the namespace of kinds are separated by language.

		However, Exuberant-ctags does not separate the kinds of C and
		C++. Enabling/disabling kindX in C language enables/disables a
		kind in C++ language having the same long-name flag with kindX. To
		emulate this behavior in Universal-ctags, a concept named
		"master parser" is introduced. Enabling/disabling some kinds
		are synchronized under the control of a master language.

		.. code-block:: console

			$ ctags --kinds-C=+'{local}' --list-kinds-full \
			  | grep -E '^(#|C\+\+ .* local)'
			#LANGUAGE  LETTER NAME   ENABLED REFONLY NROLES MASTER DESCRIPTION
			C++        l      local  yes     no      0      C      local variables
			$ ctags --kinds-C=-'{local}' --list-kinds-full \
			  | grep -E '^(#|C\+\+ .* local)'
			#LANGUAGE  LETTER NAME   ENABLED REFONLY NROLES MASTER DESCRIPTION
			C++        l      local  no      no      0      C      local variables

		You see "ENABLED" field of "local" kind of C++ language is changed
		Though "local" kind of C language is enabled/disabled. If you swap the languages, you
		see the same result.

	DESCRIPTION
		Human readable description for the kind.

``--list-languages``
	Lists the names of the languages understood by ctags,
	and then exits. These language names are case insensitive and may be
	used in many other options like ``--language-force``,
	``--languages``, ``--kinds-<LANG>``, ``--regex-<LANG>``, and so on.

	Each language listed is disabled if followed by "[disabled]".
	To use the parser for such a language, specify the language as an
	argument of ``--languages=+`` option.

	This option does not work with ``--machinable`` nor
	``--with-list-header``.

``--list-map-extensions[=language|all]``
	Lists the file extensions which associate a file
	name with a language for either the specified *language* or **all**
	languages, and then exits.
	**all** is used as default value if the option argument is omitted.

``--list-map-patterns[=language|all]``
	Lists the file name patterns which associate a file
	name with a language for either the specified *language* or **all**
	languages, and then exits.
	**all** is used as default value if the option argument is omitted.

``--list-maps[=language|all]``
	Lists file name patterns and the file extensions which associate a file
	name with a language for either the specified *language* or **all**
	languages, and then exits. See the ``--langmap`` option, and
	"`Determining file language`_", above.
	**all** is used as default value if the option argument is omitted.

	To list the file extensions or file name patterns individually, use
	``--list-map-extensions`` or ``--list-map-patterns`` option.
	See the ``--langmap`` option, and "`Determining file language`_", above.

	This option does not work with ``--machinable`` nor
	``--with-list-header``.

``--list-mline-regex-flags``
	Output list of flags which can be used in a multiline regex parser
	definition.

``--list-params[=language|all]``
	Lists the parameters for either the specified *language* or **all**
	languages, and then exits.
	**all** is used as default value if the option argument is omitted.

``--list-pseudo-tags``
	Output list of pseudo-tags.

``--list-regex-flags``
	See ctags-optlib(7).

``--list-roles[=language|all[.kinds]]``
	List the roles for either the specified *language* or **all** languages.
	**all** is used as default value if the option argument is omitted.
	If the parameter kinds is given after the parameter
	*language* or **all** with concatenating with '.', list only roles
	defined in the kinds. Both one-letter flags and long name flags surrounded
	by braces are acceptable as the parameter kinds.

	The meaning of columns are as follows:

	LANGUAGE
		The name of language having the role.

	KIND(L/N)
		The one-letter flag and the long-name flag of kind having the role.

	NAME
		The long-name flag of the role.

	ENABLED
		Whether the kind is enabled or not. It takes "yes" or "no".
		(Currently all roles are enabled. No option for disabling
		a specified role is not implemented yet.)

	DESCRIPTION
		Human readable description for the role.

``--list-subparsers[=baselang|all]``
	Lists the subparsers for a base language for either the specified
	*baselang* or **all** languages, and then exits.
	**all** is used as default value if the option argument is omitted.

``--machinable[=yes|no]``
	Use tab character as separators for ``--list-`` option output.  It
	may be suitable for scripting. See "`List options`_" for considered
	use cases. Disabled by default.

``--map-<LANG>=[+|-]extension|pattern``
	This option provides the way to control mapping(s) of file names to
	languages in a more fine-grained way than ``--langmap`` option.

	In ctags, more than one language can map to a
	file name pattern or file extension (*N:1 map*). Alternatively,
	``--langmap`` option handle only *1:1 map*, only one language
	mapping to one file name pattern or file extension.  A typical N:1
	map is seen in C++ and ObjectiveC language; both languages have
	a map to ".h" as a file extension.

	A file extension is specified by preceding the extension with a period (e.g. ".c").
	A file name pattern is specified by enclosing the pattern in parentheses (e.g.
	"([Mm]akefile)"). A prefixed plus ('+') sign is for adding, and
	minus ('-') is for removing. No prefix means replacing the map of *<LANG>*.

	Unlike ``--langmap``, *extension* (or *pattern*) is not a list.
	``--map-<LANG>`` takes one *extension* (or *pattern*). However,
	the option can be specified with different arguments multiple times
	in a command line.

``--maxdepth=N``
	Limits the depth of directory recursion enabled with the ``--recurse``
	(``-R``) option.

``--mline-regex-<LANG>=/line_pattern/name_pattern/[flags]``
	Define multiline regular expression for locating tags in specific language.

``--options=pathname``
	Read additional options from file or directory.

	ctags searches *pathname* in optlib path list
	first. If ctags cannot find a file or directory
	in the list, ctags reads a file or directory
	at the specified *pathname*.

	If a file is specified, it should contain one option per line. If
	a directory is specified, files suffixed with ".ctags" under it
	are read in alphabetical order.

	As a special case, if "--options=NONE" is specified as the first
	option on the command line, preloading is disabled; the option
	will disable the automatic reading of any configuration options
	from either a file or the environment (see "`FILES`_").

``--options-maybe=pathname``
	Same as ``--options`` but doesn't cause an error if file
	(or directory) specified with *pathname* doesn't exist.

``--optlib-dir=[+]directory``
	Add an optlib *directory* to or reset **optlib** path list.
	By default, the optlib path list is empty.

``--output-encoding=encoding``
	Specifies the encoding of the tags file.
	Universal-ctags converts the encoding of input files from the encoding
	specified by ``--input-encoding=encoding`` to this encoding.

	In addition ``encoding`` is specified at the top the tags file as the
	value for the ``TAG_FILE_ENCODING`` pseudo-tag. The default value of
	``encoding`` is UTF-8.

``--output-format=u-ctags|e-ctags|etags|xref|json``
	Specify the output format. The default is "u-ctags".
	See tags(5) for "u-ctags" and "e-ctags".
	See ``-e`` for "etags", and ``-x`` for "xref".
	"json" is experimental format, and available only if
	the ctags executable is built with libjansson.
	This option must appear before the first file name.

.. TODO: convert output-json.rst to ctags-json-output.1.rst (ctags-json-output(1)).
   and add a link to it here.

``--param-<LANG>:name=argument``
	Set <LANG> specific parameter. Available parameters can be listed with
	``--list-params``.

``--pattern-length-limit=N``
	Cutoff patterns of tag entries after N characters. Disable by setting to 0
	(default is 96). Specifying 0 as *N* results no truncation.

	An input source file with long lines and multiple tag matches per
	line can generate an excessively large tags file with an
	unconstrained pattern length. For example, running ctags on a
	minified JavaScript source file often exhibits this behaviour.

	The truncation avoids cutting in the middle of a UTF-8 code point
	spanning multiple bytes to prevent writing invalid byte sequences from
	valid input files. This handling allows for an extra 3 bytes above the
	configured limit in the worse case of a 4 byte code point starting
	right before the limit. Please also note that this handling is fairly
	naive and fast, and although it is resistant against any input, it
	requires a valid input to work properly; it is not guaranteed to work
	as the user expects when dealing with partially invalid UTF-8 input.
	This also partially affect non-UTF-8 input, if the byte sequence at
	the truncation length looks like a multibyte UTF-8 sequence. This
	should however be rare, and in the worse case will lead to including
	up to an extra 3 bytes above the limit.

``--print-language``
	Just prints the language parsers for specified source files, and then exits.

``--pseudo-tags=[+|-]ptag``, ``--pseudo-tags=*``
	Enable/disable emitting pseudo-tag named ptag.
	If \* is given, enable emitting all pseudo-tags.

``--put-field-prefix``
	Put "UCTAGS" as prefix for the name of fields newly introduced in
	Universal-ctags.

	Some fields are newly introduced in Universal-ctags and more will
	be introduced in the future. Other tags generators may also
	introduce their specific fields.

	In such a situation, there is a concern about conflicting field
	names; mixing tags files generated by multiple tags generators
	including Universal-ctags is difficult. This option provides a
	workaround for such station.

	.. code-block:: console

		$ ctags --fields='{line}{end}' -o - hello.c
		main	hello.c	/^main(int argc, char **argv)$/;"	f	line:3	end:6
		$ ctags --put-field-prefix --fields='{line}{end}' -o - /tmp/hello.c
		main	/tmp/hello.c	/^main(int argc, char **argv)$/;"	f	line:3	UCTAGSend:6

	In the above exapmle, the prefix is put to "end" field which is
	newly introduced in Universal-ctags.

``--quiet[=yes|no]``
	Write fewer messages (default is no).

``--recurse[=yes|no]``
	Recurse into directories encountered in the list of supplied files.
	If the list of supplied files is empty and no file list is specified with
	the -L option, then the current directory (i.e. ".") is assumed.
	Symbolic links are followed. If you don't like these behaviors, either
	explicitly specify the files or pipe the output of find(1) into
	ctags -L- instead. Note: This option is not supported on
	all platforms at present. It is available if the output of the ``--help``
	option includes this option. See, also, the ``--exclude`` and
	``--maxdepth`` to limit recursion.

``--regex-<LANG>=/regexp/replacement/[kind-spec/][flags]``
	See ctags-optlib(7).

``--sort[=yes|no|foldcase]``
	Indicates whether the tag file should be sorted on the tag name
	(default is yes). Note that the original vi(1) required sorted tags.
	The foldcase value specifies case insensitive (or case-folded) sorting.
	Fast binary searches of tag files sorted with case-folding will require
	special support from tools using tag files, such as that found in the
	ctags readtags library, or Vim version 6.2 or higher
	(using "set ignorecase"). This option must appear before the first file
	name. [Ignored in etags mode]

``--tag-relative[=yes|no|always|never]``
	The yes value indicates that the file paths recorded in the tag file should be
	relative to the directory containing the tag file, rather than relative
	to the current directory, unless the files supplied on the command line
	are specified with absolute paths. This option must appear before the
	first file name. The default is yes when running in etags mode (see
	the ``-e`` option), no otherwise.
	The always value indicates the recorded file paths should be relative
	even if source file names are passed in with absolute paths.
	The never value indicates the recorded file paths should be absolute
	even if source file names are passed in with relative paths.

``--totals[=yes|no|extra]``
	Prints statistics about the source files read and the tag file written
	during the current invocation of ctags. This option
	is off by default. This option must appear before the first file name.

	The extra value prints parser specific statistics for parsers
	gathering such information.

``--use-slash-as-filename-separator[=yes|no]``
	Uses slash character as filename separators instead of backslash
	character when printing ``input:`` field.
	This option is available on MSWindows only.
	The default is yes for the default "u-ctags" output format, and
	no for the other formats.

``--verbose[=yes|no]``
	Enable verbose mode. This prints out information on option processing
	and a brief message describing what action is being taken for each file
	considered by ctags. Normally, ctags
	does not read command line arguments until after options are read
	from the configuration files (see "`FILES`_", below) and the CTAGS
	environment variable. However, if this option is the first argument on
	the command line, it will take effect before any options are read from
	these sources. The default is no.

``--version``
	Prints a version identifier for ctags to standard
	output, and then exits. This is guaranteed to always contain the string
	"Universal Ctags".

``--with-list-header[=yes|no]``
	Print headers describing columns in ``--list-`` option output.
	See also "`List options`_".

OPERATIONAL DETAILS
-------------------
As ctags considers each source file name in turn, it tries to
determine the language of the file by applying tests described in
"`Determining file language`_".

If a language was identified, the file is opened and then the appropriate
language parser is called to operate on the currently open file. The parser
parses through the file and adds an entry to the tag file for each
language object it is written to handle. See "`TAG FILE FORMAT`_", below,
for details on these entries.

This implementation of ctags imposes no formatting
requirements on C code as do legacy implementations. Older implementations
of ctags tended to rely upon certain formatting assumptions in order to
help it resolve coding dilemmas caused by preprocessor conditionals.

In general, ctags tries to be smart about conditional
preprocessor directives. If a preprocessor conditional is encountered
within a statement which defines a tag, ctags follows
only the first branch of that conditional (except in the special case of
"#if 0", in which case it follows only the last branch). The reason for
this is that failing to pursue only one branch can result in ambiguous
syntax, as in the following example:

.. code-block:: C

	#ifdef TWO_ALTERNATIVES
	struct {
	#else
	union {
	#endif
		short a;
		long b;
	}

Both branches cannot be followed, or braces become unbalanced and
ctags would be unable to make sense of the syntax.

If the application of this heuristic fails to properly parse a file,
generally due to complicated and inconsistent pairing within the
conditionals, ctags will retry the file using a
different heuristic which does not selectively follow conditional
preprocessor branches, but instead falls back to relying upon a closing
brace ("}") in column 1 as indicating the end of a block once any brace
imbalance results from following a #if conditional branch.

ctags will also try to specially handle arguments lists
enclosed in double sets of parentheses in order to accept the following
conditional construct:

	extern void foo __ARGS((int one, char two));

Any name immediately preceding the "((" will be automatically ignored and
the previous name will be used.

C++ operator definitions are specially handled. In order for consistency
with all types of operators (overloaded and conversion), the operator
name in the tag file will always be preceded by the string "operator "
(i.e. even if the actual operator definition was written as "operator<<").

After creating or appending to the tag file, it is sorted by the tag name,
removing identical tag lines.


Determining file language
--------------------------

File name mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~

Unless the ``--language-force`` option is specified, the language of each source
file is automatically selected based upon a **mapping** of file names to
languages. The mappings in effect for each language may be displayed using
the ``--list-maps`` option and may be changed using the ``--langmap`` or
``--map-<LANG>`` options.

If the name of a file is not mapped to a language, ctags tries
to heuristically guess the language for the file by inspecting its content. See
"`Determining file language`_".

All files that have no file name mapping and no guessed parser are
ignored. This permits running ctags on all files in
either a single directory (e.g.  "ctags \*"), or on
all files in an entire source directory tree
(e.g. "ctags -R"), since only those files whose
names are mapped to languages will be scanned.

The same extensions are mapped to multiple parsers. For example, ".h"
are mapped to C++, C and ObjectiveC. These mappings can cause
issues. ctags tries to select the proper parser
for the source file by applying heuristics to its content, however
it is not perfect.  In case of issues one can use ``--language-force=language``,
``--langmap=map[,map[...]]``, or the ``--map-<LANG>=-pattern|extension``
options. (Some of the heuristics are applied whether ``--guess-language-eagerly``
is given or not.)

.. options should be revised here
	``--map-<LANG>`` (done)
	``--langmap=map[,map[...]]`` (done)
	``--language-force=language`` (done)
	``--languages=[+|-]list`` (done)
	``--list-maps[=language|all]`` (done)
	``--list-map-extensions`` (done)
	``--list-map-patterns`` (done)

Heuristically guessing
~~~~~~~~~~~~~~~~~~~~~~~~~~

If ctags cannot select a parser from the mapping of file names,
various heuristic tests are conducted to determine the language:

template file name testing
	If the file name has an ".in" extension, ctags applies
	the mapping to the file name without the extension. For example,
	"config.h" is tested for a file named "config.h.in".

"interpreter" testing
	The first line of the file is checked to see if the file is a "#!"
	script for a recognized language. ctags looks for
	a parser having the same name.

	If ctags finds no such parser,
	ctags looks for the name in alias lists. For
	example, consider if the first line is "#!/bin/sh".  Though
	ctags has a "shell" parser, it doesn't have a "sh"
	parser. However, "sh" is listed as an alias for "shell", therefore
	ctags selects the "shell" parser for the file.

	An exception is "env". If "env" is specified, ctags
	reads more lines to find real interpreter specification.

	To display the list of aliases, use ``--list-aliases`` option.
	To add/remove an item to/from the list, use the
	``--alias-<LANG>=[+|-]aliasPattern`` option.

"zsh autoload tag" testing
	If the first line starts with "#compdef" or "#autoload",
	ctags regards the line as "zsh".

"emacs mode at the first line" testing
	The Emacs editor has multiple editing modes specialized for programming
	languages. Emacs can recognize a marker called modeline in a file
	and utilize the marker for the mode selection. This heuristic test does
	the same as what Emacs does.

	ctags treats *MODE* as a name of interpreter and applies the same
	rule of "interpreter" testing if the first line has one of
	the following patterns::

		-*- mode: MODE -*-

	or

	::

		-*- MODE -*-

"emacs mode at the EOF" testing
	Emacs editor recognizes another marker at the end of file as a
	mode specifier. This heuristic test does the same as what Emacs does.

	ctags treats *MODE* as a name of an interpreter and applies the same
	rule of "interpreter" heuristic testing, if the lines at the tail of the file
	have the following pattern::

		Local Variables:
		...
		mode: MODE
		...
		End:

	3000 characters are sought from the end of file to find the pattern.

"vim modeline" testing
	Like the modeline of the Emacs editor, Vim editor has the same concept.
	ctags treats *TYPE* as a name of interpreter and applies the same
	rule of "interpreter" heuristic testing if the last 5 lines of the file
	have one of the following patterns::

		filetype=TYPE

	or

	::

		ft=TYPE

"PHP marker" testing
	If the first line is started with "<?php",
	ctags regards the line as "php".

Looking into the file contents is a more expensive operation than file
name matching. So ctags runs the testings in limited
conditions.  "interpreter" testing is enabled only when a file is an
executable or the ``--guess-language-eagerly`` (``-G`` in short) option is
given. The other heuristic tests are enabled only when ``-G`` option is
given.

The ``--print-language`` option can be used just to print the results of
parser selections for given files instead of generating a tags file.

Examples:

.. code-block:: console

	$ ctags --print-language config.h.in input.m input.unknown
	config.h.in: C++
	input.m: MatLab
	input.unknown: NONE

``NONE`` means that ctags does not select any parser for the file.


TAG ENTRIES
-----------

A tag is an index for a language object. The concept of a tag and related
items in Exuberant-ctags are refined and extended in Universal-ctags.

A tag is categorized into **definition tags** or **reference tags**.
In general, Exuberant-ctags only tags *definitions* of
language objects: places where newly named language objects are introduced.
Universal-ctags, on the other hand, can also tag *references* of language
objects: places where named language objects are used. However, support
for generating reference tags is new and limited to specific areas of
specific languages in the current version.


Fields
~~~~~~

A tag can record various information, called **fields**. The
essential fields are: **name** of language objects, **input**,
**pattern**, and **line**. ``input:`` is the name of source file where
``name:`` is defined or referenced. ``pattern:`` can be used to search
the **name** in ``input:``. **line** is the line number where
``name:`` is defined or referenced in ``input:``.

ctags offers extension fields. See also the
descriptions of ``--list-fields`` option and ``--fields`` option.


Kinds
~~~~~~

``kind:`` is a field which represents the *kind* of language object
specified by a tag. Kinds used and defined are very different between
parsers. For example, C language defines "macro", "function",
"variable", "typedef", etc. See also the descriptions of
``--list-kinds-full`` option and ``--kinds-<LANG>`` option.


Extras
~~~~~~

Generally, ctags tags only language objects appearing
in source files, as is. In other words, a value for a ``name:`` field
should be found on the source file associated with the ``name:``. An
"extra" type tag (*extra*) is for tagging a language object with a processed
name, or for tagging something not associated with a language object. A typical
extra tag is "qualified", which tags a language object with a
class-qualified or scope-qualified name.

The following example demonstrates the "qualified" extra tag.

.. code-block:: Java

	package Bar;
	import Baz;

	class Foo {
		// ...
	}

For the above source file, ctags tags "Bar" and "Foo" by
default.  If the "qualified" extra is enabled from the command line
(``--extras=+q``), then "Bar.Foo" is also tagged even though the string
"Bar.Foo" is not in the source code.

See also the descriptions of ``--list-extras`` option and ``--extras``
option in "`OPTIONS`_".


Roles
~~~~~~

*Role* is a newly introduced concept in Universal-ctags. Role is a
concept associated with reference tags, and is not implemented widely yet.

As described previously in "Kinds", the "kind" field represents the type
of language object specified with a tag, such as a function vs. a variable.
Specific kinds are defined for reference tags, such as the C++ kind "header" for
header file, or Java kind "package" for package statements. For such reference
kinds, a "roles" field can be added to distinguish the role of the reference
kind. In other words, the "kind" field identifies the "what" of the language
object, whereas the "roles" field identifies the "how" of a referenced language
object. Roles are only used with specific kinds.

For example, for the source file used for demonstrating in the "`Extras`_"
subsection, "Baz" is tagged as a reference tag with kind "package" and with
role "imported". Another example is for a C++ "header" kind tag, generated by
"#include" statements: the ``roles:system`` or ``roles:local`` fields will be
added depending on whether the include file name begins with "<" or not.

See also the descriptions of ``--list-roles`` option.


Language-specific fields and extras
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Exuberant-ctags has the concept of "fields" and "extras". They are common
between parsers of different languages. Universal-ctags extends this concept
by providing language-specific fields and extras.

.. options should be explained and revised here
   ``--list-languages`` (done)
   ``--list-kinds``     (done)
   ``--list-kinds-full``(done)
   ``--list-fields``    (done)
   ``--list-extras``    (done)
   ``--list-roles``     (done)
   ``--kinds-<LANG>=``  (done)
   ``--fields=``        (done)
   ``--fields-<LANG>``  (done)
   ``--extras=``        (done)
   ``--extras-<LANG>=`` (done)


TAG FILE FORMAT
---------------

When not running in etags mode, each entry in the tag file consists of a
separate line, each looking like this in the most general case:

tag_name<TAB>file_name<TAB>ex_cmd;"<TAB>extension_fields

The fields and separators of these lines are specified as follows:

	1.	tag name
	2.	single tab character
	3.	name of the file in which the object associated with the tag is located
	4.	single tab character
	5.	EX command used to locate the tag within the file; generally a
		search pattern (either /pattern/ or ?pattern?) or line number (see
		``--excmd``). Tag file format 2 (see ``--format``) extends this EX command
		under certain circumstances to include a set of extension fields
		(described below) embedded in an EX comment immediately appended
		to the EX command, which leaves it backward-compatible with original
		vi(1) implementations.

A few special tags are written into the tag file for internal purposes.
These tags are composed in such a way that they always sort to the top of
the file. Therefore, the first two characters of these tags are used a magic
number to detect a tag file for purposes of determining whether a
valid tag file is being overwritten rather than a source file.

Note that the name of each source file will be recorded in the tag file
exactly as it appears on the command line. Therefore, if the path you
specified on the command line was relative to the current directory, then
it will be recorded in that same manner in the tag file. See, however,
the ``--tag-relative`` option for how this behavior can be modified.

Extension fields are tab-separated key-value pairs appended to the end of
the EX command as a comment, as described above. These key value pairs
appear in the general form "key:value". Their presence in the lines of the
tag file are controlled by the ``--fields`` option. The possible keys and
the meaning of their values are as follows:

.. Q: this list is very out-of-date. Should we just say "use --list-fields"?

access
	Indicates the visibility of this class member, where value is specific
	to the language.

file
	Indicates that the tag has file-limited visibility. This key has no
	corresponding value.

kind
	Indicates the type, or kind, of tag. Its value is either one of the
	corresponding one-letter flags described under the various
	``--kinds-<LANG>`` options above, or a long-name flag. It is permitted
	(and is, in fact, the default) for the key portion of this field to be
	omitted. The optional behaviors are controlled with the ``--fields`` option.

implementation
	When present, this indicates a limited implementation (abstract vs.
	concrete) of a routine or class, where value is specific to the
	language ("virtual" or "pure virtual" for C++; "abstract" for Java).

inherits
	When present, value. is a comma-separated list of classes from which
	this class is derived (i.e. inherits from).

signature
	When present, value is a language-dependent representation of the
	signature of a routine. A routine signature in its complete form
	specifies the return type of a routine and its formal argument list.
	This extension field is presently supported only for C-based
	languages and does not include the return type.

In addition, information on the scope of the tag definition may be
available, with the key portion equal to some language-dependent construct
name and its value the name declared for that construct in the program.
This scope entry indicates the scope in which the tag was found.
For example, a tag generated for a C structure member would have a scope
looking like "struct:myStruct".


HOW TO USE WITH VI
------------------

Vi will, by default, expect a tag file by the name "tags" in the current
directory. Once the tag file is built, the following commands exercise
the tag indexing feature:

vi -t tag
	Start vi and position the cursor at the file and line where "tag"
	is defined.

:ta tag
	Find a tag.

Ctrl-]
	Find the tag under the cursor.

Ctrl-T
	Return to previous location before jump to tag (not widely implemented).


HOW TO USE WITH GNU EMACS
-------------------------

Emacs will, by default, expect a tag file by the name "TAGS" in the
current directory. Once the tag file is built, the following commands
exercise the tag indexing feature:

M-x visit-tags-table <RET> FILE <RET>
	Select the tag file, "FILE", to use.

M-. [TAG] <RET>
	Find the first definition of TAG. The default tag is the identifier
	under the cursor.

M-*
	Pop back to where you previously invoked "M-.".

C-u M-.
	Find the next definition for the last tag.

For more commands, see the Tags topic in the Emacs info document.


HOW TO USE WITH NEDIT
---------------------

NEdit version 5.1 and later can handle the new extended tag file format
(see ``--format``). To make NEdit use the tag file, select "File->Load Tags
File". To jump to the definition for a tag, highlight the word, then press
Ctrl-D. NEdit 5.1 can read multiple tag files from different
directories. Setting the X resource nedit.tagFile to the name of a tag
file instructs NEdit to automatically load that tag file at startup time.


CAVEATS
-------

Because ctags is neither a preprocessor nor a compiler,
use of preprocessor macros can fool ctags into either
missing tags or improperly generating inappropriate tags. Although
ctags has been designed to handle certain common cases,
this is the single biggest cause of reported problems. In particular,
the use of preprocessor constructs which alter the textual syntax of C
can fool ctags. You can work around many such problems
by using the ``-I`` option.

Note that since ctags generates patterns for locating
tags (see the ``--excmd`` option), it is entirely possible that the wrong line
may be found by your editor if there exists another source line which is
identical to the line containing the tag. The following example
demonstrates this condition:

.. code-block:: C

	int variable;

	/* ... */
	void foo(variable)
	int variable;
	{
		/* ... */
	}

Depending upon which editor you use and where in the code you happen to be,
it is possible that the search pattern may locate the local parameter
declaration in foo() before it finds the actual global variable definition,
since the lines (and therefore their search patterns are identical).
This can be avoided by use of the ``--excmd=n`` option.


BUGS
----

ctags has more options than ls(1).

When parsing a C++ member function definition (e.g. "className::function"),
ctags cannot determine whether the scope specifier
is a class name or a namespace specifier and always lists it as a class name
in the scope portion of the extension fields. Also, if a C++ function
is defined outside of the class declaration (the usual case), the access
specification (i.e. public, protected, or private) and implementation
information (e.g. virtual, pure virtual) contained in the function
declaration are not known when the tag is generated for the function
definition. It will, however be available for prototypes (e.g. "--kinds-c++=+p").

No qualified tags are generated for language objects inherited into a class.

ENVIRONMENT VARIABLES
---------------------

CTAGS
	If this environment variable exists, it will be expected to contain a
	set of default options which are read when ctags
	starts, after the configuration files listed in FILES, below, are read,
	but before any command line options are read. Options appearing on
	the command line will override options specified in this variable.
	Only options will be read from this variable. Note that all white space
	in this variable is considered a separator, making it impossible to pass
	an option parameter containing an embedded space. If this is a problem,
	use a configuration file instead.

ETAGS
	Similar to the CTAGS variable above, this variable, if found, will be
	read when etags starts. If this variable is not
	found, etags will try to use CTAGS instead.

TMPDIR
	On Unix-like hosts where mkstemp() is available, the value of this
	variable specifies the directory in which to place temporary files.
	This can be useful if the size of a temporary file becomes too large
	to fit on the partition holding the default temporary directory
	defined at compilation time. ctags creates temporary
	files only if either (1) an emacs-style tag file is being
	generated, (2) the tag file is being sent to standard output, or
	(3) the program was compiled to use an internal sort algorithm to sort
	the tag files instead of the sort utility of the operating system.
	If the sort utility of the operating system is being used, it will
	generally observe this variable also. Note that if ctags
	is setuid, the value of TMPDIR will be ignored.


FILES
-----

$XDG_CONFIG_HOME/ctags/\*.ctags, or $HOME/.config/ctags/\*.ctags if $XDG_CONFIG_HOME is not defeind
(on other than MSWindows)

$HOME/.ctags.d/\*.ctags

$HOMEDRIVE$HOMEPATH/ctags.d/\*.ctags (on MSWindows only)

.ctags.d/\*.ctags

ctags.d/\*.ctags

	If any of these configuration files exist, each will be expected to
	contain a set of default options which are read in the order listed
	when ctags starts, but before the CTAGS environment
	variable is read or any command line options are read. This makes it
	possible to set up personal or project-level defaults. It
	is possible to compile ctags to read an additional
	configuration file before any of those shown above, which will be
	indicated if the output produced by the ``--version`` option lists the
	"custom-conf" feature. Options appearing in the CTAGS environment
	variable or on the command line will override options specified in these
	files. Only options will be read from these files. Note that the option
	files are read in line-oriented mode in which spaces are significant
	(since shell quoting is not possible) but spaces at the beginning
	of a line are ignored. Each line of the file is read as
	one command line parameter (as if it were quoted with single quotes).
	Therefore, use new lines to indicate separate command-line arguments.
	A line starting with '#' is treated as a comment.

	\*.ctags files in a directory are loaded in alphabetical order.

tags
	The default tag file created by ctags.

TAGS
	The default tag file created by etags.


SEE ALSO
--------

See ctags-optlib(7) for defining (or extending) a parser
in a configuration file.

See tags(5) for the format of tag files.

See ctags-incompatibilities(7) about known incompatible changes
with Exuberant-ctags.

See ctags-client-tools(7) if you are interested in writing
a tool for processing tags files.

See readtags(1) about a client tool for binary searching a
name in a sorted tags file.

The official Universal-ctags web site at:

https://ctags.io/

Also ex(1), vi(1), elvis, or, better yet, vim, the official editor of ctags.
For more information on vim, see the VIM Pages web site at:

https://www.vim.org/


AUTHOR
------

Universal-ctags project
https://ctags.io/

Darren Hiebert <dhiebert@users.sourceforge.net>
http://DarrenHiebert.com/


MOTIVATION
----------

"Think ye at all times of rendering some service to every member of the
human race."

"All effort and exertion put forth by man from the fullness of his heart is
worship, if it is prompted by the highest motives and the will to do
service to humanity."

-- From the Baha'i Writings

CREDITS
-------
This version of ctags (Universal-ctags) derived from
the repository, known as **fishman-ctags**, started by Reza Jelveh.

Some parsers are taken from **tagmanager** of **Geany** (https://www.geany.org/)
project.


The fishman-ctags was derived from Exuberant-ctags.

Exuberant-ctags was originally derived from and
inspired by the ctags program by Steve Kirkendall <kirkenda@cs.pdx.edu>
that comes with the Elvis vi clone (though virtually none of the original
code remains).

Credit is also due Bram Moolenaar <Bram@vim.org>, the author of vim,
who has devoted so much of his time and energy both to developing the editor
as a service to others, and to helping the orphans of Uganda.

The section entitled "HOW TO USE WITH GNU EMACS" was shamelessly stolen
from the info page for GNU etags.
