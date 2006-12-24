%define		_modname	yaz
%define		_status		stable
%define		_sysconfdir	/etc/php
%define		extensionsdir	%(php-config --extension-dir 2>/dev/null)
Summary:	%{_modname} - a Z39.50 client for PHP
Summary(pl):	%{_modname} - klient Z39.50 dla PHP
Name:		php-pecl-%{_modname}
Version:	1.0.8
Release:	1
License:	PHP
Group:		Development/Languages/PHP
Source0:	http://pecl.php.net/get/%{_modname}-%{version}.tgz
# Source0-md5:	72795905f95e7786b17b9918989eeaa6
URL:		http://pecl.php.net/package/yaz/
BuildRequires:	libxslt-devel
BuildRequires:	php-devel >= 3:5.0.0
BuildRequires:	rpmbuild(macros) >= 1.344
BuildRequires:	yaz-devel
%{?requires_php_extension}
Requires:	%{_sysconfdir}/conf.d
Obsoletes:	php-pear-%{_modname}
Obsoletes:	php-yaz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This extension implements a Z39.50 client for PHP using the YAZ
toolkit.

Find more information at: <http://www.indexdata.dk/phpyaz/>
<http://www.indexdata.dk/yaz/>.

In PECL status of this package is: %{_status}.

%description -l pl
To rozszerzenie implementuje klienta Z39.50 dla PHP za pomoc± narzêdzi
YAZ.

Wiêcej informacji mo¿na znale¼æ na stronach:
<http://www.indexdata.dk/phpyaz/> <http://www.indexdata.dk/yaz/>.

To rozszerzenie ma w PECL status: %{_status}.

%prep
%setup -q -c

%build
cd %{_modname}-%{version}
phpize
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/conf.d,%{extensionsdir}}

install %{_modname}-%{version}/modules/%{_modname}.so $RPM_BUILD_ROOT%{extensionsdir}
cat <<'EOF' > $RPM_BUILD_ROOT%{_sysconfdir}/conf.d/%{_modname}.ini
; Enable %{_modname} extension module
extension=%{_modname}.so
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
%doc %{_modname}-%{version}/{CREDITS,README}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/conf.d/%{_modname}.ini
%attr(755,root,root) %{extensionsdir}/%{_modname}.so
