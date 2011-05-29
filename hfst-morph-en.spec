Summary:	HFST morphological analysis transducer for English language
Summary(pl.UTF-8):	Automat HFST do analizy morfologicznej dla języka angielskiego
Name:		hfst-morph-en
# or 20110316?
Version:	0
Release:	1
License:	GPL v2
Group:		Applications/Text
# source is hfst-english.tar.gz, but it doesn't contain scripts
Source0:	http://downloads.sourceforge.net/hfst/hfst-english-installable.tar.gz
# Source0-md5:	567c761cd7b8bb48c9600671b5ffebdf
Patch0:		%{name}-DESTDIR.patch
URL:		http://hfst.sourceforge.net/
Requires:	hfst
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an English morphological transducer for HFST. It is meant for
analysis, and thus overgenerates by allowing a large number of
prefixes and suffixes. The exceptions lexicon and parts of the main
lexicon are based on WordNet 2.0 (see
http://wordnet.princeton.edu/wordnet/license/). The grammar itself is
licensed under the GNU General Public License.

%description -l pl.UTF-8
Ten pakiet zawiera automat dla HFST do analizy morfologicznej języka
angielskiego. Jest przeznaczony do analizy, więc generuje nadmiarowe
dane, pozwalając na dużą liczbę przedrostków i przyrostków. Słownik
wyjątków i części głównego słownika są oparte na słowniku WordNet 2.0
(p. http://wordnet.princeton.edu/wordnet/license/). Sama gramatyka
jest na Powszechnej Licencji Publicznej GNU (GNU GPL).

%prep
%setup -q -n hfst-english-installable
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/english-analyze.sh
%attr(755,root,root) %{_bindir}/english-generate.sh
%{_datadir}/hfst/en
