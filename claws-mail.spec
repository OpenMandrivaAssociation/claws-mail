%define pre         %nil
%define name        claws-mail
%define version     2.9.1
%define version_name    %{name}-%{version}
%define release     %mkrel 1
%define iconname    %{name}.png
%define Group       Networking/Mail
%define Summary     Enhanced version of the Sylpheed e-mail client
 

Summary:            %{Summary}
Name:               %{name}
Version:            %{version}
Release:            %{release}
Source:             %{name}-%{version}.tar.bz2 
License:            GPL
URL:                http://www.claws-mail.org/
Group:              %{Group}
Epoch:              1
Buildroot:          %{_tmppath}/%{version_name}-%{release}-buildroot
BuildRequires:      openldap-devel
BuildRequires:      aspell-devel 
BuildRequires:      libgdk_pixbuf2.0-devel >= 2.6.4
BuildRequires:      pilot-link-devel
BuildRequires:      ImageMagick
BuildRequires:      libltdl-devel
BuildRequires:      multiarch-utils
BuildRequires:      libetpan-devel >= 0.42
BuildRequires:      libgnomeprintui-devel
BuildRequires:      spamassassin-spamd >= 3.0.0
BuildRequires:      libclamav-devel
BuildRequires:      gpgme-devel > 0.4.5
BuildRequires:      desktop-file-utils
BuildRequires:      libsm-devel
Requires:           common-licenses 
Requires:           aspell-dictionary    
Obsoletes:          %{name}-tools
Provides:           %{name}-tools
# Fix upgrade from mdk 2006:
Obsoletes:          sylpheed-claws2
Obsoletes:	    sylpheed-claws

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

This is an improved version over the "bare" sylpheed package.  It has
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

%package -n %name-devel
Summary:    %{Summary}
Group:   Development/Other
Requires:  %{name} = 1:%{version}
Requires:          openldap-devel
Requires:          aspell-devel >= 0.50, aspell-dictionary
Requires:          libgdk_pixbuf2.0-devel >= 2.6.4
Requires:          pilot-link-devel
Requires:          libltdl-devel
Requires:          libetpan-devel >= 0.42
Requires:          libgnomeprintui-devel
Requires:          gpgme-devel > 0.4.5
Obsoletes: sylpheed-claws2-devel
Obsoletes: sylpheed-claws-devel

%description -n %name-devel
Pkg contains the header files needed for developing with sylpheed-claws.

%package spamassassin-plugin
Summary: Spamassassin-plugin for %{name}
Group: %{Group}
Requires: %{name} = 1:%{version}
Requires: spamassassin-spamd
Provides: sylpheed-claws2-spamassassin-plugin
Obsoletes: sylpheed-claws2-spamassassin-plugin

%description spamassassin-plugin
This package uses the spamd SpamAssassin server to check for spam mail.
- See README for configuration and set-up info.

%package clamav-plugin
Summary: Clamav plugin for %name
Group: %Group 
Requires: %{name} = 1:%{version}
Requires: clamav
Provides: sylpheed-claws2-clamav-plugin
Obsoletes: sylpheed-claws2-clamav-plugin

%description clamav-plugin
This plugin will scan incoming messages for viruses using 
Clam AntiVirus.
- See README for configuration and set-up info.

%package dillo_viewer-plugin
Summary: Dillo-plugin for %{name}
Group: %{Group}
Requires: %{name} = 1:%{version}
Requires: dillo
Provides: sylpheed-claws2-dillo_viewer-plugin
Obsoletes: sylpheed-claws2-dillo_viewer-plugin

%description dillo_viewer-plugin
This plugin uses the Dillo browser to view text/html MIME parts inside
%name.

%package trayicon-plugin
Summary: Notafication icon for %name
Group: %{Group}
Requires: %{name} = 1:%{version}
Provides: sylpheed-claws2-trayicon-plugin
Obsoletes: sylpheed-claws2-trayicon-plugin

%description trayicon-plugin
This plugin puts a little icon into the system tray.
System trays known to work are Gnome2 and KDE 3.
- See README for additional info.

%package pgpcore-plugin
Summary: PGP core plugin for %name
Group: %{Group}
Requires: %{name} = 1:%{version}
Provides: sylpheed-claws2-pgpcore-plugin
Obsoletes: sylpheed-claws2-pgpcore-plugin

%description pgpcore-plugin
This plugin handles PGP core operations. It is used by other
plugins, like the pgpmime plugin and pgpinline plugin.

%package pgpmime-plugin
Summary: PGP plgin for %name
Group: %{Group}
Requires: %{name} = 1:%{version}
Requires: %{name}-pgpcore-plugin = 1:%{version}-%{release}
Provides: sylpheed-claws2-pgpmime-plugin
Obsoletes: sylpheed-claws2-pgpmime-plugin

%description pgpmime-plugin
This plugin verifies signatures and decrypts messages.

%package pgpinline-plugin
Summary: PGP (inline) plugin for %name
Group: %{Group}
Requires: %{name} = 1:%{version}
Requires: %{name}-pgpcore-plugin = 1:%{version}
Provides: sylpheed-claws2-pgpinline-plugin
Obsoletes: sylpheed-claws2-pgpinline-plugin

%description pgpinline-plugin
This plugin enables signature verification of digitally
signed messages, and decryption of encrypted messages.

%package bogofilter-plugin
Summary: Bogofilter plugin for %name
Group: %{Group}
BuildRequires: bogofilter
Requires: %{name} = 1:%{version}
Requires: bogofilter
 

%description bogofilter-plugin
This plugin provides spam filtering and learning

%prep
%setup -q
 
%build

%configure2_5x --enable-aspell --enable-jpilot --enable-openssl --enable-ldap \
                         --enable-gpgme --enable-crash_dialog --enable-spamassassin-plugin \
                         --enable-dillo_viewer-plugin --enable-mathml_viewer-plugin \
                         --enable-trayicon-plugin  --enable-clamav-plugin --enable-bogofilter

%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std  

# multiarch
%multiarch_includes %{buildroot}%{_includedir}/%{name}/config.h 
 
##remove duplicate man#
rm -rfd  $RPM_BUILD_ROOT/usr/share/man
## remove unneeded file 
rm -rf tools/Makefile*   
## remove unneeded devel files
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.*a

mkdir -p %{buildroot}{%{_miconsdir},%{_iconsdir},%{_liconsdir},%{_menudir}}
convert %{name}.png -geometry 48x48 %{buildroot}%{_liconsdir}/%{iconname}
convert %{name}.png -geometry 32x32 %{buildroot}%{_iconsdir}/%{iconname}
convert %{name}.png -geometry 16x16 %{buildroot}%{_miconsdir}/%{iconname}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/
install -m644 %{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applications/
install -m644 %{name}.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/

mkdir -p $RPM_BUILD_ROOT%{_datadir}/claws-mail/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/claws-mail/manual/

cat > %{buildroot}%{_menudir}/%{name} << EOF
?package(%{name}):\
    command="%{name}" \
        icon="%{iconname}" \
    title="Sylpheed Claws" \
    longtitle="%{Summary}" \
    needs="x11" \         
    section="Internet/Mail" \
        xdg="true"
EOF

desktop-file-install --vendor="" \
--add-category="X-MandrivaLinux-Internet-Mail" \
--dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/* 
 
%find_lang %{name}

%post
%{update_menus}
     
%postun
%{clean_menus}

%clean
rm -rf %{buildroot} 

%files -f %{name}.lang
%defattr(-,root,root)
%doc ABOUT-NLS COPYING AUTHORS ChangeLog* NEWS README* INSTALL* TODO*
%doc RELEASE_NOTES
%doc tools
%{_bindir}/%{name}
%{_bindir}/sylpheed-claws
%dir %{_datadir}/%{name}
#%{_datadir}/%{name}/manual/*/%{name}-manual.* 
%{_datadir}/applications/claws-mail.desktop
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/plugins
%{_menudir}/%{name}
%{_miconsdir}/%{iconname}
%{_iconsdir}/%{iconname}
%{_liconsdir}/%{iconname}
%{_datadir}/icons/hicolor/48x48/apps/claws-mail.png
%dir %{_docdir}/claws-mail
%doc %{_docdir}/claws-mail/RELEASE_NOTES
%dir %{_docdir}/claws-mail/manual
%dir %{_docdir}/claws-mail/manual/en
%doc %{_docdir}/claws-mail/manual/en/*
%dir %{_docdir}/claws-mail/manual/es
%doc %{_docdir}/claws-mail/manual/es/*
%dir %{_docdir}/claws-mail/manual/en
%doc %{_docdir}/claws-mail/manual/en/*
%dir %{_docdir}/claws-mail/manual/fr
%doc %{_docdir}/claws-mail/manual/fr/*
%dir %{_docdir}/claws-mail/manual/pl
%doc %{_docdir}/claws-mail/manual/pl/*

%files -n %name-devel
%defattr(-,root,root)
%{_includedir}/%{name}
%{_libdir}/pkgconfig/claws-mail.pc
%multiarch %{multiarch_includedir}/%{name}/config.h

%files spamassassin-plugin
%defattr(-,root,root)
%doc src/plugins/spamassassin/README
%{_libdir}/%{name}/plugins/spamassassin*.so                                       

%files clamav-plugin
%defattr(-,root,root)
%doc src/plugins/clamav/README
%{_libdir}/%{name}/plugins/clamav*.so

%files dillo_viewer-plugin
%defattr(-,root,root)
%doc src/plugins/clamav/README
%{_libdir}/%{name}/plugins/dillo*.so 

%files trayicon-plugin
%defattr(-,root,root)
%doc src/plugins/trayicon/README
%{_libdir}/%{name}/plugins/trayicon.so

%files pgpcore-plugin
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/pgpcore.so

%files pgpmime-plugin
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/pgpmime.so
%{_libdir}/%{name}/plugins/pgpmime.deps

%files pgpinline-plugin
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/pgpinline.so
%{_libdir}/%{name}/plugins/pgpinline.deps

%files bogofilter-plugin
%defattr(-,root,root)
%{_libdir}/%{name}/plugins/bogofilter.so 


