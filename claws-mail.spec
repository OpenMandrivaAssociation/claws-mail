%define pre %nil
%define version_name %{name}-%{version}
%define iconname %{name}.png
%define Group Networking/Mail

Summary:	The user-friendly, lightweight and fast GTK2 based email client
Name:		claws-mail
Version:	3.5.0
Release:	%mkrel 3
Epoch:		1
License:	GPLv3+
Group:		%{Group}
URL:		http://www.claws-mail.org
Source0:	http://downloads.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.bz2
Patch0:		claws-mail-3.3.0-fix-desktop-file.patch
Buildroot:	%{_tmppath}/%{version_name}-%{release}-buildroot
BuildRequires:	gtk2-devel
BuildRequires:	openldap-devel
BuildRequires:	aspell-devel
BuildRequires:	libgdk_pixbuf2.0-devel >= 2.6.4
BuildRequires:	pilot-link-devel
BuildRequires:	libltdl-devel
BuildRequires:	multiarch-utils
BuildRequires:	libetpan-devel >= 0.42
%if %mdkversion < 200700
BuildRequires:	libgnomeprintui-devel
%endif
BuildRequires:	spamassassin-spamd >= 3.0.0
BuildRequires:	gpgme-devel > 0.4.5
BuildRequires:	libsm-devel
%if %mdkversion > 200800
BuildRequires: imagemagick
%else
BuildRequires: ImageMagick
%endif
%if %mdkversion > 200800
BuildRequires:	compface-devel
Requires:	compface
%endif
%if %mdkversion > 200700
BuildRequires:	libdbus-glib-devel
%endif
#%if %mdkversion >= 200900
#BuildRequires:	libnm_util-devel
#BuildRequires:	libnm_glib-devel
#%endif
Requires:	common-licenses
Requires:	aspell-dictionary
Obsoletes:	%{name}-tools
Provides:	%{name}-tools
# Fix upgrade from mdk 2006:
Obsoletes:	sylpheed-claws2
Obsoletes:	sylpheed-claws
#Clamav is dropped
Obsoletes:	claws-mail-clamav-plugin
## additinal feature which can be enabled at configure are jconv
## jconv
## A general purpose Japanese code conversion tool.
## BuildRequires: jconv
## Requires: jconv
Buildroot:	%{_tmppath}/%{version_name}-%{release}-buildroot


%description
Claws-Mail is an e-mail client (and news reader) based on GTK+2, running
on X Window System, and aiming for:
 * Quick response
 * Graceful, and sophisticated interface
 * Easy configuration, intuitive operation
 * Abundant features
The appearance and interface are similar to some popular e-mail clients for
Windows, such as Outlook Express, Becky!, and Datula. The interface is also
designed to emulate the mailers on Emacsen, and almost all commands are
accessible with the keyboard.

The messages are managed by MH format, and you'll be able to use it together
with another mailer based on MH format (like Mew). You can also utilize
fetchmail or/and procmail, and external programs on receiving (like inc or
imget).

This is an improved version over the "bare" sylpheed package. It has
some additional features, and also extends existing features.

Addtitional features include:
    o Scoring
    o Spell checking
    o Return receipts

Improved features include:
    o SMTP Auth
    o Filtering
    o MIME attachments
    o Integrated News reader
    o Automatic mail checking
    o Line-wrapping
    o XML-based addressbook
    o Newly arrived and unread message management
    o Printing
    o GnuPG support
    o Address book supports JPilot, LDAP, LDIF, and vCard data files

For a complete listing of Features: http://www.claws-mail.org/features.php

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	gtk2-devel
Requires:	openldap-devel
Requires:	aspell-devel >= 0.50
Requires:	aspell-dictionary
Requires:	libgdk_pixbuf2.0-devel >= 2.6.4
Requires:	pilot-link-devel
Requires:	libltdl-devel
Requires:	libetpan-devel >= 0.42
%if %mdkversion < 200700
Requires:	libgnomeprintui-devel
%endif
Requires:	gpgme-devel > 0.4.5
Obsoletes:	sylpheed-claws2-devel
Obsoletes:	sylpheed-claws-devel

%description -n %{name}-devel
Development files and headers for %{name}

%package bogofilter-plugin
Summary:	Bogofilter plugin for %{name}
Group:		%{Group}
BuildRequires:	bogofilter
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	bogofilter

%description bogofilter-plugin
Enables the scanning of incoming mail received from a 
POP, IMAP, or LOCAL account using Bogofilter. It can 
optionally delete mail identified as spam or save it 
to a designated folder. Bogofilter is a pure Bayesian 
filter, therefore it has better speed performance 
than SpamAssassin but might catch less spam.

%package dillo_viewer-plugin
Summary:	Dillo HTML viewer plugin for %{name}
Group:		%{Group}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	dillo
Provides:	sylpheed-claws2-dillo_viewer-plugin
Obsoletes:	sylpheed-claws2-dillo_viewer-plugin

%description dillo_viewer-plugin
This plugin uses the Dillo browser to view text/html
MIME parts inside %{name}.

%package pgpcore-plugin
Summary:	PGP core plugin for %{name}
Group:		%{Group}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	sylpheed-claws2-pgpcore-plugin
Obsoletes:	sylpheed-claws2-pgpcore-plugin

%description pgpcore-plugin
Handles core PGP functions and is a dependency of both 
the PGP/Inline and PGP/MIME plugins.

%package pgpinline-plugin
Summary:	PGP/Inline plugin for %{name}
Group:		%{Group}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-pgpcore-plugin = %{epoch}:%{version}-%{release}
Provides:	sylpheed-claws2-pgpinline-plugin
Obsoletes:	sylpheed-claws2-pgpinline-plugin

%description pgpinline-plugin
Handles PGP/Inline signed and/or encrypted mails.
You can decrypt mails, verify signatures or sign 
and encrypt your own mails.

%package pgpmime-plugin
Summary:	PGP/MIME plugin for %{name}
Group:		%{Group}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	%{name}-pgpcore-plugin = %{epoch}:%{version}-%{release}
Provides:	sylpheed-claws2-pgpmime-plugin
Obsoletes:	sylpheed-claws2-pgpmime-plugin

%description pgpmime-plugin
Handles PGP/MIME signed and/or encrypted mails.
You can decrypt mails, verify signatures or sign
and encrypt your own mails.

%package spamassassin-plugin
Summary:	Spamassassin-plugin for %{name}
Group:		%{Group}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Requires:	spamassassin-spamd
Provides:	sylpheed-claws2-spamassassin-plugin
Obsoletes:	sylpheed-claws2-spamassassin-plugin

%description spamassassin-plugin
Enables the scanning of incoming mail received from a 
POP, IMAP, or LOCAL account using SpamAssassin

See README for configuration and set-up info.

%package trayicon-plugin
Summary:	Notafication icon for %{name}
Group:		%{Group}
Requires:	%{name} = %{epoch}:%{version}-%{release}
Provides:	sylpheed-claws2-trayicon-plugin
Obsoletes:	sylpheed-claws2-trayicon-plugin

%description trayicon-plugin
Places an icon in the system tray that indicates 
whether you have any new mail. A tooltip also shows 
the current new, unread and total number of messages, 
and a contextual menu allows the most common operations.

See README for additional info.

%prep
%setup -q
%patch0 -p0

%build

%configure2_5x \
	--enable-aspell \
	--enable-jpilot \
	--enable-openssl \
	--enable-ldap \
	--enable-gpgme \
	--enable-crash-dialog \
	--enable-spamassassin-plugin \
	--enable-dillo-viewer-plugin \
	--enable-trayicon-plugin \
	--enable-bogofilter \
	--enable-ipv6 \
%if %mdkversion > 200800
	--enable-compface \
%endif
	--disable-rpath \
	--disable-static

%make

%check
make check

%install
rm -rf %{buildroot}
%makeinstall_std

# multiarch
%multiarch_includes %{buildroot}%{_includedir}/%{name}/config.h

##remove duplicate man#
rm -rfd  %{buildroot}%{_mandir}
## remove unneeded file
#rm -rf tools/Makefile*
## remove unneeded devel files
rm -f %{buildroot}%{_libdir}/%{name}/plugins/*.*a

mkdir -p %{buildroot}%{_iconsdir}/hicolor/{16x16,32x32,48x48,64x64,128x128}/apps
convert %{name}.png -geometry 16x16 %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{iconname}
convert %{name}.png -geometry 32x32 %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{iconname}
install -m644 %{name}.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{iconname}
install -m644 %{name}-64x64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{iconname}
install -m644 %{name}-128x128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{iconname}

mkdir -p %{buildroot}%{_datadir}/applications/
install -m644 %{name}.desktop %{buildroot}%{_datadir}/applications/

cp -a ABOUT-NLS AUTHORS NEWS README* TODO* RELEASE_NOTES tools %{buildroot}%{_docdir}/claws-mail/
rm -f %{buildroot}%{_docdir}/claws-mail/tools/Makefile*

%find_lang %{name}

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_bindir}/%{name}
%{_bindir}/sylpheed-claws
%{_datadir}/applications/claws-mail.desktop
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_iconsdir}/hicolor/*/apps/*.png
%{_docdir}/claws-mail

%files devel
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/pkgconfig/claws-mail.pc
%multiarch %{multiarch_includedir}/%{name}/config.h

%files bogofilter-plugin
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/bogofilter.so

%files dillo_viewer-plugin
%defattr(-,root,root)
%doc src/plugins/dillo_viewer/README
%{_libdir}/%{name}/plugins/dillo*.so

%files pgpcore-plugin
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/pgpcore.so

%files pgpinline-plugin
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/pgpinline.so
%{_libdir}/%{name}/plugins/pgpinline.deps

%files pgpmime-plugin
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/pgpmime.so
%{_libdir}/%{name}/plugins/pgpmime.deps

%files spamassassin-plugin
%defattr(-,root,root)
%doc src/plugins/spamassassin/README
%{_libdir}/%{name}/plugins/spamassassin*.so

%files trayicon-plugin
%defattr(-,root,root)
%doc src/plugins/trayicon/README
%{_libdir}/%{name}/plugins/trayicon.so
