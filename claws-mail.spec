%define _disable_ld_no_undefined 1

# There are perl scripts in docs/tools and we don't want to install perl
# modules required by these scripts
%define __noautoreq 'perl(.*)'

%define version_name %{name}-%{version}
%define iconname %{name}.png
%define Group Networking/Mail

Summary:	The user-friendly, lightweight and fast GTK2 based email client
Name:		claws-mail
Version:	3.9.0
Release:	1
Epoch:		1
License:	GPLv3+
Group:		%{Group}
URL:		http://www.claws-mail.org
Source0:	http://downloads.sourceforge.net/sylpheed-claws/%{name}-%{version}.tar.bz2
# from Debian
Patch0:		claws-mail-3.7.6-trashed-read.patch
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dbus-1) >= 0.60
BuildRequires:	pkgconfig(dbus-glib-1) >= 0.60
BuildRequires:	pkgconfig(enchant) >= 1.0.0
BuildRequires:	pkgconfig(glib-2.0) >= 2.6
BuildRequires:	pkgconfig(gmodule-2.0) >= 2.6
BuildRequires:	pkgconfig(gnutls) >= 2.2
BuildRequires:	pkgconfig(gobject-2.0) >= 2.6
BuildRequires:	pkgconfig(gthread-2.0) >= 2.6
BuildRequires:	pkgconfig(gtk+-2.0) >= 2.16
BuildRequires:	pkgconfig(libgnome-2.0) >= 2.0
BuildRequires:	pkgconfig(libstartup-notification-1.0) >= 0.5
BuildRequires:	pkgconfig(NetworkManager) >= 0.6.2
BuildRequires:	docbook-utils
BuildRequires:	libsm-devel
BuildRequires:	openldap-devel
BuildRequires:	pilot-link-devel
BuildRequires:	libetpan-devel >= 0.42
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	valgrind-devel
BuildRequires:	spamassassin-spamd >= 3.0.0
BuildRequires:	libgcrypt-devel
BuildRequires:	gpgme-devel > 0.4.5
BuildRequires:	imagemagick
BuildRequires:	compface-devel

Requires:	compface
Requires:	rootcerts
Requires:	common-licenses
Requires:	aspell-dictionary
Obsoletes:	%{name}-tools < %{EVRD}
Provides:	%{name}-tools
Obsoletes:	%{name}-spamassassin-plugin < %{EVRD}
#Clamav is dropped
Obsoletes:	claws-mail-clamav-plugin < %{EVRD}
## additinal feature which can be enabled at configure are jconv
## jconv
## A general purpose Japanese code conversion tool.
## BuildRequires: jconv
## Requires: jconv

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
Requires:	%{name} = %{EVRD}
Requires:	aspell-dictionary

%description -n %{name}-devel
Development files and headers for %{name}.

%package bogofilter-plugin
Summary:	Bogofilter plugin for %{name}
Group:		%{Group}
BuildRequires:	bogofilter
Requires:	%{name} = %{EVRD}
Requires:	bogofilter

%description bogofilter-plugin
Enables the scanning of incoming mail received from a POP, IMAP, or LOCAL
account using Bogofilter. It can optionally delete mail identified as spam
or save it to a designated folder. Bogofilter is a pure Bayesian filter,
therefore it has better speed performance than SpamAssassin but might catch
less spam.

%package smime-plugin
Summary:	S/Mime plugin for %{name}
Group:		%{Group}
Requires:	%{name} = %{EVRD}

%description smime-plugin
This plugin allows to use S/Mime signatures and encryptions in Claws Mail.

%package dillo_viewer-plugin
Summary:	Dillo HTML viewer plugin for %{name}
Group:		%{Group}
Requires:	%{name} = %{EVRD}
Requires:	dillo

%description dillo_viewer-plugin
This plugin uses the Dillo browser to view text/html MIME parts
inside Claws Mail.

%package pgpcore-plugin
Summary:	PGP core plugin for %{name}
Group:		%{Group}
Requires:	%{name} = %{EVRD}

%description pgpcore-plugin
Handles core PGP functions and is a dependency of both the PGP/Inline and
PGP/MIME plugins.

%package pgpinline-plugin
Summary:	PGP/Inline plugin for %{name}
Group:		%{Group}
Requires:	%{name} = %{EVRD}
Requires:	%{name}-pgpcore-plugin = %{EVRD}

%description pgpinline-plugin
Handles PGP/Inline signed and/or encrypted mails. You can decrypt mails,
verify signatures or sign and encrypt your own mails.

%package pgpmime-plugin
Summary:	PGP/MIME plugin for %{name}
Group:		%{Group}
Requires:	%{name} = %{EVRD}
Requires:	%{name}-pgpcore-plugin = %{EVRD}

%description pgpmime-plugin
Handles PGP/MIME signed and/or encrypted mails. You can decrypt mails, verify
signatures or sign and encrypt your own mails.

%package spamassassin-plugin
Summary:	Spamassassin-plugin for %{name}
Group:		%{Group}
Requires:	%{name} = %{EVRD}
Requires:	spamassassin-spamd

%description spamassassin-plugin
Enables the scanning of incoming mail received from a POP, IMAP, or LOCAL
account using SpamAssassin. See README for configuration and set-up info.

%package trayicon-plugin
Summary:	Notafication icon for %{name}
Group:		%{Group}
Requires:	%{name} = %{EVRD}

%description trayicon-plugin
Places an icon in the system tray that indicates whether you have any new mail.
A tooltip also shows the current new, unread and total number of messages, and
a contextual menu allows the most common operations. See README for additional
info.

%prep
%setup -q
%patch0 -p1

%build
%configure2_5x \
	--enable-enchant \
	--enable-jpilot \
	--enable-ldap \
	--enable-crash-dialog \
	--enable-spamassassin-plugin \
	--enable-dillo-viewer-plugin \
	--enable-trayicon-plugin \
	--enable-ipv6 \
	--enable-compface \
	--enable-gnutls \
	--enable-networkmanager-support \
	--disable-rpath \
	--disable-static

%make LIBTOOL=%{_bindir}/libtool

%check
make check

%install
%makeinstall_std

##remove duplicate man#
rm -rf  %{buildroot}%{_mandir}
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

%files -f %{name}.lang
%{_bindir}/%{name}
%{_bindir}/sylpheed-claws
%{_datadir}/applications/claws-mail.desktop
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_iconsdir}/hicolor/*/apps/*.png
%{_docdir}/claws-mail

%files devel
%{_includedir}/%{name}
%{_libdir}/pkgconfig/claws-mail.pc

%files bogofilter-plugin
%{_libdir}/%{name}/plugins/bogofilter.so

%files smime-plugin
%{_libdir}/%{name}/plugins/smime.so
%{_libdir}/%{name}/plugins/smime.deps

%files dillo_viewer-plugin
%doc src/plugins/dillo_viewer/README
%{_libdir}/%{name}/plugins/dillo*.so

%files pgpcore-plugin
%{_libdir}/%{name}/plugins/pgpcore.so

%files pgpinline-plugin
%{_libdir}/%{name}/plugins/pgpinline.so
%{_libdir}/%{name}/plugins/pgpinline.deps

%files pgpmime-plugin
%{_libdir}/%{name}/plugins/pgpmime.so
%{_libdir}/%{name}/plugins/pgpmime.deps

%files spamassassin-plugin
%doc src/plugins/spamassassin/README
%{_libdir}/%{name}/plugins/spamassassin*.so

%files trayicon-plugin
%doc src/plugins/trayicon/README
%{_libdir}/%{name}/plugins/trayicon.so

