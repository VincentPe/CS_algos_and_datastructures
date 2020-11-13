# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    stack_idx = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append(next)
            stack_idx.append(i+1)

        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i+1
            elif are_matching(opening_brackets_stack[-1], next):
                del opening_brackets_stack[-1]
                del stack_idx[-1]
            else:
                return i+1
    if len(opening_brackets_stack) > 0:
        return stack_idx[-1]
    else:
        return 'Success'


#text = 'X{89}{w}(gy)b?r(;)[CS[e]Ko]5{eMi}[n(;);J](o)ls{}a(5NW(RA)m)BA.[][N(V()ka)1x]()()BS{w.}r[?j(7F)Zw](v)G;[B[U]L][]{Y}d([ud])I[Z];(V)[7I(w(W)lF)Q]L{U(B)g}{b}o(M)B[P.]?{wm(OA20)}()(1)(;j{u}v)k[7nX.]En(pC{X})wK[x()E]Mh(Y)[f]()b[[];:][]A:({7})r[:]3wU[olDn]MB1{}ch[]{PZ([o])}4s{{ivH}}M4[[CM;]IZ][][]af[{}]y{8K}E[Giq[slK]Jwi]{}h{;1I}i(n)[F](fo)8O(cn())[ri]M(9[n]dAV2)[P.D[j]!][][]d{[]}Hk[{b6}hRwi]()BC{l}4()T()nU([!r]C?)GI{S}x()9G[eY4MH,U]G(k8[,T{kU}f]yV){7p{R}}l:(x4){}((F);y)?{j}{t}g{R}Ca{}p{(dN)8R}Sfa[?]e[0]()v{9}([,])Da(3)x{fw[15]},N[[{D[K]9}]b?]?Zf()()U{o{3[()]Nl}J}Wx()BB[{[S]z}]J(yZ0q)x[dq[([])]q]p[[]T]7TE(U[V])bSxd(!Q)I(e8:[H(3)KDo]p){f[u]k}UBe{}(9i(T[S0a])C:).F[:EM[:[SM]a?;]]qI[Q()u]y{}(.()I)L(4)dSB(r){7[]}[[];L][](SP(6d)f)g{.}W()b{3eU}[]6{9}7(J)()(A)mr[p](){()E},()VS(){!U}IA!?{}F7(Z){}[3]{L{m}e72}2u(R()){}4i[rDo],p[2][H6]t.((D))[]uJ[{}t]RV(4{aNqn}q)[7X],q9(0){}F{i}{K}f(a()y){J{0.}WL}6[]Y{O}mHG{{3}86u}h(N{(I)}){}v(Fr)XyEct[;[oL]0]Dp{Xj3}L[][0dH7]g[B(Y;)BOm:]b{}Q{}{y}t(L)z{SG}{{8}}U{h}E[i[]r]{{}}n[D{sJ}:9H]g[]{r}v{bn}j?([]wa){U}e[6]0()Rx[2]C{Ua}!(i)XM[]1;[C!]()q(c2{J{H}s}eQh)1is{sb[o{8}O]H}h{k}[(X)]e{h{V}5}(R)K[]U[H[(B8)x]?]ly{(1()F)}Tp[f([N]U:)][hN4]{D}b{},p(zG{L}e)h(b(9f))()zy{YQ}?M[kq]U2[z9]i(H)Z[]gQ{r}Ik{}fX[k](Yo{O}xN)7k{e}(rS(Uq))([cx])([[]V]H)Rc{(1SZ).l}[[]4e]V{s,{z}}r((o)1f!)xUL()o[t[]]W{(v)jS}o[(1{})Y]g[y]{Qj{}3}7{HH}mK{n}{f}5(t)YB[](C){e}0[{4}]{?}vU{3{Y{U}xX}}LC[y()](y())3i(bPR[6]0)[5](y1Q)p[?][[J]Ey]ZH{S}U(z)Z{qx{VS1{Lz}Yyvy}A}(h)[P]H(oC{})q{};Iq[7]k(7c[F{Bv}Z]?)tG{1G(x)}R(5{D}8)tG{!}P[1]J(hy)0d{r}Z({Wqs};X){}H{S}(L)U(r{K}o6){}D()4?[]H[](![19w]HZ)Z[m][A]2{bDE[J.]uk}[]A[v[]]aJ{}T1[]{3k.[h{?}G]}v{r(.())}(;[tF[JE]])[({}L)4Z]e[K]p{S}J{JMV9{e}x}2()5()h(8){MY[]R;}3[]{o}()b(Px){9}R(A)Ui[]v{J()}{PPh}wC(Wm{Z[s(Y)Of]u}Yg)Q[]{8[j{ux}7];9}B[rup[(YWe)]i0f]CP(ex){}yS(CY)LJ{P[h]f}dD[(q[]z)]3()o[]1[4K()]S{}()3(){{cVa{{j4G}T}aM}0b}[]J(Og)y{h}{5[{60m}]w}mK[p]{}K[usi9(k)B]Ds[]{Ra};{8Q}4{}9m,([])G{;}({S})[7B]L{G}mZ(i())M![]v[u]z(PE5IZ()hw)w()p[JwJ]{[]}((r))H([w[]])k{}T[6.k]{(A)C}XV'
#find_mismatch(text)



def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)


if __name__ == "__main__":
    main()