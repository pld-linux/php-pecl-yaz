%define		php_name	php%{?php_suffix}
%define		modname		yaz
Summary:	%{modname} - a Z39.50 client for PHP
Summary(pl.UTF-8):	%{modname} - klient Z39.50 dla PHP
Name:		%{php_name}-pecl-%{modname}
Version:	1.1.6
Release:	1
License:	PHP v3.01
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{modname}-%{version}.tgz
# Source0-md5:	b4d586861df602ed330da38c3136d86c
URL:		http://pecl.php.net/package/yaz/
BuildRequires:	libxslt-devel
BuildRequires:	%{php_name}-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.650
BuildRequires:	yaz-devel >= 3.0.2
%{?requires_php_extension}
Requires:	php(core) >= 5.0.4
Suggests:	re2c >= 0.13.4
Obsoletes:	php-pear-%{modname}
Obsoletes:	php-yaz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extension implements a Z39.50 client for PHP using the YAZ
toolkit.

Find more information at: <http://www.indexdata.dk/phpyaz/>
<http://www.indexdata.dk/yaz/>.

%description -l pl.UTF-8
To rozszerzenie implementuje klienta Z39.50 dla PHP za pomocą narzędzi
YAZ.

Więcej informacji można znaleźć na stronach:
<http://www.indexdata.dk/phpyaz/> <http://www.indexdata.dk/yaz/>.

%prep
%setup -qc
mv %{modname}-%{version}/* .

%build
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_sysconfdir}/conf.d,%{php_extensiondir}}

install -p modules/%{modname}.so $RPM_BUILD_ROOT%{php_extensiondir}
cat <<'EOF' > $RPM_BUILD_ROOT%{php_sysconfdir}/conf.d/%{modname}.ini
; Enable %{modname} extension module
extension=%{modname}.so
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%php_webserver_restart

%postun
if [ "$1" = 0 ]; then
	%php_webserver_restart
fi

%files
%defattr(644,root,root,755)
%doc CREDITS README
%config(noreplace) %verify(not md5 mtime size) %{php_sysconfdir}/conf.d/%{modname}.ini
%attr(755,root,root) %{php_extensiondir}/%{modname}.so
