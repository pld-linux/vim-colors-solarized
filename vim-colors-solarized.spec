%define		colors	solarized
%define		snap	20161013
Summary:	Vim colorscheme: solarized
Name:		vim-colors-%{colors}
Version:	1.0.0
Release:	0.%{snap}.1
License:	Vim
Group:		Applications/Editors/Vim
Source0:	vim-colors-solarized-%{snap}.tar.gz
# Source0-md5:	93213046ae69c8694ce35a7c0493ab3b
URL:		https://github.com/altercation/vim-colors-solarized
Requires:	vim-rt >= 4:7.4.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_vimdatadir	%{_datadir}/vim

%description
Vim colorscheme: solarized.

%package doc
Summary:	Documentation for %{colors} Vim colorscheme
Requires(post,postun):	/usr/bin/vim
Requires:	%{name} = %{version}-%{release}
Requires:	vim-rt >= 4:7.4.2054-2

%description doc
Documentation for %{colors} Vim colorscheme.

%prep
%setup -qn vim-colors-solarized

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_vimdatadir}/
cp -pr autoload colors doc $RPM_BUILD_ROOT%{_vimdatadir}

rm $RPM_BUILD_ROOT%{_vimdatadir}/doc/tags

%clean
rm -rf $RPM_BUILD_ROOT

%post doc
%vim_doc_helptags

%postun doc
%vim_doc_helptags

%files
%defattr(644,root,root,755)
%doc README.mkd
%{_vimdatadir}/autoload/togglebg.vim
%{_vimdatadir}/colors/solarized.vim

%files doc
%defattr(644,root,root,755)
%{_vimdatadir}/doc/solarized.txt
