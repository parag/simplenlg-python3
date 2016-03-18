# java -cp lib/py4j0.6.jar:lib/simplenlg-3.8.jar:. Py4JServer 8080
from py4j.java_gateway import JavaGateway, GatewayClient, java_import

gateway = JavaGateway(GatewayClient(port=8080))

# Import the SimpleNLG classes
java_import(gateway.jvm, "simplenlg.features.*")
java_import(gateway.jvm, "simplenlg.realiser.*")
java_import(gateway.jvm, "simplenlg.framework.*")
java_import(gateway.jvm, "simplenlg.lexicon.*")
java_import(gateway.jvm, "simplenlg.phrasespec.*")

# Define aliases so that we don't have to use the gateway.jvm prefix.
NPPhraseSpec = gateway.jvm.NPPhraseSpec
PPPhraseSpec = gateway.jvm.PPPhraseSpec
VPPhraseSpec = gateway.jvm.VPPhraseSpec
SPhraseSpec = gateway.jvm.SPhraseSpec
InterrogativeType = gateway.jvm.InterrogativeType
NLGFactory = gateway.jvm.NLGFactory
Realiser = gateway.jvm.Realiser
TextSpec = gateway.jvm.TextSpec
Tense = gateway.jvm.Tense
Form = gateway.jvm.Form


phrase = SPhraseSpec()

cand_type = NPPhraseSpec("candidates")
cand_type.addModifier("good")
cand_type.addModifier("JAVA")

prep = PPPhraseSpec()
prep.setPreposition("those are")
prep.addComplement("hard working")
prep.addComplement("sincere")
prep.addComplement("smart")
cand_type.addModifier(prep)

phrase.setInterrogative(gateway.jvm.InterrogativeType.YES_NO)
phrase.setSubject("you")
phrase.setVerb("want")
phrase.addComplement(cand_type)

realiser = Realiser()
output = realiser.realiseDocument(phrase).strip()
print (output)
