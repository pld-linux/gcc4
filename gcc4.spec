#
# Conditional build:
%bcond_with	profiling	# build with profiling
%bcond_without	bootstrap	# omit 3-stage bootstrap
%bcond_with	tests		# torture gcc

%if %{without bootstrap}
%undefine	with_profiling
%endif

Summary:	GNU Compiler Collection: the C compiler and shared files
Summary(es):	Colección de compiladores GNU: el compilador C y ficheros compartidos
Summary(pl):	Kolekcja kompilatorów GNU: kompilator C i pliki wspó³dzielone
Summary(pt_BR):	Coleção dos compiladores GNU: o compilador C e arquivos compartilhados
%define	sname	gcc
Name:		%{sname}4
Version:	4.1.1
#define		_snap	20060515r113785
#define		_snap	20060517
#Release:	0.%{_snap}.1
Release:	1
Epoch:		5
License:	GPL v2+
Group:		Development/Languages
#Source0:	ftp://gcc.gnu.org/pub/gcc/prerelease-%{version}-%{_snap}/gcc-%{version}-%{_snap}.tar.bz2
Source0:	ftp://gcc.gnu.org/pub/gcc/releases/gcc-%{version}/%{sname}-%{version}.tar.bz2
# Source0-md5:	ad9f97a4d04982ccf4fd67cb464879f3
#Source0:	ftp://gcc.gnu.org/pub/gcc/snapshots/4.1-%{_snap}/gcc-4.1-%{_snap}.tar.bz2
#Source0:	gcc-4.1-%{_snap}.tar.bz2
Source1:	%{name}-optimize-la.pl
Patch0:		%{name}-info.patch
Patch1:		%{name}-nolocalefiles.patch
Patch2:		%{name}-nodebug.patch
Patch3:		%{name}-ada-link.patch
Patch4:		%{name}-sparc64-ada_fix.patch
Patch5:		%{name}-alpha-ada_fix.patch
# -fvisibility fixes...
Patch6:		%{name}-pr19664_gnu_internal.patch
Patch7:		%{name}-pr19664_libstdc++.patch
Patch8:		%{name}-pr20218.patch

# PRs
Patch10:	%{name}-pr7776.patch
Patch11:	%{name}-pr19606.patch
Patch12:	%{name}-pr24879.patch
Patch13:	%{name}-pr26435-pr20256.patch

Patch17:	%{name}-pr19505.patch
Patch18:	%{name}-pr24419.patch
Patch19:	%{name}-pr24669.patch
Patch20:	%{name}-pr17390.patch
Patch21:	%{name}-pr13676.patch
Patch22:	%{name}-pr25626.patch
Patch23:	%{name}-libstdcxx-bitset.patch

Patch25:	%{name}-libjava-multilib.patch
Patch26:	%{name}-ppc64-m32-m64-multilib-only.patch
Patch27:	%{name}-enable-java-awt-qt.patch

# 128-bit long double support for glibc 2.4
Patch30:	%{name}-ldbl-default-libstdc++.patch
Patch31:	%{name}-ldbl-default.patch

URL:		http://gcc.gnu.org/
BuildRequires:	autoconf
%{?with_tests:BuildRequires:	autogen}
BuildRequires:	automake
# binutils 2.16.91 or newer are required for compiling medium model now
BuildRequires:	binutils >= 2:2.16.91.0.1
BuildRequires:	bison
BuildRequires:	chrpath >= 0.13-2
%{?with_tests:BuildRequires:	dejagnu}
BuildRequires:	fileutils >= 4.0.41
BuildRequires:	flex
BuildRequires:	gettext-devel
BuildRequires:	glibc-devel >= 6:2.4-1
BuildRequires:	perl-base
BuildRequires:	rpmbuild(macros) >= 1.211
BuildRequires:	texinfo >= 4.1
BuildRequires:	zlib-devel
# AS_NEEDED directive for dynamic linker
# http://sources.redhat.com/ml/glibc-cvs/2005-q1/msg00614.html
# http://sources.redhat.com/ml/binutils/2005-01/msg00288.html
Requires:	binutils >= 2:2.16.90.0.1-0.3
Requires:	libgcc = %{epoch}:%{version}-%{release}
Provides:	cpp = %{epoch}:%{version}-%{release}
Obsoletes:	cpp
Obsoletes:	egcs-cpp
Obsoletes:	gcc-chill
Obsoletes:	gcc-cpp
Obsoletes:	gcc-ksi
Obsoletes:	gont
Conflicts:	glibc-devel < 2.2.5-20
BuildRoot:	%{tmpdir}/%{sname}-%{version}-root-%(id -u -n)

%define		_slibdir	/%{_lib}

%description
A compiler aimed at integrating all the optimizations and features
necessary for a high-performance and stable development environment.

This package contains the C compiler and some files shared by various
parts of the GNU Compiler Collection. In order to use another GCC
compiler you will need to install the appropriate subpackage.

%description -l es
Un compilador que intenta integrar todas las optimalizaciones y
características necesarias para un entorno de desarrollo eficaz y
estable.

Este paquete contiene el compilador de C y unos ficheros compartidos
por varias partes de la colección de compiladores GNU (GCC). Para usar
otro compilador de GCC será necesario que instale el subpaquete
adecuado.

%description -l pl
Kompilator, posiadaj±cy du¿e mo¿liwo¶ci optymalizacyjne niezbêdne do
wyprodukowania szybkiego i stabilnego kodu wynikowego.

Ten pakiet zawiera kompilator C i pliki wspó³dzielone przez ró¿ne
czê¶ci kolekcji kompilatorów GNU (GCC). ¯eby u¿ywaæ innego kompilatora
z GCC, trzeba zainstalowaæ odpowiedni podpakiet.

%description -l pt_BR
Este pacote adiciona infraestrutura básica e suporte a linguagem C ao
GNU Compiler Collection.

%package -n libgcc4
Summary:	Shared gcc library
Summary(es):	Biblioteca compartida de gcc
Summary(pl):	Biblioteka gcc
Summary(pt_BR):	Biblioteca runtime para o GCC
License:	GPL with unlimited link permission
Group:		Libraries
Obsoletes:	libgcc1

%description -n libgcc4
Shared gcc library.

%description -n libgcc4 -l es
Biblioteca compartida de gcc.

%description -n libgcc4 -l pl
Biblioteka dynamiczna gcc.

%description -n libgcc4 -l pt_BR
Biblioteca runtime para o GCC.

%prep
%setup -q -n gcc-%{version}

%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

# -fvisbility fixes...
%patch6 -p1
%patch7 -p1
%patch8 -p1

# PRs
%patch10 -p1
%patch11 -p0
%patch12 -p0
%patch13 -p1

%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1

%patch25 -p1
%patch26 -p1
%patch27 -p1

%patch30 -p0
%patch31 -p0

# because we distribute modified version of gcc...
sed -i 's:#define VERSUFFIX.*:#define VERSUFFIX " (PLD-Linux)":' gcc/version.c
perl -pi -e 's@(bug_report_url.*<URL:).*";@$1http://bugs.pld-linux.org/>";@' gcc/version.c

mv ChangeLog ChangeLog.general

%build
cd gcc
%{__autoconf}
cd ..
cd libjava
%{__autoconf}
cd classpath
%{__autoconf}
cd ../..
cp -f /usr/share/automake/config.sub .

rm -rf builddir && install -d builddir && cd builddir

CFLAGS="%{rpmcflags}" \
CXXFLAGS="%{rpmcxxflags}" \
TEXCONFIG=false \
../configure \
	--prefix=%{_prefix} \
	--with-local-prefix=%{_prefix}/local \
	--libdir=%{_libdir} \
	--libexecdir=%{_libdir} \
	--infodir=%{_infodir} \
	--mandir=%{_mandir} \
	--x-libraries=%{_libdir} \
	--enable-shared \
	--enable-threads=posix \
	--enable-languages="c" \
	--enable-c99 \
	--enable-long-long \
	--enable-nls \
	--disable-werror \
	--with-gnu-as \
	--with-gnu-ld \
	--with-demangler-in-ld \
	--with-system-zlib \
	--with-slibdir=%{_slibdir} \
%ifnarch ia64
	--without-system-libunwind \
%else
	--with-system-libunwind \
%endif
	--without-x \
	--with-long-double-128 \
%ifarch ppc ppc64
	--enable-secureplt \
%endif
	%{_target_platform}

cd ..

%{__make} -C builddir \
	%{?with_bootstrap:%{?with_profiling:profiled}bootstrap} \
	GCJFLAGS="%{rpmcflags}" \
	BOOT_CFLAGS="%{rpmcflags}" \
	STAGE1_CFLAGS="%{rpmcflags} -O0" \
	GNATLIBCFLAGS="%{rpmcflags}" \
	LDFLAGS_FOR_TARGET="%{rpmldflags}" \
	mandir=%{_mandir} \
	infodir=%{_infodir}

%{?with_tests:%{__make} -k -C builddir check 2>&1 ||:}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/lib,%{_aclocaldir},%{_datadir},%{_infodir}}

cd builddir

%{__make} -j1 install \
	mandir=%{_mandir} \
	infodir=%{_infodir} \
	DESTDIR=$RPM_BUILD_ROOT

install gcc/specs $RPM_BUILD_ROOT%{_libdir}/gcc/%{_target_platform}/%{version}

%ifarch sparc64
ln -sf	%{_bindir}/sparc64-pld-linux-gcc \
	$RPM_BUILD_ROOT%{_bindir}/sparc-pld-linux-gcc
%endif

ln -sf %{_bindir}/cpp $RPM_BUILD_ROOT/lib/cpp
ln -sf gcc $RPM_BUILD_ROOT%{_bindir}/cc
echo ".so gcc.1" > $RPM_BUILD_ROOT%{_mandir}/man1/cc.1

libssp=$(cd $RPM_BUILD_ROOT%{_libdir}; echo libssp.so.*.*.*)
mv $RPM_BUILD_ROOT{%{_libdir}/$libssp,%{_slibdir}}
ln -sf %{_slibdir}/$libssp $RPM_BUILD_ROOT%{_libdir}/libssp.so

cd ..

# include/ contains install-tools/include/* and headers that were fixed up
# by fixincludes, we don't want former
gccdir=$(echo $RPM_BUILD_ROOT%{_libdir}/gcc/*/*/)
mkdir	$gccdir/tmp

# we have to save these however
mv $gccdir/include/syslimits.h $gccdir/tmp
mv $gccdir/include/ssp $gccdir/tmp
rm -rf $gccdir/include
mv $gccdir/tmp $gccdir/include
cp $gccdir/install-tools/include/*.h $gccdir/include
# but we don't want anything more from install-tools
rm -rf $gccdir/install-tools

%find_lang gcc
%find_lang cpplib
cat cpplib.lang >> gcc.lang

# cvs snap doesn't contain (release does) below files,
# so let's create dummy entries to satisfy %%files.
[ ! -f NEWS ] && touch NEWS
[ ! -f libgfortran/AUTHORS ] && touch libgfortran/AUTHORS
[ ! -f libgfortran/README ] && touch libgfortran/README

%clean
rm -rf $RPM_BUILD_ROOT

%post
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%postun
[ ! -x /usr/sbin/fix-info-dir ] || /usr/sbin/fix-info-dir -c %{_infodir} >/dev/null 2>&1

%post	-p /sbin/ldconfig -n libgcc4
%postun	-p /sbin/ldconfig -n libgcc4

%files -f gcc.lang
%defattr(644,root,root,755)
%doc ChangeLog.general MAINTAINERS NEWS
# bugs.html faq.html
%doc gcc/{ChangeLog,ONEWS,README.Portability}
%dir %{_libdir}/gcc
%dir %{_libdir}/gcc/*
%dir %{_libdir}/gcc/*/*
%dir %{_libdir}/gcc/*/*/include
%dir %{_libdir}/gcc/*/*/include/ssp

%attr(755,root,root) %{_bindir}/*-gcc*
%attr(755,root,root) %{_bindir}/gcc
%attr(755,root,root) %{_bindir}/gccbug
%attr(755,root,root) %{_bindir}/gcov
%attr(755,root,root) %{_bindir}/cc
%attr(755,root,root) %{_bindir}/cpp

%{_mandir}/man1/cc.1*
%{_mandir}/man1/cpp.1*
%{_mandir}/man1/gcc.1*
%{_mandir}/man1/gcov.1*

%{_infodir}/cpp*
%{_infodir}/gcc*

%attr(755,root,root) /lib/cpp

%attr(755,root,root) %{_slibdir}/lib*.so
%{_libdir}/libssp.a
%{_libdir}/libssp.la
%attr(755,root,root) %{_libdir}/libssp.so
%{_libdir}/libssp_nonshared.a
%{_libdir}/libssp_nonshared.la
%{_libdir}/gcc/*/*/libgcov.a
%{_libdir}/gcc/*/*/libgcc.a
%{_libdir}/gcc/*/*/libgcc_eh.a
%{_libdir}/gcc/*/*/specs
%{_libdir}/gcc/*/*/crt*.o
%attr(755,root,root) %{_libdir}/gcc/*/*/cc1
%attr(755,root,root) %{_libdir}/gcc/*/*/collect2

%{_libdir}/gcc/*/*/include/*.h
%{_libdir}/gcc/*/*/include/ssp/*.h

%files -n libgcc4
%defattr(644,root,root,755)
%attr(755,root,root) %{_slibdir}/lib*.so.*
