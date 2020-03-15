const index = 'stocks'

exports.get_all = async (req, res, next) => {
  try {

    res.json({data: results})
  } catch (e) {
    res.status(500).send(e)
  }
}

exports.get = async (req, res, next) => {
  try {

    res.json({data: results})
  } catch (e) {
    res.status(500).send(e)
  }
}

exports.create = async (req, res, next) => {
  try {

    res.status(200).json({message:"succes"})
  } catch (e) {
    res.status(500).send(e)
  }
}

exports.update = async (req, res, next) => {
  try {

    res.status(200).json({message:"succes"})
  } catch (e) {
    res.status(500).send(e)
  }
}

exports.delete = async (req, res, next) => {
  try {

    res.status(200).json({message:"succes"})
  } catch (e) {
    res.status(500).send(e)
  }
}
