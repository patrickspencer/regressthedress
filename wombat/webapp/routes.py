from flask import Blueprint, render_template
from wombat.models import dbsession
main = Blueprint('main', __name__, url_prefix='/')

text = """Lorem ipsum dolor sit amet, fabellas assueverit et has, vim ei timeam dolores percipitur. Quo dicit maiestatis an, duo quaestio quaerendum ad, no nihil tibique tractatos cum. Ea dolorum facilis temporibus mel, ea qui virtute scripserit. Omnis mandamus interesset ei cum, augue eripuit quo an, quod elit inani ius ea. Quo ex semper feugait, eu prompta sanctus duo, cu vis eius consequat suscipiantur.

Pro cu aperiam gloriatur, ius eu utroque recusabo, esse scribentur id vim. Saperet delenit ceteros vix et. Nam ignota abhorreant ad, eam ad novum omnesque. Pri prima docendi postulant id, at vix adhuc feugiat adolescens. Ad melius sanctus his, ei vim quis tamquam. Numquam sapientem necessitatibus vis ex, usu ei doctus prompta efficiendi.

No nec audire equidem accommodare, stet option adipisci et ius. His ad meliore dissentiunt. Noster inermis conclusionemque an vim, vitae voluptatibus ad pro. Probo euismod recusabo ei eum, inermis perfecto id eos.

Te pro assum quidam posidonium, scripta facilis appareat ut qui, vim velit reprehendunt ne. Doming option volumus an sit, natum tempor prompta eos an, vidit possim incorrupte duo ex. Facilis convenire eu has. Id vim mazim scribentur, id his cetero antiopam theophrastus. Sea atomorum volutpat et, sumo molestiae sit ei, cu duo lorem civibus.

An vix fabellas tacimates, eu ius congue alterum recteque, no deleniti splendide similique per. Has fugit efficiendi id. Pri partem maiorum ei, his eu mandamus elaboraret. Cu vim accumsan perpetua temporibus, dicat dicta mollis mei eu. Est tacimates maluisset no, usu in erant clita veniam, ut duo quidam inimicus qualisque."""

@main.route("/")
def index():
    return render_template('index.jinja2', text=text)
