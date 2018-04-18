\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{thesis}[2018/01/09 v2.0 Thesis Class]
\LoadClass[12pt, oneside, letterpaper]{book}


\RequirePackage{etoolbox}

% Line spacing: dsingle/ddouble
%   Whether to use single- or doublespacing.
\newtoggle{DissertateSingleSpace}
\togglefalse{DissertateSingleSpace}
\DeclareOption{dsingle}{
    \toggletrue{DissertateSingleSpace}
    \ClassWarning{Dissertate}{Single-spaced mode on.}
}
\DeclareOption{ddouble}{\togglefalse{DissertateSingleSpace}}

\ProcessOptions\relax

% Line Spacing
%   Define two line spacings: one for the body, and one that is more compressed.

%% This looks good
% \iftoggle{DissertateSingleSpace}{
%     \newcommand{\dnormalspacing}{1.2}
%     \newcommand{\dcompressedspacing}{1.0}
% }{
%     \newcommand{\dnormalspacing}{1.5}  % Setting line spacing to 1.5
%     \newcommand{\dcompressedspacing}{1.2}
% }

\iftoggle{DissertateSingleSpace}{
    \newcommand{\dnormalspacing}{1.0}
    \newcommand{\dcompressedspacing}{1.0}
}{
    \newcommand{\dnormalspacing}{1.2}  % Setting line spacing to 1.5
    \newcommand{\dcompressedspacing}{1.0}
}

% Block quote with compressed spacing
\let\oldquote\quote
\let\endoldquote\endquote
\renewenvironment{quote}
    {\begin{spacing}{\dcompressedspacing}\oldquote}
    {\endoldquote\end{spacing}}

% Itemize with compressed spacing
\let\olditemize\itemize
\let\endolditemize\enditemize
\renewenvironment{itemize}
    {\begin{spacing}{\dcompressedspacing}\olditemize}
    {\endolditemize\end{spacing}}

% Enumerate with compressed spacing
\let\oldenumerate\enumerate
\let\endoldenumerate\endenumerate
\renewenvironment{enumerate}
    {\begin{spacing}{\dcompressedspacing}\oldenumerate}
    {\endoldenumerate\end{spacing}}

% Text layout.
\RequirePackage[width=5.75in, letterpaper]{geometry}
\usepackage{ragged2e}
% \RaggedRight
\RequirePackage{graphicx}
\usepackage{fixltx2e}
\parindent 12pt
\RequirePackage{lettrine}
\RequirePackage{setspace}
\RequirePackage{verbatim}

% Fonts.
\RequirePackage{color}
\RequirePackage{xcolor}
\usepackage{hyperref}
\RequirePackage{url}
\RequirePackage{amssymb}
\RequirePackage{mathspec}
\setmathsfont(Digits,Latin,Greek)[Numbers={Proportional}]{EB Garamond}
\setmathrm{EB Garamond}
\AtBeginEnvironment{tabular}{\addfontfeature{RawFeature=+tnum}}
\widowpenalty=300
\clubpenalty=300
\setromanfont[Numbers=OldStyle, Ligatures={Common, TeX}, Scale=1.0]{EB Garamond}
\newfontfamily{\smallcaps}[RawFeature={+c2sc,+scmp}]{Source Sans Pro}
\setsansfont[Scale=MatchLowercase, BoldFont={Lato Bold}]{Lato Regular}
\setmonofont[Scale=MatchLowercase]{Source Code Pro}
\RequirePackage[labelfont={bf,sf,footnotesize,singlespacing},
                textfont={sf,footnotesize,singlespacing},
                justification={justified},
                singlelinecheck=false,
                margin=0pt,
                figurewithin=chapter,
                tablewithin=chapter]{caption}
\renewcommand{\thefootnote}{\fnsymbol{footnote}}
\RequirePackage{microtype}




% Headings and headers.
\RequirePackage{fancyhdr}
\RequirePackage[tiny, md, sc]{titlesec}
\setlength{\headheight}{15pt}
%%%%%%%%%%%%%%%%%%% Making Subheadings Bold
\titleformat{\section}{\fontsize{14}{16}\bfseries}{\thesection}{1em}{}
\titleformat{\subsection}{\fontsize{12}{14}\bfseries}{\thesubsection}{1em}{}
%%%%%%%%%%%%%%%%%%%
\pagestyle{plain}
\RequirePackage{titling}


%% Front matter.
\setcounter{tocdepth}{2} %% changing to show subsections as well
\usepackage[titles]{tocloft}
\usepackage[titletoc]{appendix}
\renewcommand{\cftsecleader}{\cftdotfill{\cftdotsep}}
\renewcommand{\cftchapfont}{\normalsize \scshape}
\renewcommand\listfigurename{Listing of figures}
\renewcommand\listtablename{Listing of tables}

% References. +  Chapter headings
% \renewcommand\bibname{References}
% \RequirePackage[super,comma,numbers]{natbib}
% \renewcommand{\bibnumfmt}[1]{[#1]}

\RequirePackage[palatino]{quotchap}  % creates the large headings
\renewcommand*{\chapterheadstartvskip}{\vspace*{-6\baselineskip}}  % moving chapter heading up
\renewcommand*{\chapterheadendvskip}{\vspace{1\baselineskip}}


%% Overwriting spacing for non numbered chapters
\renewcommand{\@makechapterhead}[1]{
\chapterheadstartvskip
{\size@chapter{\sectfont\raggedleft
  {\chapnumfont
   \ifnum \c@secnumdepth >\m@ne%
    \if@mainmatter\thechapter\else\phantom{\thechapter}%
  \fi\else\vspace{-0.5\baselineskip}\phantom{\thechapter}\fi
  \par\nobreak}%
{\raggedleft\advance\leftmargin10em\interlinepenalty\@M #1\par}}
\nobreak\chapterheadendvskip}}

% An environment for paragraph-style section.
% \providecommand\newthought[1]{%
%    \addvspace{1.0\baselineskip plus 0.5ex minus 0.2ex}%
%    \noindent\textsc{#1}%
% }

% Align reference numbers so that they do not cause an indent.
\newlength\mybibindent
\setlength\mybibindent{0pt}
\renewenvironment{thebibliography}[1]
    {\chapter*{\bibname}%
     \@mkboth{\MakeUppercase\bibname}{\MakeUppercase\bibname}%
     \list{\@biblabel{\@arabic\c@enumiv}}
          {\settowidth\labelwidth{\@biblabel{999}}
           \leftmargin\labelwidth
            \advance\leftmargin\dimexpr\labelsep+\mybibindent\relax\itemindent-\mybibindent
           \@openbib@code
           \usecounter{enumiv}
           \let\p@enumiv\@empty
           \renewcommand\theenumiv{\@arabic\c@enumiv}}
     \sloppy
     \clubpenalty4000
     \@clubpenalty \clubpenalty
     \widowpenalty4000%
     \sfcode`\.\@m}
    {\def\@noitemerr
      {\@latex@warning{Empty `thebibliography' environment}}
     \endlist}

% Some definitions.
\def\advisor#1{\gdef\@advisor{#1}}

\definecolor{SchoolColor}{rgb}{0.5, 0.5, 0.5} % Crimson
\definecolor{chaptergrey}{rgb}{0.5, 0.5, 0.5} % for chapter numbers

\hypersetup{
    colorlinks,
    citecolor=SchoolColor,
    filecolor=black,
    linkcolor=black,
    urlcolor=SchoolColor,
}

\renewcommand{\maketitle}{
	\thispagestyle{empty}
  \newgeometry{top=0cm}
  {
    \begin{figure}[t]
      \hspace*{-3.33cm}
      \includegraphics[width=\paperwidth]{figures/ucl_logo.png}
    \end{figure}
  }
	\begin{center}
  \linespread{1}{
    \textcolor{SchoolColor}{
    	\Huge
      \vspace{2.5cm}
      \parbox{\linewidth}{
        \begin{center}
          \thetitle
        \end{center}
      }
    }
  }
  \normalsize \\
	{
  	\vspace{100pt}
  	{\Large \theauthor}\\
  	\vspace{12pt}
  	BSc Computer Science\\
    \vspace{12pt}
  	Supervisor: Dr. Ilya Sergey\\
  	\vspace{12pt}
  	Submission Date: 30th April 2018\\
  	\vspace*{\fill}
	}
	\center
	{
    \linespread{1.2}{
      % \large
      % { \fontfamily{\sfdefault}\selectfont
        This report is submitted as part requirement for the BSc degree in Computer Science at UCL.
        It is substantially the result of my own
        work except where explicitly indicated in the text. The report may be freely copied
        and distributed provided the source is explicitly acknowledged. \par
      % }
    }
  }
	\end{center}
  \restoregeometry
}

\newcommand{\abstractpage}{
	\newpage
	\pagenumbering{roman}
	\setcounter{page}{3}
	\pagestyle{fancy}
	\lhead{Thesis advisor: \@advisor} \rhead{\@author}
	\renewcommand{\headrulewidth}{0.0pt}
	\vspace*{35pt}
	\begin{center}
	\Large \textcolor{SchoolColor}{Mechanised Verification of Paxos-like Consensus Protocols} \normalsize \\
	\vspace*{20pt}
	\scshape Abstract \\ \rm
	\end{center}
	\input{frontmatter/abstract}
	\vspace*{\fill}
	\newpage \lhead{} \rhead{}
	\cfoot{\thepage}
}

\newcommand{\dedicationpage}{
	\newpage \thispagestyle{fancy} \vspace*{\fill}
	\scshape \noindent \input{frontmatter/dedication}
	\vspace*{\fill} \newpage \rm
}

\newcommand{\acknowledgments}{
	\chapter*{Acknowledgments}
	\noindent
	\input{frontmatter/thanks}
	\vspace*{\fill} \newpage
	\setcounter{page}{1}
	\pagenumbering{arabic}
}
